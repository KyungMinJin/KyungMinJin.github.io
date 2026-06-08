import re
import json
import urllib.request
import sys
import time
from bs4 import BeautifulSoup

URL = "https://scholar.google.com/citations?user=-d9eXb4AAAAJ&hl=en"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5'
}

def fetch_profile(url, max_retries=3):
    for attempt in range(max_retries):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as response:
                return response.read()
        except Exception as e:
            print(f"Scraper attempt {attempt + 1} failed: {e}", file=sys.stderr)
            if attempt < max_retries - 1:
                time.sleep(3)
            else:
                raise e

try:
    print(f"Fetching Google Scholar profile from {URL}...")
    html = fetch_profile(URL)
    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Parse table metrics (Citations, h-index, i10-index)
    stats_table = soup.find('table', id='gsc_rsb_st')
    stats = {}
    if stats_table:
        rows = stats_table.find_all('tr')[1:] # Skip header
        for r in rows:
            cols = r.find_all('td')
            if len(cols) >= 2:
                name_td = cols[0].find('a') or cols[0]
                name = name_td.text.strip().lower().replace('-', '_').replace(' ', '_')
                val = cols[1].text.strip()
                stats[name] = int(val) if val.isdigit() else val
    print(f"Parsed table metrics: {stats}")

    # 2. Extract layout coordinates to align years and citations perfectly
    years_list = []
    for span in soup.find_all('span', class_='gsc_g_t'):
        style = span.get('style', '')
        match = re.search(r'right:\s*(\d+)px', style)
        if match:
            right_px = int(match.group(1))
            years_list.append((right_px, span.text.strip()))

    values_list = []
    for a in soup.find_all('a', class_='gsc_g_a'):
        style = a.get('style', '')
        match = re.search(r'right:\s*(\d+)px', style)
        if match:
            right_px = int(match.group(1))
            val_span = a.find('span', class_='gsc_g_al')
            val = int(val_span.text.strip()) if val_span and val_span.text.strip().isdigit() else 0
            values_list.append((right_px, val))

    print(f"Raw coordinates parsed: Years={years_list}, Bars={values_list}")

    # Map each year to its nearest bar by finding the minimum coordinate difference
    graph_data = []
    for y_right, y_text in years_list:
        best_val = 0
        min_diff = 9999
        for v_right, v_val in values_list:
            diff = abs(y_right - v_right)
            if diff < min_diff:
                min_diff = diff
                best_val = v_val
        
        graph_data.append({
            "year": y_text[-2:],
            "full_year": y_text,
            "citations": best_val
        })
        
    # Sort chronologically (oldest to newest)
    graph_data.sort(key=lambda x: x["full_year"])
    print(f"Aligned Graph Data: {graph_data}")
    
    # Save output
    final_citations = stats.get("citations", 94)
    final_h_index = stats.get("h_index", stats.get("hindex", 5))
    final_i10_index = stats.get("i10_index", stats.get("i10index", 4))

    data = {
        "citations": final_citations,
        "h_index": final_h_index,
        "i10_index": final_i10_index,
        "graph": graph_data
    }
    
    with open('_data/scholar.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        
    print("Google Scholar metrics updated successfully in _data/scholar.json.")
except Exception as e:
    print(f"Error executing scraper: {e}", file=sys.stderr)
    sys.exit(1)
