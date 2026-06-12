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
    
    <!-- Experience: LG Electronics -->
    <div class="timeline-org-group mb-5">
        <div class="d-flex justify-content-between align-items-start mb-2">
            <div>
                <strong class="text-dark d-block" style="font-size: 1.05rem;">LG Electronics (Robotics & AI Labs)</strong>
                <span class="text-muted" style="font-size: 0.88rem;">Senior Research Engineer (선임연구원) · Mar 2023 - Present</span>
            </div>
            <span class="badge badge-primary font-weight-bold px-3 py-2" style="font-size: 0.75rem;">Full-time</span>
        </div>
        <ul class="pl-3 text-muted" style="line-height: 1.75; font-size: 0.88rem;">
            <li class="mb-2"><strong>Robotics Perception & Embodied AI (Advanced Robotics Lab):</strong> Developing language-grounded robotic query-response intelligence, building robust open-world spatial perception systems, and constructing RAG-ROS2 query datasets.</li>
            <li class="mb-2"><strong>Multimodal Examodal Project (AI Lab):</strong> Co-designed large-scale Vision-Language-Audio models for appliance event detection; optimized cross-modal alignment and implemented appliance log integration.</li>
            <li><strong>Edge Quantization:</strong> Integrated action recognition and hand mesh models into TV edge devices, utilizing Quantization-Aware Training (QAT) to Qualcomm Neural SDK frameworks.</li>
        </ul>
    </div>
    
    <!-- Experience: Academic Research -->
    <div class="timeline-org-group mb-5">
        <div class="d-flex justify-content-between align-items-start mb-2">
            <div>
                <strong class="text-dark d-block" style="font-size: 1.05rem;">Korea University (PRML Lab)</strong>
                <span class="text-muted" style="font-size: 0.88rem;">M.S. in Artificial Intelligence · Sep 2021 - Feb 2023</span>
            </div>
            <span class="badge badge-secondary font-weight-bold px-3 py-2" style="font-size: 0.75rem;">Research</span>
        </div>
        <ul class="pl-3 text-muted" style="line-height: 1.75; font-size: 0.88rem;">
            <li class="mb-2"><strong>Video Pose Estimation:</strong> Designed physical law-guided hierarchical attention transformers (HANet) to tackle joint jitter. Published at top computer vision venue <strong>WACV 2023 (Oral)</strong>.</li>
            <li class="mb-2"><strong>Occlusion-Aware Transformer (OTPose):</strong> Proposed self-supervised occluded-joint learning frameworks in sparse annotation videos (IEEE SMC 2022 Oral).</li>
            <li><strong>3D Mesh Recovery:</strong> Co-developed self-supervised Multi-Hypothesis Canonical lifting networks for in-the-wild video pose recovery (Pattern Recognition 2024).</li>
        </ul>
    </div>

    <!-- Side Projects & Development Experience -->
    <h4 class="font-weight-bold text-dark mt-5 mb-3"><i class="fa fa-code-fork text-primary mr-2"></i> Side Projects & Development Experience</h4>
    <div class="pl-2 mb-5">
        <ul class="pl-3 text-muted mb-0" style="line-height: 1.8; font-size: 0.92rem;">
            <li class="mb-3">
                <strong>KLUE (Jul 2019 - Present):</strong> Course evaluation service for Korea University students. Participated in planning, Frontend renewal, and Admin page development.
                <div class="text-secondary mt-1" style="font-size: 0.82rem;"><i class="fa fa-wrench mr-1"></i> React, MobX, TypeScript</div>
            </li>
            <li class="mb-3">
                <strong>da Vinci (Jul 2020 - Feb 2021):</strong> In-house startup team developing link-saving helper utilities. Maintained mobile apps, Chrome extensions, and server endpoints.
                <div class="text-secondary mt-1" style="font-size: 0.82rem;"><i class="fa fa-wrench mr-1"></i> React, React Native, MobX, Node.js, Express, AWS</div>
            </li>
            <li class="mb-3">
                <strong>Deer (Jul 2020 - Feb 2021):</strong> Shared electric kickboard service. Developed and maintained mobile app frontend elements.
                <div class="text-secondary mt-1" style="font-size: 0.82rem;"><i class="fa fa-wrench mr-1"></i> React Native, TypeScript, MobX</div>
            </li>
            <li class="mb-3">
                <strong>SubjectArea:</strong> Shopping and news utility application. Built backend servers, admin portals, and mobile app clients.
                <div class="text-secondary mt-1" style="font-size: 0.82rem;"><i class="fa fa-wrench mr-1"></i> React Native, Node.js, MongoDB, AWS, Redux</div>
            </li>
            <li class="mb-3">
                <strong>StayTuned:</strong> Frontend development for e-commerce helper utilities.
                <div class="text-secondary mt-1" style="font-size: 0.82rem;"><i class="fa fa-wrench mr-1"></i> React, Redux, AWS S3</div>
            </li>
            <li>
                <strong>BodyApp (슬기로on):</strong> Tablet-based application for anatomical visualizations and physiological descriptions.
                <div class="text-secondary mt-1" style="font-size: 0.82rem;"><i class="fa fa-wrench mr-1"></i> React Native</div>
            </li>
        </ul>
    </div>
</div>

