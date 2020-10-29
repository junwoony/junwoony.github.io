---
layout: archive
title: "ML Course Projects"
permalink: /projects/
author_profile: true
---

begin 1
{% include base_path %}
begin 2
{% for post in site.projects reversed %}
   post 1
  {% include archive-single.html %}
{% endfor %}

end

<sup>*</sup> Co-First Authors
