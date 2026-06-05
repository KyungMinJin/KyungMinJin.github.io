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
    <div class="col-md-6 mb-4">
        <div class="card h-100 shadow-sm border">
            <div class="card-body">
                <div class="d-flex justify-content-between align-items-center mb-2">
                    <span class="badge badge-primary">Robotics / Embodied AI</span>
                    <small class="text-muted">2026.01 - Present</small>
                </div>
                <h5 class="card-title font-weight-bold">Natural Language-Based Object Understanding for Robots</h5>
                <h6 class="card-subtitle mb-3 text-secondary">LG Electronics, Advanced Robotics Lab</h6>
                <p class="card-text text-muted" style="font-size: 0.95rem;">
                    Building robot perception systems that ground natural language in visual environments to enable intuitive human-robot interaction.
                </p>
                <ul class="pl-3 text-muted" style="font-size: 0.9rem;">
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
            </div>
        </div>
    </div>

    <!-- Project 2 -->
    <div class="col-md-6 mb-4">
        <div class="card h-100 shadow-sm border">
            <div class="card-body">
                <div class="d-flex justify-content-between align-items-center mb-2">
                    <span class="badge badge-success">Multimodal Learning</span>
                    <small class="text-muted">2023.07 - 2025.12</small>
                </div>
                <h5 class="card-title font-weight-bold">SAMIF: Semantic-Aware Mutual Information Factorized Learning</h5>
                <h6 class="card-subtitle mb-3 text-secondary">LG Electronics, AI Lab</h6>
                <p class="card-text text-muted" style="font-size: 0.95rem;">
                    Researched cross-modality shared and unique information factorization strategies to improve semantic segmentation across aligned data modalities.
                </p>
                <ul class="pl-3 text-muted" style="font-size: 0.9rem;">
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
            </div>
        </div>
    </div>

    <!-- Project 3 -->
    <div class="col-md-6 mb-4">
        <div class="card h-100 shadow-sm border">
            <div class="card-body">
                <div class="d-flex justify-content-between align-items-center mb-2">
                    <span class="badge badge-danger">LLM / VLM</span>
                    <small class="text-muted">LG Electronics</small>
                </div>
                <h5 class="card-title font-weight-bold">Small Multimodal LLM & Audio Tower Training</h5>
                <h6 class="card-subtitle mb-3 text-secondary">LG Electronics, AI Lab</h6>
                <p class="card-text text-muted" style="font-size: 0.95rem;">
                    Developed small-scale multimodal language models featuring audio/vision towers and optimized using advanced policy training.
                </p>
                <ul class="pl-3 text-muted" style="font-size: 0.9rem;">
                    <li>Designed an audio tower and LLM cross-modal continual learning pipeline.</li>
                    <li>Achieved a 20.7% improvement by training GRPO on synthetic data with Self-Reflection and Unification.</li>
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
            </div>
        </div>
    </div>

    <!-- Project 4 -->
    <div class="col-md-6 mb-4">
        <div class="card h-100 shadow-sm border">
            <div class="card-body">
                <div class="d-flex justify-content-between align-items-center mb-2">
                    <span class="badge badge-info">Reinforcement Learning</span>
                    <small class="text-muted">Joint Research</small>
                </div>
                <h5 class="card-title font-weight-bold">Fast-Reasoning Modality-Aware Policy Optimization</h5>
                <h6 class="card-subtitle mb-3 text-secondary">LG Electronics & Toronto AI Lab</h6>
                <p class="card-text text-muted" style="font-size: 0.95rem;">
                    Collaborated on online policy optimization methods that apply modality-aware weighting in Group Relative Policy Optimization (GRPO).
                </p>
                <ul class="pl-3 text-muted" style="font-size: 0.9rem;">
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
            </div>
        </div>
    </div>

    <!-- Project 5 -->
    <div class="col-md-6 mb-4">
        <div class="card h-100 shadow-sm border">
            <div class="card-body">
                <div class="d-flex justify-content-between align-items-center mb-2">
                    <span class="badge badge-warning">Computer Vision</span>
                    <small class="text-muted">Research & Deployed</small>
                </div>
                <h5 class="card-title font-weight-bold">Optimized Body & Hand Pose Estimation</h5>
                <h6 class="card-subtitle mb-3 text-secondary">Korea University & LG Electronics</h6>
                <p class="card-text text-muted" style="font-size: 0.95rem;">
                    Developed state-of-the-art pose estimation algorithms and optimized them for edge-device integration.
                </p>
                <ul class="pl-3 text-muted" style="font-size: 0.9rem;">
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
            </div>
        </div>
    </div>

    <!-- Project 6 -->
    <div class="col-md-6 mb-4">
        <div class="card h-100 shadow-sm border">
            <div class="card-body">
                <div class="d-flex justify-content-between align-items-center mb-2">
                    <span class="badge badge-secondary">Embedded AI</span>
                    <small class="text-muted">2020.05 - 2020.11</small>
                </div>
                <h5 class="card-title font-weight-bold">Golf Pose Estimation & Action Localization</h5>
                <h6 class="card-subtitle mb-3 text-secondary">Voice Caddie</h6>
                <p class="card-text text-muted" style="font-size: 0.95rem;">
                    Developed and optimized golf swing pose estimation models and temporal action localization algorithms for portable smart devices.
                </p>
                <ul class="pl-3 text-muted" style="font-size: 0.9rem;">
                    <li>Deployed golf pose estimation models onto AI assistant golf devices.</li>
                    <li>Created action localization pipelines and dedicated annotation tools for internal dataset curation.</li>
                </ul>
                <div class="mt-3">
                    <span class="badge badge-light border text-secondary">Python</span>
                    <span class="badge badge-light border text-secondary">PyTorch</span>
                    <span class="badge badge-light border text-secondary">C++</span>
                    <span class="badge badge-light border text-secondary">OpenCV</span>
                </div>
            </div>
        </div>
    </div>
</div>
