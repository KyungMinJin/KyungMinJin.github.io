---
layout: page
title: CV
permalink: /about
comments: true
---

<div class="row justify-content-center">
<div class="col-md-8 pr-md-5">

<div class="lang-en">
    <p>I am Kyung-Min Jin, completed my master’s studies in the Graduate School of Artificial Intelligence at Korea University <a target="_blank" href="http://pr.korea.ac.kr/">(PRML Lab)</a>, where I was advised by Prof. Seong-Hwan Lee. Before studying at graduate school, I received Bachelor's degrees (Computer Science and Engineering) and (Artificial Intelligence) at Korea University in 2021.</p>
    
    <p><b>Building multimodal intelligence from visual perception to embodied reasoning.</b></p>
    
    <p>My research began in the computer vision domain, where I designed novel pose estimation frameworks that combine transformer-based architectures with convolutional neural networks. This work achieved state-of-the-art performance across multiple benchmarks and led to publications in international conferences and peer-reviewed journals, including WACV.</p>
    
    <p>After joining LG Electronics, I worked on deploying body and hand pose estimation models to edge devices, focusing on efficiency and robustness in real-world environments. As my research interests expanded, I transitioned toward multimodal learning, contributing to the development of large-scale Vision–Language–Audio models, cross-modal continual learning strategies, and reinforcement learning–based policy optimization methods such as GRPO and DPO.</p>
    
    <p>More recently, I have been working within an advanced robotics research team, where my focus is on robotic perception and natural language–based object understanding. My current research aims to bridge multimodal foundation models with embodied AI, enabling robots to ground language in visual perception and interact with the physical world more effectively. </p>
    
    <p>For more detailed information about my background and experience, please refer to my <a target="_blank" href="https://kyungminjin.github.io/CV.pdf">CV</a>.</p>
</div>

<div class="lang-ko">
    <p>저는 고려대학교 인공지능대학원 <a target="_blank" href="http://pr.korea.ac.kr/">PRML 연구실</a>에서 이성환 교수님의 지도 아래 석사 과정을 마친 진경민입니다. 대학원 진학 이전에는 고려대학교에서 컴퓨터공학과와 인공지능을 전공하여 2021년에 학사 학위를 취득했습니다.</p>
    
    <p><b>시각적 지각에서 실제 동작(Embodied AI)으로 이어지는 멀티모달 지능 구축.</b></p>
    
    <p>저의 연구는 컴퓨터 비전 분야에서 시작되었으며, 트랜스포머 아키텍처와 합성곱 신경망을 결합한 새로운 포즈 추정 프레임워크를 제안해 다수의 벤치마크에서 최고 수준의 성능을 달성했습니다. 이러한 연구 성과를 바탕으로 WACV를 포함한 국제 학회 및 저널에 논문을 게재했습니다.</p>
    
    <p>이후 LG전자에 합류하여 인체 및 손 포즈 추정 모델을 엣지 디바이스 환경에 적용하는 연구를 수행하며, 실제 환경에서의 효율성과 강건성을 중심으로 한 모델 개발에 참여했습니다. 연구 관심사는 점차 확장되어 Vision–Language–Audio 기반의 대규모 멀티모달 모델, 교차 모달 지속 학습(Continual Learning) 전략, 그리고 GRPO 및 DPO와 같은 강화학습 기반 정책 최적화 기법을 활용한 멀티모달 학습 연구를 진행했습니다.</p>
    
    <p>최근에는 로봇 선행 연구 조직에서 로봇 인지 및 자연어 기반 객체 이해 기술을 연구하고 있으며, 멀티모달 파운데이션 모델과 Embodied 인공지능(Embodied AI)을 연결해 로봇이 시각 정보를 언어적으로 이해하고 물리적 환경과 효과적으로 상호작용할 수 있도록 하는 것을 목표로 하고 있습니다.</p>
    
    <p>더 자세한 경력은 <a target="_blank" href="https://kyungminjin.github.io/CV.pdf">이력서(CV)</a>를 참고해주세요.</p>
</div>

</div> <!-- col-md-8 끝 -->
</div> <!-- row 끝 (소개 Row) -->

<div class="row mt-5 pt-4 border-top justify-content-center">
<div class="col-md-6 mb-4">

