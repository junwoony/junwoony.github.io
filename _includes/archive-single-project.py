{% include base_path %}

{% if post.header.teaser %}
  {% capture teaser %}{{ post.header.teaser }}{% endcapture %}
{% else %}
  {% assign teaser = site.teaser %}
{% endif %}

{% if post.id %}
  {% assign title = post.title | markdownify | remove: "<p>" | remove: "</p>" %}
{% else %}
  {% assign title = post.title %}
{% endif %}

<div class="{{ include.type | default: "list" }}__item">
  <article class="archive__item" itemscope itemtype="http://schema.org/CreativeWork">
    {% if include.type == "grid" and teaser %}
      <div class="archive__item-teaser">
        <img src=
          {% if teaser contains "://" %}
            "{{ teaser }}"
          {% else %}
            "{{ teaser | prepend: "/images/" | prepend: base_path }}"
          {% endif %}
          alt="">
      </div>
    {% endif %}

    <h2 class="archive__item-title" itemprop="headline">
      {% if post.collection == 'publications' %}
        {{ title }}
      {% elsif post.link %}
        <a href="{{ post.link }}">{{ title }}</a> <a href="{{ base_path }}{{ post.url }}" rel="permalink"><i class="fa fa-link" aria-hidden="true" title="permalink"></i><span class="sr-only">Permalink</span></a>
      {% else %}
        <a href="{{ base_path }}{{ post.url }}" rel="permalink">{{ title }}</a>
      {% endif %}
    </h2>
    
    {% if post.read_time %}
      <p class="page__meta"><i class="fa fa-clock-o" aria-hidden="true"></i> {% include read-time.html %}</p>
    {% endif %}

    {% if post.collection == 'teaching' %}
      <p> {{ post.type }}, <i>{{ post.venue }}</i>, {{ post.date | default: "1900-01-01" | date: "%Y" }} </p>
    {% elsif post.collection == 'publications' %}
      {% if post.abstract %}
        <details><summary>Abstract</summary>
        <blockquote>
        <p>
        {{ post.abstract }}
        </p>
        </blockquote>
        </details>
      {% endif %}
      
      <!-- citation and icon code -->
      <p>
      {% if post.journal %}
        <p style="color:brown; font-size: 20px;">{{post.journal}}</p>
      {% endif %}
      {% if post.citation %}
        {{ post.citation }}
      {% endif %}
      <br>
      {% if post.link %}
        <a href="{{ post.link }}" target="_blank" rel="noopener noreferrer">{{post.project}}</a>
      {% endif %}
      {% if post.paperurl %}
        <a href="{{ post.paperurl}}" target="_blank" rel="noopener noreferrer"><i class="fas fa-fw fa-file-pdf zoom" aria-hidden="true"></i></a>
      {% endif %}
      {% if post.github %}
        <a href="{{ post.github }}" target="_blank" rel="noopener noreferrer"><i class="fab fa-fw fa-github zoom" aria-hidden="true"></i></a>
      {% endif %}
      {% if post.image %}
        <br>
        <img src="{{post.image}}">
      {% endif %}
      {% if post.gif %}
        <br>
        <img src="{{post.gif}}">
      {% endif %}
      </p>
    {% elsif post.collection == 'posts' and post.date %}
      <p class="page__date"><strong><i class="fa fa-fw fa-calendar" aria-hidden="true"></i> {{ site.data.ui-text[site.locale].date_label | default: "Published:" }}</strong> <time$
    {% endif %}


    {% if post.excerpt and site.read_more != 'enabled' %}
    <p class="archive__item-excerpt" itemprop="description">{{ post.excerpt | markdownify }}</p>
    {% elsif post.excerpt and site.read_more == 'enabled' %}
    <p class="archive__item-excerpt" itemprop="description"><p>{{ post.excerpt | markdownify | remove: '<p>' | remove: '</p>' }}<strong><a href="{{ base_path }}{{ post.url }}" rel="permalink"> Read more</a></strong></p></p>
    {% endif %}
    
  </article>
</div>
