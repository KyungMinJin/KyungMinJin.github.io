import re
import json
import urllib.request
import sys
from bs4 import BeautifulSoup

URL = "https://scholar.google.com/citations?user=-d9eXb4AAAAJ&hl=en"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

try:
    print(f"Fetching Google Scholar profile from {URL}...")
    req = urllib.request.Request(URL, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as response:
        html = response.read()
    
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

    # 2. Parse Year Graph (using grid-column index parsing to ensure correct mapping)
    years_dict = {}
    for span in soup.find_all('span', class_='gsc_g_t'):
        style = span.get('style', '')
        # Match grid-column-start: \d+ or grid-column: \d+
        match = re.search(r'grid-column(?:-start)?:\s*(\d+)', style)
        if match:
            col = int(match.group(1))
            years_dict[col] = span.text.strip()
        else:
            # Fallback if style layout is different
            # Try to find index of this span among siblings
            siblings = list(span.parent.find_all('span', class_='gsc_g_t'))
            idx = siblings.index(span) + 1
            years_dict[idx] = span.text.strip()

    values_dict = {}
    for a in soup.find_all('a', class_='gsc_g_a'):
        style = a.get('style', '')
        match = re.search(r'grid-column(?:-start)?:\s*(\d+)', style)
        col = int(match.group(1)) if match else None
        
        # If no grid column start, match by its position among siblings
        if col is None:
            siblings = list(a.parent.find_all('a', class_='gsc_g_a'))
            # We match by index since there might be fewer bars than years
            # If so, z-index style or left style is used
            z_match = re.search(r'z-index:\s*(\d+)', style)
            if z_match:
                col = int(z_match.group(1))
            else:
                col = siblings.index(a) + 1
                
        val_span = a.find('span', class_='gsc_g_al')
        val = int(val_span.text.strip()) if val_span and val_span.text.strip().isdigit() else 0
        if col:
            values_dict[col] = val

    print(f"Years mapped: {years_dict}")
    print(f"Values mapped: {values_dict}")

    graph_data = []
    if years_dict:
        # Use column mapping if available
        for col in sorted(years_dict.keys()):
            yr = years_dict[col]
            val = values_dict.get(col, 0)
            graph_data.append({
                "year": yr[-2:],
                "full_year": yr,
                "citations": val
            })
    else:
        # Fallback to simple zip
        years = [span.text.strip() for span in soup.find_all('span', class_='gsc_g_t')]
        values = []
        for a in soup.find_all('a', class_='gsc_g_a'):
            val_span = a.find('span', class_='gsc_g_al')
            values.append(int(val_span.text.strip()) if val_span and val_span.text.strip().isdigit() else 0)
        
        for yr, val in zip(years, values):
            graph_data.append({
                "year": yr[-2:],
                "full_year": yr,
                "citations": val
            })

    print(f"Final Graph Data: {graph_data}")
    
    # Standardize stats fields
    final_citations = stats.get("citations", 94)
    final_h_index = stats.get("h_index", stats.get("hindex", 5))
    final_i10_index = stats.get("i10_index", stats.get("i10index", 4))

    data = {
        "citations": final_citations,
        "h_index": final_h_index,
        "i10_index": final_i10_index,
        "graph": graph_data
    }
    
    # Save output
    with open('_data/scholar.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        
    print("Google Scholar metrics updated successfully in _data/scholar.json.")
except Exception as e:
    print(f"Error updating Google Scholar: {e}", file=sys.stderr)
    sys.exit(1)
