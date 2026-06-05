---
layout: page
title: Projects
permalink: /projects
comments: true
---

<div class="row">
    <div class="col-md-12">
        <p class="lead">A showcase of selected research, open-source, and industrial AI/Robotics projects.</p>
        <hr class="my-4">
    </div>
</div>

<div class="row">
    <!-- Project 1 -->
    <div class="col-md-12 mb-4">
        <div class="card shadow-sm border overflow-hidden">
            <div class="card-body">
                <div class="row align-items-center">
                    <div class="col-lg-8 col-md-7">
                        <div class="d-flex justify-content-between align-items-center mb-2">
                            <span class="badge badge-primary">Robotics / Embodied AI</span>
                            <small class="text-muted">2026.01 - Present</small>
                        </div>
                        <h5 class="card-title font-weight-bold text-dark mb-1">Natural Language-Based Object Understanding for Robots</h5>
                        <h6 class="card-subtitle mb-3 text-secondary">LG Electronics, Advanced Robotics Lab</h6>
                        <p class="card-text text-muted" style="font-size: 0.95rem; line-height: 1.6;">
                            Building robot perception systems that ground natural language in visual environments to enable intuitive human-robot interaction and reasoning.
                        </p>
                        <ul class="pl-3 text-muted" style="font-size: 0.9rem; line-height: 1.6;">
                            <li>Constructed a contextual Knowledge Graph and RAG-based Vector Database.</li>
                            <li>Generated QA pairs based on video shots and interaction history.</li>
                            <li>Developed a time-sensitive hybrid RAG QA system for robot reasoning.</li>
                        </ul>
                        <div class="mt-3">
                            <span class="badge badge-light border text-secondary">Python</span>
                            <span class="badge badge-light border text-secondary">PyTorch</span>
                            <span class="badge badge-light border text-secondary">LangChain</span>
                            <span class="badge badge-light border text-secondary">llama-index</span>
                            <span class="badge badge-light border text-secondary">Qdrant</span>
                        </div>
                        <div class="mt-3">
                            <a href="{{ site.baseurl }}/posts/robotics-kg/" class="btn btn-sm btn-outline-primary mr-2"><i class="fa fa-book"></i> Read Research Note</a>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-5 mt-3 mt-md-0 text-center">
                        <img class="img-fluid rounded shadow-sm border" src="{{ site.baseurl }}/assets/images/robotics_perception_kg.png" alt="Robotics Knowledge Graph" style="max-height: 200px; width: 100%; object-fit: cover;">
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Project 2 -->
    <div class="col-md-12 mb-4">
        <div class="card shadow-sm border overflow-hidden">
            <div class="card-body">
                <div class="row align-items-center">
                    <div class="col-lg-8 col-md-7">
                        <div class="d-flex justify-content-between align-items-center mb-2">
                            <span class="badge badge-success">Multimodal Learning</span>
                            <small class="text-muted">2023.07 - 2025.12</small>
                        </div>
                        <h5 class="card-title font-weight-bold text-dark mb-1">SAMIF: Semantic-Aware Mutual Information Factorized Learning</h5>
                        <h6 class="card-subtitle mb-3 text-secondary">LG Electronics, AI Lab</h6>
                        <p class="card-text text-muted" style="font-size: 0.95rem; line-height: 1.6;">
                            Researched cross-modality shared and unique information factorization strategies to improve semantic segmentation across aligned data modalities.
                        </p>
                        <ul class="pl-3 text-muted" style="font-size: 0.9rem; line-height: 1.6;">
                            <li>Designed, experimented, and validated cross-modality factorized learning frameworks.</li>
                            <li>Achieved state-of-the-art performance for multimodal semantic segmentation (2-3% improvement).</li>
                            <li>Created PoC by improving the IoU (0.3% ↑) and f1-score (23% ↑) in action localization.</li>
                        </ul>
                        <div class="mt-3">
                            <span class="badge badge-light border text-secondary">Python</span>
                            <span class="badge badge-light border text-secondary">PyTorch</span>
                            <span class="badge badge-light border text-secondary">Cross-attention</span>
                            <span class="badge badge-light border text-secondary">ONNX</span>
                            <span class="badge badge-light border text-secondary">Qualcomm SDK</span>
                        </div>
                        <div class="mt-3">
                            <a href="{{ site.baseurl }}/posts/samif/" class="btn btn-sm btn-outline-primary mr-2"><i class="fa fa-book"></i> Read Research Note</a>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-5 mt-3 mt-md-0 text-center">
                        <img class="img-fluid rounded shadow-sm border" src="{{ site.baseurl }}/assets/images/multimodal_samif.png" alt="SAMIF Architecture" style="max-height: 200px; width: 100%; object-fit: cover;">
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Project 3 -->
    <div class="col-md-12 mb-4">
        <div class="card shadow-sm border overflow-hidden">
            <div class="card-body">
                <div class="row align-items-center">
                    <div class="col-lg-8 col-md-7">
                        <div class="d-flex justify-content-between align-items-center mb-2">
                            <span class="badge badge-danger">LLM / VLM</span>
                            <small class="text-muted">LG Electronics</small>
                        </div>
                        <h5 class="card-title font-weight-bold text-dark mb-1">Small Multimodal LLM & Audio Tower Training</h5>
                        <h6 class="card-subtitle mb-3 text-secondary">LG Electronics, AI Lab</h6>
                        <p class="card-text text-muted" style="font-size: 0.95rem; line-height: 1.6;">
                            Developed small-scale multimodal language models featuring audio/vision towers and optimized using advanced policy training.
                        </p>
                        <ul class="pl-3 text-muted" style="font-size: 0.9rem; line-height: 1.6;">
                            <li>Designed an audio tower and LLM cross-modal continual learning pipeline.</li>
                            <li>Achieved a 20.7% improvement by training GRPO on synthetic data with Self-Reflection.</li>
                            <li>Served image and video-based QA demo applications within the company.</li>
                        </ul>
                        <div class="mt-3">
                            <span class="badge badge-light border text-secondary">Python</span>
                            <span class="badge badge-light border text-secondary">PyTorch</span>
                            <span class="badge badge-light border text-secondary">FastAPI</span>
                            <span class="badge badge-light border text-secondary">Transformers</span>
                            <span class="badge badge-light border text-secondary">TRL</span>
                            <span class="badge badge-light border text-secondary">Gradio</span>
                        </div>
                        <div class="mt-3">
                            <a href="{{ site.baseurl }}/posts/grpo/" class="btn btn-sm btn-outline-primary mr-2"><i class="fa fa-book"></i> Read Research Note</a>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-5 mt-3 mt-md-0 text-center">
                        <img class="img-fluid rounded shadow-sm border" src="{{ site.baseurl }}/assets/images/grpo_vlm_alignment.png" alt="GRPO VLM Alignment" style="max-height: 200px; width: 100%; object-fit: cover;">
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Project 4 -->
    <div class="col-md-12 mb-4">
        <div class="card shadow-sm border overflow-hidden">
            <div class="card-body">
                <div class="row align-items-center">
                    <div class="col-lg-8 col-md-7">
                        <div class="d-flex justify-content-between align-items-center mb-2">
                            <span class="badge badge-info">Reinforcement Learning</span>
                            <small class="text-muted">Joint Research</small>
                        </div>
                        <h5 class="card-title font-weight-bold text-dark mb-1">Fast-Reasoning Modality-Aware Policy Optimization</h5>
                        <h6 class="card-subtitle mb-3 text-secondary">LG Electronics & Toronto AI Lab</h6>
                        <p class="card-text text-muted" style="font-size: 0.95rem; line-height: 1.6;">
                            Collaborated on online policy optimization methods that apply modality-aware weighting in Group Relative Policy Optimization (GRPO).
                        </p>
                        <ul class="pl-3 text-muted" style="font-size: 0.9rem; line-height: 1.6;">
                            <li>Proposed a loss update and reward mechanism that applies modality-aware online weighting in GRPO.</li>
                            <li>Improved answer accuracy after fast reasoning by predicting missed and hallucinated cases.</li>
                            <li>Co-authored and submitted a paper on the resulting policy optimization framework.</li>
                        </ul>
                        <div class="mt-3">
                            <span class="badge badge-light border text-secondary">Python</span>
                            <span class="badge badge-light border text-secondary">PyTorch</span>
                            <span class="badge badge-light border text-secondary">veRL</span>
                            <span class="badge badge-light border text-secondary">GRPO / DPO</span>
                        </div>
                        <div class="mt-3">
                            <a href="{{ site.baseurl }}/posts/grpo/#2-modality-aware-online-weighting" class="btn btn-sm btn-outline-primary mr-2"><i class="fa fa-book"></i> View Policy Optimization Details</a>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-5 mt-3 mt-md-0 text-center">
                        <img class="img-fluid rounded shadow-sm border" src="{{ site.baseurl }}/assets/images/qat_pose_estimation.png" alt="Modality-Aware weighting" style="max-height: 200px; width: 100%; object-fit: cover;">
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Project 5 -->
    <div class="col-md-12 mb-4">
        <div class="card shadow-sm border overflow-hidden">
            <div class="card-body">
                <div class="row align-items-center">
                    <div class="col-lg-8 col-md-7">
                        <div class="d-flex justify-content-between align-items-center mb-2">
                            <span class="badge badge-warning">Computer Vision</span>
                            <small class="text-muted">Research & Deployed</small>
                        </div>
                        <h5 class="card-title font-weight-bold text-dark mb-1">Optimized Body & Hand Pose Estimation</h5>
                        <h6 class="card-subtitle mb-3 text-secondary">Korea University & LG Electronics</h6>
                        <p class="card-text text-muted" style="font-size: 0.95rem; line-height: 1.6;">
                            Developed state-of-the-art pose estimation algorithms and optimized them for edge-device integration.
                        </p>
                        <ul class="pl-3 text-muted" style="font-size: 0.9rem; line-height: 1.6;">
                            <li>Trained 2D & 3D pose estimation models using Quantization-Aware Training (QAT).</li>
                            <li>Designed RecycleNet, which re-trains synthesized hand mesh models.</li>
                            <li>Successfully deployed body pose estimation models to LG Smart TVs.</li>
                        </ul>
                        <div class="mt-3">
                            <span class="badge badge-light border text-secondary">Python</span>
                            <span class="badge badge-light border text-secondary">PyTorch</span>
                            <span class="badge badge-light border text-secondary">ONNX</span>
                            <span class="badge badge-light border text-secondary">QAT</span>
                            <span class="badge badge-light border text-secondary">Transformers</span>
                        </div>
                        <div class="mt-3">
                            <a href="{{ site.baseurl }}/posts/hanet/" class="btn btn-sm btn-outline-primary mr-2"><i class="fa fa-book"></i> Read HANet Paper Summary</a>
                            <a href="https://github.com/KyungMinJin/HANet" target="_blank" class="btn btn-sm btn-outline-dark"><i class="fa fa-github"></i> GitHub Code</a>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-5 mt-3 mt-md-0 text-center">
                        <img class="img-fluid rounded shadow-sm border" src="{{ site.baseurl }}/assets/images/jhmdb.gif" alt="Pose Estimation Tracking" style="max-height: 200px; width: 100%; object-fit: cover;">
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Project 6 -->
    <div class="col-md-12 mb-4">
        <div class="card shadow-sm border overflow-hidden">
            <div class="card-body">
                <div class="row align-items-center">
                    <div class="col-lg-8 col-md-7">
                        <div class="d-flex justify-content-between align-items-center mb-2">
                            <span class="badge badge-secondary">Embedded AI</span>
                            <small class="text-muted">2020.05 - 2020.11</small>
                        </div>
                        <h5 class="card-title font-weight-bold text-dark mb-1">Golf Pose Estimation & Action Localization</h5>
                        <h6 class="card-subtitle mb-3 text-secondary">Voice Caddie</h6>
                        <p class="card-text text-muted" style="font-size: 0.95rem; line-height: 1.6;">
                            Developed and optimized golf swing pose estimation models and temporal action localization algorithms for portable smart devices.
                        </p>
                        <ul class="pl-3 text-muted" style="font-size: 0.9rem; line-height: 1.6;">
                            <li>Deployed golf pose estimation models onto AI assistant golf devices.</li>
                            <li>Created action localization pipelines and dedicated annotation tools for internal dataset curation.</li>
                        </ul>
                        <div class="mt-3">
                            <span class="badge badge-light border text-secondary">Python</span>
                            <span class="badge badge-light border text-secondary">PyTorch</span>
                            <span class="badge badge-light border text-secondary">C++</span>
                            <span class="badge badge-light border text-secondary">OpenCV</span>
                        </div>
                        <div class="mt-3">
                            <a href="{{ site.baseurl }}/posts/edge-deployment/" class="btn btn-sm btn-outline-primary mr-2"><i class="fa fa-book"></i> Read Edge AI Guide</a>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-5 mt-3 mt-md-0 text-center">
                        <img class="img-fluid rounded shadow-sm border" src="{{ site.baseurl }}/assets/images/pose_estimation_cv.png" alt="Golf Pose Estimation" style="max-height: 200px; width: 100%; object-fit: cover;">
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

