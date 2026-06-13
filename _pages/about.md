---
layout: page
title: "CV | ML Engineer & AI Researcher"
permalink: /about
comments: true
---

<!-- Include Chart.js via CDN -->
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<div class="row justify-content-center">
<div class="col-md-10">

<!-- Interactive Radar Chart & Core Competencies Side-by-Side -->
<div class="row mt-2 mb-5">
    <!-- Skills Radar Chart Card (col-md-5) -->
    <div class="col-md-5 mb-4">
        <div class="card shadow-sm border-0 p-3 bg-white h-100" style="border-radius: 12px;">
            <h5 class="font-weight-bold text-dark mb-3 text-center lang-en" style="font-size: 1rem;"><i class="fa fa-pie-chart text-info mr-1"></i> Expertise Radar</h5>
            <h5 class="font-weight-bold text-dark mb-3 text-center lang-ko" style="font-size: 1rem;"><i class="fa fa-pie-chart text-info mr-1"></i> 직무 역량 레이더</h5>
            <div style="position: relative; height: 260px; width: 100%;">
                <canvas id="skillsRadarChart"></canvas>
            </div>
            <div class="mt-3 text-muted text-center" style="font-size: 0.78rem; line-height: 1.5;">
                <span class="lang-en">Balanced engineering capabilities spanning Multimodal AI, CV models, Quantization, Robot systems, and Frontend applications.</span>
                <span class="lang-ko">멀티모달 AI, 컴퓨터 비전, 경량화/양자화, 로봇 시스템, 프론트엔드를 고루 다루는 융합형 역량 그래프입니다.</span>
            </div>
        </div>
    </div>
    
    <!-- Core Research Competency (col-md-7) -->
    <div class="col-md-7 mb-4">
        <div class="card shadow-sm border-0 p-4 bg-white h-100" style="border-radius: 12px;">
            <h5 class="font-weight-bold text-dark mb-3 lang-en"><i class="fa fa-star text-warning mr-2"></i> Core Competencies</h5>
            <h5 class="font-weight-bold text-dark mb-3 lang-ko"><i class="fa fa-star text-warning mr-2"></i> 핵심 연구 및 실무 역량</h5>
            <ul class="pl-3 text-muted mb-0" style="line-height: 1.75; font-size: 0.88rem;">
                <li class="mb-2"><strong>AI Research & Multimodal:</strong> VLM/MLM (Examodal), Instruction Tuning, Cross-modal Alignment, GRPO/DPO policy optimization.</li>
                <li class="mb-2"><strong>Computer Vision:</strong> 2D/3D human and hand pose estimation, transformer models, joint occlusion, tracking.</li>
                <li class="mb-2"><strong>On-device & Quantization:</strong> Quantized-Aware Training (QAT), model pruning, edge deployment (Qualcomm Neural SDK, ONNX).</li>
                <li class="mb-2"><strong>Robotic Systems:</strong> Robotic query response, RAG + ROS2 integration, query datasets.</li>
                <li><strong>Frontend & Dev:</strong> React, TypeScript, React Native, MobX/Redux, Chrome extensions.</li>
            </ul>
        </div>
    </div>
</div>

<div class="lang-en">
    <p class="lead mb-4"><strong>Building multimodal intelligence from visual perception to embodied reasoning.</strong></p>
    
    <!-- Professional Experience -->
    <h4 class="font-weight-bold text-dark mt-4 mb-3"><i class="fa fa-briefcase text-primary mr-2"></i> Professional Experience</h4>
    
    {% include timeline-about.html %}

    <!-- Side Projects & Development Experience -->
    <h4 class="font-weight-bold text-dark mt-5 mb-3"><i class="fa fa-code-fork text-primary mr-2"></i> Side Projects & Development Experience</h4>
    <div class="pl-2 mb-5">
        <ul class="pl-3 text-muted mb-0" style="line-height: 1.8; font-size: 0.92rem;">
            {% for project in site.data.projects.early_projects %}
            <li class="mb-3">
                <strong>{{ project.title }} ({{ project.duration }}):</strong> {{ project.desc }}
                <div class="text-secondary mt-1" style="font-size: 0.82rem;">
                    <i class="fa fa-wrench mr-1"></i> 
                    {% for tag in project.tags %}{{ tag }}{% unless forloop.last %}, {% endunless %}{% endfor %}
                </div>
            </li>
            {% endfor %}
        </ul>
    </div>
</div>

<div class="lang-ko">
    <p class="lead mb-4"><b>시각적 지각에서 실제 동작(Embodied AI)으로 이어지는 멀티모달 지능 구축.</b></p>
    
    <!-- 실무 및 학술 경력 -->
    <h4 class="font-weight-bold text-dark mt-4 mb-3"><i class="fa fa-briefcase text-primary mr-2"></i> 실무 및 학술 연구 경력</h4>
    
    {% include timeline-about.html %}

    <!-- Side Projects & Development Experience -->
    <h4 class="font-weight-bold text-dark mt-5 mb-3"><i class="fa fa-code-fork text-primary mr-2"></i> 기타 프로젝트 및 개발 경험</h4>
    <div class="pl-2 mb-5">
        <ul class="pl-3 text-muted mb-0" style="line-height: 1.8; font-size: 0.92rem;">
            {% for project in site.data.projects.early_projects %}
            <li class="mb-3">
                <strong>{{ project.title }} ({{ project.duration }}):</strong> {{ project.desc }}
                <div class="text-secondary mt-1" style="font-size: 0.82rem;">
                    <i class="fa fa-wrench mr-1"></i> 
                    {% for tag in project.tags %}{{ tag }}{% unless forloop.last %}, {% endunless %}{% endfor %}
                </div>
            </li>
            {% endfor %}
        </ul>
    </div>
