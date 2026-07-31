---
layout: page
title: Publications
permalink: /publications/
---

<style>
  ol.bibliography { list-style-type: none; padding-left: 2em; margin-left: 0; }
  ol.bibliography li { text-indent: -2em; margin-bottom: 1.2em; line-height: 1.5; }
</style>

## Journal Articles and Refereed Conference Proceedings

{% bibliography --file publications %}

<script>
  document.addEventListener("DOMContentLoaded", function() {
    var bib = document.querySelector('.bibliography');
    if (bib) {
      bib.innerHTML = bib.innerHTML.replace(
        /(https?:\/\/[^\s<]+)/g, 
        '<a href="$1" target="_blank" rel="noopener noreferrer">$1</a>'
      );
    }
  });
</script>