<div class="lang-ko">
    <p class="lead mb-4"><b>시각적 지각에서 실제 동작(Embodied AI)으로 이어지는 멀티모달 지능 구축.</b></p>
    
    <!-- 실무 및 학술 경력 -->
    <h4 class="font-weight-bold text-dark mt-4 mb-3"><i class="fa fa-briefcase text-primary mr-2"></i> 실무 및 학술 연구 경력</h4>
    
    <!-- 경력: LG전자 -->
    <div class="timeline-org-group mb-5">
        <div class="d-flex justify-content-between align-items-start mb-2">
            <div>
                <strong class="text-dark d-block" style="font-size: 1.05rem;">LG전자 (로봇선행연구소 / AI연구소)</strong>
                <span class="text-muted" style="font-size: 0.88rem;">로봇 인지 태스크 선임연구원 · 2023.03 - 현재</span>
            </div>
            <span class="badge badge-primary font-weight-bold px-3 py-2" style="font-size: 0.75rem;">정직원</span>
        </div>
        <ul class="pl-3 text-muted" style="line-height: 1.75; font-size: 0.88rem;">
            <li class="mb-2"><strong>로봇 인지 및 Embodied AI (로봇선행연구소):</strong> 로봇의 시각 인지 및 자연어 기반 환경 파악 연구, RAG와 ROS2를 결합한 질의응답 모델 고도화, 전용 데이터셋 구축.</li>
            <li class="mb-2"><strong>멀티모달 가전 상황인지 (AI연구소):</strong> 대규모 영상-오디오-로그 융합 추론 모델(Examodal) 구조 설계 및 크로스모달 얼라인먼트 최적화.</li>
            <li><strong>임베디드 최적화:</strong> ONNX 및 Qualcomm Neural SDK를 이용한 행동 검출 및 손 메쉬 모델 엣지(Edge/TV) 기기 탑재 및 QAT(양자화 인식 학습) 최적화.</li>
        </ul>
    </div>
    
    <!-- 경력: 대학원 -->
    <div class="timeline-org-group mb-5">
        <div class="d-flex justify-content-between align-items-start mb-2">
            <div>
                <strong class="text-dark d-block" style="font-size: 1.05rem;">고려대학교 대학원 (인공지능학과 PRML 연구실)</strong>
                <span class="text-muted" style="font-size: 0.88rem;">인공지능학 석사 · 2021.09 - 2023.02</span>
            </div>
            <span class="badge badge-secondary font-weight-bold px-3 py-2" style="font-size: 0.75rem;">학술 연구</span>
        </div>
        <ul class="pl-3 text-muted" style="line-height: 1.75; font-size: 0.88rem;">
            <li class="mb-2"><strong>비디오 인체 포즈 추정 (HANet):</strong> 물리 운동 법칙(속도/가속도)을 활용해 프레임 간 튀는 떨림을 해결하는 트랜스포머 아키텍처 제안 (<strong>WACV 2023 Oral</strong> 발표).</li>
            <li class="mb-2"><strong>가림 현상 해결 (OTPose):</strong> 레이블링이 드문 비디오 환경에서 가려진 관절점을 가상 보정하는 Occlusion-Aware Transformer 설계 (IEEE SMC 2022 Oral).</li>
            <li><strong>3D 구조 복원 (MHCanonNet):</strong> 와일드 비디오 시각 정보의 3D 리프팅 네트워크 설계 (Pattern Recognition 2024 게재).</li>
        </ul>
    </div>

    <!-- Side Projects & Development Experience -->
    <h4 class="font-weight-bold text-dark mt-5 mb-3"><i class="fa fa-code-fork text-primary mr-2"></i> 기타 프로젝트 및 개발 경험</h4>
    <div class="pl-2 mb-5">
        <ul class="pl-3 text-muted mb-0" style="line-height: 1.8; font-size: 0.92rem;">
            <li class="mb-3">
                <strong>KLUE (2019.07 - 현재):</strong> 고려대학교 강의 평가 서비스. 기획 및 프론트엔드 리뉴얼, 관리자 대시보드 어드민 페이지 개발.
                <div class="text-secondary mt-1" style="font-size: 0.82rem;"><i class="fa fa-wrench mr-1"></i> React, MobX, TypeScript</div>
            </li>
            <li class="mb-3">
                <strong>da Vinci (2020.07 - 2021.02):</strong> 링크 아카이빙 솔루션 사내 스타트업. 크롬 확장 프로그램 및 모바일 앱 화면 개발, 백엔드 API 배포.
                <div class="text-secondary mt-1" style="font-size: 0.82rem;"><i class="fa fa-wrench mr-1"></i> React, React Native, MobX, Node.js, Express, AWS</div>
            </li>
            <li class="mb-3">
                <strong>Deer (2020.07 - 2021.02):</strong> 전동 킥보드 공유 플랫폼 디어. 하이브리드 앱 프론트엔드 모듈 개발 및 유지보수.
                <div class="text-secondary mt-1" style="font-size: 0.82rem;"><i class="fa fa-wrench mr-1"></i> React Native, TypeScript, MobX</div>
            </li>
            <li class="mb-3">
                <strong>SubjectArea:</strong> 쇼핑 및 뉴스 통합 유틸리티 앱. DB 스키마 및 백엔드 서버 설계, 앱 클라이언트 개발.
                <div class="text-secondary mt-1" style="font-size: 0.82rem;"><i class="fa fa-wrench mr-1"></i> React Native, Node.js, MongoDB, AWS, Redux</div>
            </li>
            <li class="mb-3">
                <strong>StayTuned:</strong> 이커머스 어시스턴트 프론트엔드 웹 툴 구축.
                <div class="text-secondary mt-1" style="font-size: 0.82rem;"><i class="fa fa-wrench mr-1"></i> React, Redux, AWS S3</div>
            </li>
            <li>
                <strong>슬기로on:</strong> 해부학 및 신체 구조 교육 설명을 위한 태블릿 전용 앱 데모 빌드.
                <div class="text-secondary mt-1" style="font-size: 0.82rem;"><i class="fa fa-wrench mr-1"></i> React Native</div>
            </li>
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
