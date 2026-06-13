---
layout: page
title: Publications
permalink: /publications
comments: true
---

<div class="row">
    <div class="col-md-12">
        <p class="lead">List of peer-reviewed journal articles, conference papers, and preprints. Key publications are marked with relevant badges.</p>
        <hr class="my-4">

        {% for pub in site.data.publications %}
        <!-- Publication {{ forloop.index }} -->
        <div class="publication-item mb-4 pb-3 border-bottom">
            <span class="badge {{ pub.badge_class }} mb-2">{{ pub.badge_text }}</span>
            <span class="badge {{ pub.category_class }} mb-2">{{ pub.category_text }}</span>
            <h5 class="font-weight-bold text-dark">{{ pub.title }}</h5>
            <p class="authors mb-1 text-muted">
                {{ pub.authors }}
            </p>
            <p class="venue mb-2">
                {{ pub.venue }}
            </p>
            {% if pub.links or pub.bibtex %}
            <div class="links mb-3">
                {% for link in pub.links %}
                <a class="btn btn-sm {{ link.class | default: 'btn-outline-primary mr-2' }}" href="{{ link.url }}" {% if link.external %}target="_blank"{% endif %}><i class="fa {{ link.icon }}"></i> {{ link.text }}</a>
                {% endfor %}
                {% if pub.bibtex %}
                <details class="d-inline">
                    <summary class="btn btn-sm btn-outline-secondary"><i class="fa fa-code"></i> BibTeX</summary>
                    <pre class="bg-light p-3 mt-2 rounded"><code>{{ pub.bibtex }}</code></pre>
                </details>
                {% endif %}
            </div>
            {% endif %}
            
            {% if pub.demo_img %}
            <!-- Visual Demo -->
            <div class="publication-demo mb-3">
                <img src="{% if pub.demo_img contains '://' %}{{ pub.demo_img }}{% else %}{{ site.baseurl }}{{ pub.demo_img }}{% endif %}" class="img-fluid rounded publication-demo-img shadow-sm" alt="{{ pub.demo_alt }}" style="cursor: zoom-in;">
            </div>
            {% elsif pub.demo_gifs %}
            <!-- Visual Demo -->
            <div class="row publication-demo mb-3">
                {% for gif in pub.demo_gifs %}
                <div class="col-md-6 mb-2">
                    <img src="{{ site.baseurl }}{{ gif.url }}" class="img-fluid rounded publication-demo-img shadow-sm" alt="{{ gif.alt }}" style="cursor: zoom-in;">
                </div>
                {% endfor %}
            </div>
            {% endif %}
        </div>
        {% endfor %}

    </div>
</div>

<style>
.publication-demo {
    width: 100%;
    overflow: hidden;
}
.publication-demo-img {
    width: 100%;
    max-width: 100%;
    height: 220px;
    object-fit: contain;
}
.publication-item details pre {
  position: relative;
  padding-right: 80px !important;
}
.copy-bibtex-btn {
  position: absolute;
  top: 8px;
  right: 8px;
  padding: 3px 8px;
  font-size: 0.75rem;
  color: #666;
  background: #fff;
  border: 1px solid #ddd;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.2s ease;
  z-index: 10;
}
.copy-bibtex-btn:hover {
  background: #00ab6b;
  color: #fff;
  border-color: #00ab6b;
}
.copy-bibtex-btn.copied {
  background: #28a745;
  color: #fff;
  border-color: #28a745;
}
</style>

<script>
document.addEventListener("DOMContentLoaded", function() {
  const preBlocks = document.querySelectorAll(".publication-item details pre");
  preBlocks.forEach((pre) => {
    // Create copy button
    const button = document.createElement("button");
    button.className = "copy-bibtex-btn";
    button.innerHTML = "<i class='fa fa-clipboard'></i> Copy";
    
    // Add click event
    button.addEventListener("click", function(e) {
      e.preventDefault();
      e.stopPropagation();
      
      const code = pre.querySelector("code");
      const text = code ? code.innerText : pre.innerText;
      
      // Filter out copy button text itself if it gets included
      const cleanText = text.replace("Copy", "").trim();
      
      navigator.clipboard.writeText(cleanText).then(() => {
        button.innerHTML = "<i class='fa fa-check'></i> Copied!";
        button.classList.add("copied");
        setTimeout(() => {
          button.innerHTML = "<i class='fa fa-clipboard'></i> Copy";
          button.classList.remove("copied");
        }, 2000);
      }).catch(err => {
        console.error("Failed to copy text: ", err);
      });
    });
    
    pre.appendChild(button);
  });
});
</script>
