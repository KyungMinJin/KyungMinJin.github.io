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
    {% for project in site.data.projects.main_projects %}
    <!-- Project {{ forloop.index }} -->
    <div class="col-md-12 mb-3">
        <div class="card shadow-sm border overflow-hidden project-card">
            <div class="card-body">
                <!-- Card Header (Full Width) -->
                <div class="d-flex justify-content-between align-items-center border-bottom pb-2 mb-3">
                    <div>
                        <span class="badge {{ project.badge_class }} mr-2">{{ project.badge_text }}</span>
                        <span class="text-secondary font-weight-normal" style="font-size: 0.85rem;"><i class="fa {{ project.org_icon }}"></i> {{ project.org_name }}</span>
                    </div>
                    <small class="text-muted font-weight-bold">{{ project.duration }}</small>
                </div>
                <!-- Card Content (Split Columns) -->
                <div class="row align-items-center">
                    <div class="col-lg-8 col-md-7">
                        <h5 class="card-title font-weight-bold text-dark mb-2">{{ project.title }}</h5>
                        <p class="card-text text-muted" style="font-size: 0.95rem; line-height: 1.6;">
                            {{ project.desc }}
                        </p>
                        {% if project.highlights %}
                        <ul class="pl-3 text-muted" style="font-size: 0.9rem; line-height: 1.6;">
                            {% for highlight in project.highlights %}
                            <li>{{ highlight }}</li>
                            {% endfor %}
                        </ul>
                        {% endif %}
                        <div class="mt-3">
                            {% for tag in project.tags %}
                            <span class="badge badge-light border text-secondary">{{ tag }}</span>
                            {% endfor %}
                        </div>
                        {% if project.links %}
                        <div class="mt-3">
                            {% for link in project.links %}
                            <a href="{% if link.external %}{{ link.url }}{% else %}{{ site.baseurl }}{{ link.url }}{% endif %}" {% if link.external %}target="_blank"{% endif %} class="btn btn-sm {{ link.class }}"><i class="fa {{ link.icon }}"></i> {{ link.text }}</a>
                            {% endfor %}
                        </div>
                        {% endif %}
                    </div>
                    {% if project.image %}
                    <div class="col-lg-4 col-md-5 mt-3 mt-md-0 text-center">
                        <img class="img-fluid rounded shadow-sm border" src="{{ site.baseurl }}{{ project.image }}" alt="{{ project.image_alt }}" style="height: 180px; width: 100%; object-fit: cover;">
                    </div>
                    {% endif %}
                </div>
            </div>
        </div>
    </div>
    {% endfor %}
</div>

<!-- Early Development Career Section -->
<hr class="my-5">
<div class="row">
    <div class="col-md-12 mb-3">
        <h5 class="font-weight-bold text-dark mb-1">
            <i class="fa fa-code text-muted"></i> Early Development Career
        </h5>
        <p class="text-muted" style="font-size:0.93rem;">
            Frontend &amp; full-stack development projects built before transitioning to AI research.
        </p>
    </div>

    {% for project in site.data.projects.early_projects %}
    <!-- {{ project.title }} -->
    <div class="col-md-6 mb-3">
        <div class="card shadow-sm border overflow-hidden project-card h-100">
            <div class="card-body">
                <div class="d-flex justify-content-between align-items-center border-bottom pb-2 mb-3">
                    <div>
                        <span class="badge {{ project.badge_class }} mr-2">{{ project.badge_text }}</span>
                        <span class="text-secondary font-weight-normal" style="font-size: 0.85rem;"><i class="fa {{ project.org_icon }}"></i> {{ project.org_name }}</span>
                    </div>
                    <small class="text-muted font-weight-bold">{{ project.duration }}</small>
                </div>
                <h6 class="card-title font-weight-bold text-dark mb-2">{{ project.title }}</h6>
                <p class="card-text text-muted" style="font-size: 0.9rem; line-height: 1.6;">
                    {{ project.desc }}
                </p>
                <div class="mt-2">
                    {% for tag in project.tags %}
                    <span class="badge badge-light border text-secondary">{{ tag }}</span>
                    {% endfor %}
                </div>
            </div>
        </div>
    </div>
    {% endfor %}
</div>

