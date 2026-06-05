---
layout: page
title: Research Notes
permalink: /notes
comments: true
---

<div class="row">
    <div class="col-md-12">
        <p class="lead">My study logs, paper reviews, and technical research notes on computer vision, reinforcement learning, and LLMs/VLMs.</p>
        <hr class="my-4">
    </div>
</div>

<div class="row listrecent">
    {% assign notes_posts = site.categories.Notes %}
    {% if notes_posts.size > 0 %}
        {% for post in notes_posts %}
            {% include postbox.html %}
        {% endfor %}
    {% else %}
        <div class="col-md-12 text-center py-5">
            <i class="fa fa-pencil-square-o fa-3x text-muted mb-3"></i>
            <p class="text-muted">No research notes posted yet. Check back soon!</p>
        </div>
    {% endif %}
</div>
