---
layout: archive
title: "ML Projects"
permalink: /publications/
author_profile: true
---

{% include base_path %}

{% for post in site.projects reversed %}
  {% include archive-single-project.html %}
{% endfor %}
