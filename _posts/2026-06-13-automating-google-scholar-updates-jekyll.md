---
layout: post
title: "Automating Google Scholar Citation Scraping and Perfect Chart Alignment in Jekyll"
title_ko: "GitHub Pages 블로그에 Google Scholar 인용 지표 자동 연동 및 그래프 정렬 구현하기"
author: Kyung-Min Jin
categories: [DevOps]
tags: [Web-Scraping, Python, GitHub-Actions, Jekyll]
image: assets/images/korea logo.jpg
description: "A detailed tutorial on how to build a Python script to scrape Google Scholar metrics, bypass IP blocks using free proxies, and parse charts using coordinate logic."
description_ko: "Google Scholar의 봇 차단을 프록시 우회 기법으로 극복하고, CSS 좌표 매핑 알고리즘을 활용해 연도별 인용수 그래프를 GitHub Pages 포트폴리오에 자동 연동하는 방법을 설명합니다."
permalink: /posts/automating-google-scholar-updates/
featured: false
hidden: false
rating: 4.8

published: false
---

<div class="lang-ko" markdown="1">
# GitHub Pages 블로그에 Google Scholar 인용 지표 자동 연동 및 그래프 정렬 구현하기

학술 포트폴리오나 개인 연구용 블로그를 운영할 때, 본인의 **Google Scholar 인용수(Citations), h-index, i10-index** 및 **연도별 인용수 추이**를 항상 최신 상태로 보여주는 것은 매우 중요합니다. 하지만 매번 수동으로 업데이트하는 것은 번거로운 작업입니다.

이 문제를 해결하기 위해, 파이썬(Python) 스크립트를 통해 구글 스콜라 프로필 데이터를 실시간으로 파싱하고 Jekyll 데이터 구조(`_data/scholar.json`)에 연동하는 자동화 파이프라인 구축 과정을 소개합니다. 특히 구글의 엄격한 **봇 차단(HTTP 403 Forbidden) 우회 기법**과 **CSS 좌표 기반 차트 데이터 추출 알고리즘**을 중점적으로 다룹니다.

---

## 1. 봇 블락 극복을 위한 Proxy Fallback 메커니즘

구글은 자동화된 스크래핑 요청을 탐지하여 빈번하게 차단(HTTP 403)하거나 캡차(CAPTCHA) 페이지를 띄웁니다. 이를 해결하기 위해 **무료 퍼블릭 프록시 풀(Public Proxy Pool)**을 사용한 Fallback 로직을 탑재했습니다.

```python
# 1. GitHub 오픈소스 프록시 리스트에서 동적으로 프록시 목록 획득
def get_free_proxies():
    urls = [
        "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt"
    ]
    proxies = []
    # ... http 프록시 목록을 파싱 및 중복 제거하여 리스트로 보관 ...
    return deduped
```

스크립트는 먼저 다이렉트로 구글 스콜라 프로필에 접근을 시도합니다. 만약 차단될 경우, 수집된 프록시 서버 목록에서 임의의 서버를 교체해가며 성공할 때까지 순차적으로 요청을 시도(Failover)합니다.

---

## 2. CSS 좌표 기반 그래프 데이터 정렬 (Coordinate Matching)

구글 스콜라의 연도별 인용수 그래프는 일반적인 테이블 포맷이 아닙니다. 연도를 나타내는 레이블(`span.gsc_g_t`)과 데이터 바(`a.gsc_g_a`)가 웹페이지 상에서 **절대 좌표(Absolute Positioning)** 값으로 떨어져 렌더링됩니다.

HTML 파싱 시 이 둘의 매핑 순서가 어긋나는 문제를 방지하기 위해, 스타일 태그 내의 `right: XXpx` 속성에서 픽셀 좌표를 파싱한 뒤 **두 좌표 간 차이의 절대값이 최소가 되는 쌍을 매칭**하는 알고리즘을 사용합니다.

```python
# 1. 각 연도 레이블의 가로 좌표 파싱
years_list = []
for span in soup.find_all('span', class_='gsc_g_t'):
    right_px = int(re.search(r'right:\s*(\d+)px', span.get('style', '')).group(1))
    years_list.append((right_px, span.text.strip()))

# 2. 각 그래프 바의 가로 좌표 및 값 파싱
values_list = []
for a in soup.find_all('a', class_='gsc_g_a'):
    right_px = int(re.search(r'right:\s*(\d+)px', a.get('style', '')).group(1))
    val = int(a.find('span', class_='gsc_g_al').text.strip())
    values_list.append((right_px, val))

# 3. 좌표 정밀 매칭 (Minimum Coordinate Difference)
graph_data = []
for y_right, y_text in years_list:
    best_val = 0
    min_diff = 9999
    for v_right, v_val in values_list:
        diff = abs(y_right - v_right)
        if diff < min_diff:
            min_diff = diff
            best_val = v_val
    graph_data.append({"year": y_text, "citations": best_val})
```

