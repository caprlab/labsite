---
layout: page
title: People
permalink: /team/
---

<style>
  /* The Grid Container */
  .team-grid {
    display: grid;
    /* This creates responsive columns that are at least 250px wide */
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 20px;
    margin-bottom: 40px;
  }

  /* Individual Team Tiles */
  .team-tile {
    border: 1px solid #e1e4e8;
    border-radius: 8px;
    padding: 20px;
    text-align: center;
    background-color: #fafbfc;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
  }

  /* Tile Images */
  .team-tile img {
    max-width: 150px;
    height: 150px;
    object-fit: cover;
    border-radius: 50%; /* Makes the image a perfect circle */
    margin: 0 auto 15px auto;
    display: block;
  }

  /* Tile Typography */
  .team-tile h3 {
    margin-top: 0;
    margin-bottom: 10px;
    font-size: 1.25em;
  }
  
  .team-tile p {
    font-size: 0.9em;
    margin-bottom: 5px;
    line-height: 1.4;
  }
</style>

## Principal Investigator

{% assign pis = site.team | where: "role", "Principal Investigator" %}
{% for person in pis %}
### {{ person.title }}
<img src="{{ person.image | relative_url }}" alt="{{ person.title }}" style="max-width: 200px; max-height: 200px; display: block; margin-bottom: 15px;">
{{ person.content | markdownify }}
{% endfor %}

---

## Graduate Students

<div class="team-grid">
  {% assign grads = site.team | where: "role", "Doctoral Student" %}
  {% for person in grads %}
    <div class="team-tile">
      <img src="{{ person.image | relative_url }}" alt="{{ person.title }}">
      <h3>{{ person.title }}</h3>
      {{ person.content | markdownify }}
    </div>
  {% endfor %}
</div>

---

## Undergraduate Students

We welcome students who are interested in the lab. Contact Dr. Bonny about joining!

<br>

<div class="team-grid">
  {% assign undergrads = site.team | where: "role", "Undergraduate Student" %}
  {% for person in undergrads %}
    <div class="team-tile">
      <img src="{{ person.image | relative_url }}" alt="{{ person.title }}">
      <h3>{{ person.title }}</h3>
      {{ person.content | markdownify }}
    </div>
  {% endfor %}
</div>

---

## Past Members

{% assign past_page = site.pages | where: "permalink", "/team/past/" | first %}
{{ past_page.content | markdownify }}