</div>

</div> <!-- col-md-10 끝 -->
</div> <!-- row 끝 (소개 Row) -->

<!-- Friendly CV Download Section -->
<hr class="my-5">

<div class="row justify-content-center text-center mb-5">
    <div class="col-md-8">
        <h5 class="font-weight-bold text-dark mb-3 lang-en">Looking for the full Curriculum Vitae?</h5>
        <h5 class="font-weight-bold text-dark mb-3 lang-ko">상세 이력서가 필요하신가요?</h5>
        <p class="text-muted mb-4" style="font-size: 0.9rem; line-height: 1.6;">
            <span class="lang-en">Click below to download the latest PDF version of the CV, detailing all publications, coursework, and side-projects.</span>
            <span class="lang-ko">출판 논문 목록, 상세 이수 과목, 사이드 프로젝트 기록이 포함된 최신 PDF 이력서를 아래에서 손쉽게 다운로드하실 수 있습니다.</span>
        </p>
        <div class="d-flex justify-content-center gap-3 flex-wrap">
            <a href="{{ site.baseurl }}/CV.pdf" download="KyungMinJin_CV.pdf" class="btn btn-outline-primary font-weight-bold px-4 py-2 text-uppercase shadow-sm" style="border-radius: 30px; font-size: 0.85rem; letter-spacing: 0.5px;">
                <i class="fa fa-download mr-2"></i> 
                <span class="lang-en">Download CV (PDF)</span>
                <span class="lang-ko">이력서 다운로드 (PDF)</span>
            </a>
        </div>
    </div>
</div>

<!-- Render Radar Chart script -->
<script>
document.addEventListener("DOMContentLoaded", function() {
    var ctx = document.getElementById('skillsRadarChart').getContext('2d');
    var isDark = document.documentElement.classList.contains("dark-mode");
    
    function getChartColors(dark) {
        return {
            grid: dark ? 'rgba(255, 255, 255, 0.12)' : 'rgba(0, 0, 0, 0.08)',
            angleLines: dark ? 'rgba(255, 255, 255, 0.15)' : 'rgba(0, 0, 0, 0.1)',
            labels: dark ? '#e0e0e0' : '#4a4a4a',
            pointLabel: dark ? '#ffffff' : '#2b2b2b',
            fill: dark ? 'rgba(74, 119, 122, 0.25)' : 'rgba(74, 119, 122, 0.2)',
            stroke: '#4a777a',
            point: '#4a777a'
        };
    }
    
    var colors = getChartColors(isDark);
    
    // Check page language to localize chart labels
    var isKo = document.documentElement.classList.contains("lang-mode-ko");
    var chartLabels = isKo ? 
        ['멀티모달 AI', '컴퓨터 비전', '경량화/양자화', '로봇 & RAG', '프론트엔드'] :
        ['Multimodal AI', 'Computer Vision', 'Edge Quantization', 'Robotics & RAG', 'Frontend Dev'];
        
    var config = {
        type: 'radar',
        data: {
            labels: chartLabels,
            datasets: [{
                label: isKo ? '역량 수준' : 'Skill Level',
                data: [95, 95, 85, 90, 85],
                backgroundColor: colors.fill,
                borderColor: colors.stroke,
                borderWidth: 2,
                pointBackgroundColor: colors.point,
                pointBorderColor: '#fff',
                pointHoverBackgroundColor: '#fff',
                pointHoverBorderColor: colors.point,
                pointRadius: 4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return context.label + ': ' + context.raw + '%';
                        }
                    }
                }
            },
            scales: {
                r: {
                    angleLines: {
                        color: colors.angleLines
                    },
                    grid: {
                        color: colors.grid
                    },
                    pointLabels: {
                        color: colors.pointLabel,
                        font: {
                            size: 11,
                            weight: '600',
                            family: 'Inter, system-ui, sans-serif'
                        }
                    },
                    ticks: {
                        display: false,
                        stepSize: 20
                    },
                    min: 0,
                    max: 100
                }
            }
        }
    };
    
    var myChart = new Chart(ctx, config);
    
    // Listen to theme-changed events to dynamically update chart colors
    window.addEventListener('theme-changed', function() {
        var dark = document.documentElement.classList.contains("dark-mode");
        var activeColors = getChartColors(dark);
        
        myChart.options.scales.r.angleLines.color = activeColors.angleLines;
        myChart.options.scales.r.grid.color = activeColors.grid;
        myChart.options.scales.r.pointLabels.color = activeColors.pointLabel;
        
        myChart.data.datasets[0].backgroundColor = activeColors.fill;
        myChart.data.datasets[0].borderColor = activeColors.stroke;
        myChart.data.datasets[0].pointBackgroundColor = activeColors.point;
        
        myChart.update();
    });
    
    // Custom trigger for direct lang dropdown click
    var checkLangInterval = setInterval(function() {
        var ko = document.documentElement.classList.contains("lang-mode-ko");
        var currentLabels = ko ? 
            ['멀티모달 AI', '컴퓨터 비전', '경량화/양자화', '로봇 & RAG', '프론트엔드'] :
            ['Multimodal AI', 'Computer Vision', 'Edge Quantization', 'Robotics & RAG', 'Frontend Dev'];
            
        if (myChart.data.labels[0] !== currentLabels[0]) {
            myChart.data.labels = currentLabels;
            myChart.update();
        }
    }, 500);
});
</script>
