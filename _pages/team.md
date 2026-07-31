---
layout: page
title: People
permalink: /team/
---

## Principal Investigator

{% assign pis = site.team | where: "role", "Principal Investigator" %}
{% for person in pis %}
### {{ person.title }}
<img src="{{ person.image | relative_url }}" alt="{{ person.title }}" style="max-width: 200px; max-height: 200px; display: block; margin-bottom: 15px;">
{{ person.content | markdownify }}
{% endfor %}

---

## Graduate Students

{% assign grads = site.team | where: "role", "Doctoral Student" %}
{% for person in grads %}
### {{ person.title }}
<img src="{{ person.image | relative_url }}" alt="{{ person.title }}" style="max-width: 200px; max-height: 200px; display: block; margin-bottom: 15px;">
{{ person.content | markdownify }}
{% endfor %}

## Undergraduate Students

We welcome students who are interested in the lab. Contact Dr. Bonny about joining!

{% assign undergrads = site.team | where: "role", "Undergraduate Student" %}
{% for person in undergrads %}
### {{ person.title }}
<img src="{{ person.image | relative_url }}" alt="{{ person.title }}" style="max-width: 200px; max-height: 200px; display: block; margin-bottom: 15px;">
{{ person.content | markdownify }}
{% endfor %}

## Past Members

{% assign past_page = site.pages | where: "permalink", "/team/past/" | first %}
{{ past_page.content | markdownify }}