이 알고리즘을 사용하면 반응형으로 렌더링되면서 꼬인 HTML 노드 순서에 상관없이 연도와 인용수 수치를 정확하게 정렬할 수 있습니다.

---

## 3. GitHub Actions를 통한 일배치 자동화

위 스크립트를 매일 자동으로 구동해 블로그에 반영하도록 `.github/workflows/update_scholar.yml`을 구성합니다.

```yaml
name: Update Google Scholar Metrics
on:
  schedule:
    - cron: '0 0 * * *' # 매일 자정 실행
  workflow_dispatch:   # 수동 실행 지원

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Install Dependencies
        run: pip install beautifulsoup4 lxml
      - name: Run Scraper
        run: python scripts/update_scholar.py
      - name: Commit and Push
        run: |
          git config --global user.name "GitHub Action"
          git config --global user.email "action@github.com"
          git add _data/scholar.json
          git diff-index --quiet HEAD || git commit -m "Update Scholar metrics" && git push
```

이제 매일 자정이 되면 깃허브 액션이 자동으로 프로필을 긁어와 `_data/scholar.json`을 업데이트하고 블로그에 푸시합니다. 블로그 프론트엔드(`index.html` 또는 `publications.md`)에서는 해당 JSON 파일을 Liquid 템플릿 문법으로 불러와 항상 실시간 지표를 표시하게 됩니다.
</div>

<div class="lang-en" markdown="1">
# Automating Google Scholar Citation Scraping and Perfect Chart Alignment in Jekyll

When maintaining an academic portfolio or research blog, displaying key metrics like **Citations, h-index, i10-index**, and **yearly citation trends** from your Google Scholar profile is essential. However, updating these numbers manually is tedious.

This post explains how to build an automated pipeline using Python to scrape Google Scholar profile data and sync it directly into Jekyll's data directory (`_data/scholar.json`). We will focus on two major technical challenges: **bypassing Google's anti-bot block (HTTP 403)** using a proxy failover, and **aligning absolute-positioned chart elements** using layout coordinates.

---

## 1. Bypassing Bot Blocks via Proxy Fallback

Google aggressively blocks automated scrapers with HTTP 403 Forbidden responses or CAPTCHA pages. To address this, we implement a proxy fallback mechanism that fetches free public HTTP proxies dynamically:

```python
# 1. Fetch public proxies from open-source GitHub repositories
def get_free_proxies():
    urls = [
        "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt"
    ]
    proxies = []
    # ... parse and deduplicate proxy lists ...
    return deduped
```

The script initially tries to access the profile directly. If blocked, it cycles through the harvested proxy servers until the page fetches successfully.

---

## 2. Aligning Chart Data via Coordinate Matching

Google Scholar's yearly citation chart is not rendered as a standard table. Instead, the year labels (`span.gsc_g_t`) and the data bar nodes (`a.gsc_g_a`) are positioned absolutely on the page using pixel offsets in their `style` attributes.

To prevent mismatches caused by misaligned HTML structures, we parse the pixel values from the `right: XXpx` property and map each year label to its nearest bar by finding the **minimum coordinate difference**:

```python
# 1. Parse right offsets for year labels
years_list = []
for span in soup.find_all('span', class_='gsc_g_t'):
    right_px = int(re.search(r'right:\s*(\d+)px', span.get('style', '')).group(1))
    years_list.append((right_px, span.text.strip()))

# 2. Parse right offsets and heights for chart bars
values_list = []
for a in soup.find_all('a', class_='gsc_g_a'):
    right_px = int(re.search(r'right:\s*(\d+)px', a.get('style', '')).group(1))
    val = int(a.find('span', class_='gsc_g_al').text.strip())
    values_list.append((right_px, val))

# 3. Coordinate alignment (Minimum Coordinate Difference)
graph_data = []
for y_right, y_text in years_list:
    best_val = 0
    min_diff = 9999
    for v_right, v_val in values_list:
        diff = abs(y_right - v_right)
        if diff < min_diff:
            min_diff = diff
            best_val = v_val
    graph_data.append({"year": y_text, "citations": best_val})
```

This ensures that the years and citation frequencies are perfectly aligned regardless of HTML element ordering.

---

## 3. Daily Automations via GitHub Actions

We automate the script execution using a GitHub Action workflow `.github/workflows/update_scholar.yml`:

```yaml
name: Update Google Scholar Metrics
on:
  schedule:
    - cron: '0 0 * * *' # Executes daily at midnight
  workflow_dispatch:   # Supports manual trigger

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Install Dependencies
        run: pip install beautifulsoup4 lxml
      - name: Run Scraper
        run: python scripts/update_scholar.py
      - name: Commit and Push
        run: |
          git config --global user.name "GitHub Action"
          git config --global user.email "action@github.com"
          git add _data/scholar.json
          git diff-index --quiet HEAD || git commit -m "Update Scholar metrics" && git push
```

Every night, GitHub Actions triggers the script, updates `_data/scholar.json`, and pushes the changes. The Jekyll site then uses Liquid templates to render dynamic, up-to-date metrics seamlessly.
</div>