<!-- Google Scholar Metrics & Citation Graph -->
<div class="card border shadow-sm p-3 pt-2 pb-2 bg-white h-100">
    <h6 class="font-weight-bold text-dark border-bottom pb-2 mb-3">
        <i class="fa fa-graduation-cap text-info"></i>
        <span class="lang-en">Google Scholar Metrics</span>
        <span class="lang-ko">구글 스콜라 지표</span>
    </h6>
    {% assign s_data = site.data.scholar %}
    <table class="table table-sm table-borderless mb-3" style="font-size: 0.9rem;">
        <thead>
            <tr class="text-secondary" style="font-size: 0.75rem; border-bottom: 1px solid #eee;">
                <th>
                    <span class="lang-en">Metric</span>
                    <span class="lang-ko">지표</span>
                </th>
                <th class="text-right">
                    <span class="lang-en">All</span>
                    <span class="lang-ko">전체</span>
                </th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="text-dark py-1">
                    <span class="lang-en">Citations</span>
                    <span class="lang-ko">인용 횟수</span>
                </td>
                <td class="text-right font-weight-bold py-1">{{ s_data.citations }}</td>
            </tr>
            <tr>
                <td class="text-dark py-1">h-index</td>
                <td class="text-right font-weight-bold py-1">{{ s_data.h_index }}</td>
            </tr>
            <tr>
                <td class="text-dark py-1">i10-index</td>
                <td class="text-right font-weight-bold py-1">{{ s_data.i10_index }}</td>
            </tr>
        </tbody>
    </table>
    
    <div class="scholar-graph-container mt-2">
        <div class="scholar-graph-title text-secondary mb-2" style="font-size: 0.75rem; font-weight: 600;">
            <span class="lang-en">Citations per year</span>
            <span class="lang-ko">연도별 인용 횟수</span>
        </div>
        
        {% assign max_cites = 1 %}
        {% for item in s_data.graph %}
            {% if item.citations > max_cites %}
                {% assign max_cites = item.citations %}
            {% endif %}
        {% endfor %}
        
        <div class="scholar-graph px-1">
            <!-- Y-axis Guidelines & Labels -->
            <div class="scholar-y-line" style="bottom: 160px;"></div>
            <span class="scholar-y-label" style="bottom: 160px;">{{ max_cites }}</span>

            {% assign mid_cites = max_cites | divided_by: 2 %}
            <div class="scholar-y-line" style="bottom: 80px;"></div>
            <span class="scholar-y-label" style="bottom: 80px;">{{ mid_cites }}</span>

            <div class="scholar-y-line" style="bottom: 0px;"></div>
            <span class="scholar-y-label" style="bottom: 0px;">0</span>

            {% for item in s_data.graph %}
                {% assign bar_height = item.citations | times: 160 | divided_by: max_cites %}
                {% if item.citations > 0 and bar_height < 5 %}
                    {% assign bar_height = 5 %}
                {% endif %}
                <div class="scholar-bar-wrapper">
                    <span class="scholar-value">{{ item.citations }}</span>
                    <div class="scholar-bar" style="height: {{ bar_height }}px;" 
                         data-tooltip="{{ item.full_year }}: {{ item.citations }} citations" 
                         title="{{ item.full_year }}: {{ item.citations }} citations"></div>
                    <span class="scholar-year">
                        {% if item.citations > 0 %}
                            {{ item.year }}
                        {% else %}
                            &nbsp;
                        {% endif %}
                    </span>
                </div>
            {% endfor %}
        </div>
    </div>
</div>

</div>

<div class="col-md-6 mb-4 text-center">

<!-- Visitor Analytics Widget -->
<div class="card border shadow-sm p-3 pt-2 pb-2 bg-white h-100 d-flex flex-column justify-content-between">
    <h6 class="font-weight-bold text-dark border-bottom pb-2 mb-3 text-left">
        <i class="fa fa-globe text-secondary"></i>
        <span class="lang-en">Visitor Map</span>
        <span class="lang-ko">방문자 분포 지도</span>
    </h6>
    <div class="visitor-map-container" style="min-height: 150px; display: flex; align-items: center; justify-content: center;">
        <a href="https://clustrmaps.com/site/1bxe2" title="Visit tracker" target="_blank" style="width: 100%;">
            <img src="https://cdn.clustrmaps.com/map_v2.png?d=2c9zJ45T_lQh5Jc7f21n40x36-g6i1v7k&cl=ffffff" 
                 alt="Visitor Map" 
                 referrerpolicy="no-referrer"
                 style="max-width: 100%; height: auto; border-radius: 8px; border: 1px solid #f1f3f5;"
                 onerror="this.onerror=null; this.src='https://cdn.clustrmaps.com/map_v2.png?d=2c9zJ45T_lQh5Jc7f21n40x36-g6i1v7k';" />
        </a>
    </div>
    <div class="mt-3">
        <img src="https://visitor-badge.laobi.icu/badge?page_id=kyungminjin.github.io&title=Total+Visits&color=4a777a" alt="Total Visits" style="border-radius: 4px;"/>
    </div>
</div>

</div>
</div>

<!-- Collapsible PDF CV Viewer -->
<hr class="my-5">

<div class="row">
    <div class="col-md-12">
        <details class="cv-viewer-details border rounded shadow-sm" open>
            <summary class="font-weight-bold p-3 text-dark bg-light" style="cursor: pointer; list-style: none; outline: none; display: flex; align-items: center; justify-content: space-between;">
                <span>
                    <i class="fa fa-file-pdf-o text-danger mr-2"></i>
                    <span class="lang-en">Click to View Interactive PDF CV</span>
                    <span class="lang-ko">대화형 PDF 이력서 보기</span>
                </span>
                <i class="fa fa-chevron-down toggle-icon text-muted" style="transition: transform 0.2s ease;"></i>
            </summary>
            <div class="p-4 bg-white border-top">
                <p class="text-muted mb-3 lang-en" style="font-size: 0.9rem;">You can view and navigate the detailed Curriculum Vitae directly below, or click <a href="{{ site.baseurl }}/CV.pdf" target="_blank" class="font-weight-bold text-primary">here</a> to open it in a new tab.</p>
                <p class="text-muted mb-3 lang-ko" style="font-size: 0.9rem;">아래에서 상세 이력서(CV)를 확인하고 탐색할 수 있으며, <a href="{{ site.baseurl }}/CV.pdf" target="_blank" class="font-weight-bold text-primary">여기</a>를 클릭하여 새 창에서 열어볼 수도 있습니다.</p>
                <div class="embed-responsive shadow-sm border rounded" style="height: 800px; background: #f8f9fa;">
                    <iframe class="embed-responsive-item" src="{{ site.baseurl }}/CV.pdf" allowfullscreen></iframe>
                </div>
            </div>
        </details>
    </div>
</div>
