#!/usr/bin/env python3
"""
generate_publications.py

Regenerates _pages/publications.md from publications.bib.

Replaces the need for the jekyll-scholar plugin: reads your BibTeX file,
formats each entry, and writes a static HTML list into publications.md.
Each <li> gets an id="<bibtex_key>" attribute, so links elsewhere in the
site like /publications/#bonny_role_2025 keep working.

USAGE
-----
1. Install the one dependency (only needs to be done once):
     pip install bibtexparser --break-system-packages
   (drop --break-system-packages if you're using a venv/rbenv-style setup
   where that flag isn't needed)

2. Update publications.bib with your new/changed entries (e.g. export a
   fresh .bib from Zotero/EndNote/etc. and overwrite the file).

3. Run this script from the same folder as publications.bib:
     python3 generate_publications.py

   By default it looks for publications.bib in the current directory and
   writes publications.md in the current directory. Override with flags:
     python3 generate_publications.py --bib path/to/publications.bib --out _pages/publications.md

4. Review the diff, then copy/move publications.md into _pages/ and commit.

WHAT IT DOES
------------
- Sorts entries by year, newest first.
- Formats authors as "Last, F. M." with "&" before the final author.
- Builds a citation line: Author(s) (Year). Title. *Journal*, *Vol*(Issue), pages.
- Links out to the DOI (as https://doi.org/<doi>) if present, otherwise the
  bib entry's `url` field if present.
- Skips the journal/volume/page block entirely for entry types where those
  fields are missing (e.g. some conference proceedings), so you never get
  a stray ", ," in the output.
"""

import argparse
import sys

try:
    import bibtexparser
    from bibtexparser.bparser import BibTexParser
    from bibtexparser.customization import convert_to_unicode
except ImportError:
    sys.exit(
        "Missing dependency 'bibtexparser'.\n"
        "Install it with:\n"
        "  pip install bibtexparser --break-system-packages\n"
        "(omit --break-system-packages if not needed on your system)"
    )


PAGE_HEADER = """---
layout: page
title: Publications
permalink: /publications/
---

<style>
  ol.bibliography {{ list-style-type: none; padding-left: 2em; margin-left: 0; counter-reset: pub-counter; }}
  ol.bibliography li {{ text-indent: -2em; margin-bottom: 1.2em; line-height: 1.5; }}
</style>

## Journal Articles and Refereed Conference Proceedings

<ol class="bibliography">
{items}
</ol>
"""


def load_entries(bib_path):
    with open(bib_path, encoding="utf-8") as f:
        parser = BibTexParser(common_strings=True)
        parser.customization = convert_to_unicode
        db = bibtexparser.load(f, parser=parser)
    return db.entries


def sort_key(entry):
    try:
        return int(entry.get("year", 0))
    except ValueError:
        return 0


def clean(s):
    if not s:
        return ""
    return s.replace("{", "").replace("}", "").strip()


def fix_initials(name):
    """Ensure single-letter initials always end with a period: 'W' -> 'W.'"""
    parts = name.split()
    fixed = []
    for p in parts:
        if len(p) == 1 and p.isupper():
            fixed.append(p + ".")
        else:
            fixed.append(p)
    return " ".join(fixed)


def format_authors(author_str):
    if not author_str:
        return ""
    authors = [a.strip() for a in author_str.split(" and ")]
    formatted = []
    for a in authors:
        if "," in a:
            last, first = a.split(",", 1)
            formatted.append(f"{last.strip()}, {fix_initials(first.strip())}")
        else:
            formatted.append(a)
    if len(formatted) == 1:
        return formatted[0]
    elif len(formatted) == 2:
        return f"{formatted[0]} &amp; {formatted[1]}"
    else:
        return ", ".join(formatted[:-1]) + f", &amp; {formatted[-1]}"


def format_entry(entry):
    cite_key = entry.get("ID", "")
    authors = format_authors(entry.get("author", ""))
    year = clean(entry.get("year", "n.d."))
    title = clean(entry.get("title", "")).rstrip(".")
    journal = clean(
        entry.get("journal", entry.get("booktitle", entry.get("chapter", "")))
    )
    volume = clean(entry.get("volume", ""))
    number = clean(entry.get("number", ""))
    pages = clean(entry.get("pages", "")).replace("--", "\u2013")
    doi = clean(entry.get("doi", ""))
    url = clean(entry.get("url", ""))

    text = f"{authors} ({year}). {title}."

    if journal:
        journal_part = f" <em>{journal}</em>"
        if volume:
            journal_part += f", <em>{volume}</em>"
            if number:
                journal_part += f"({number})"
        if pages:
            journal_part += f", {pages}"
        journal_part += "."
        text += journal_part

    link = f"https://doi.org/{doi}" if doi else url
    if link:
        text += f' <a href="{link}" target="_blank" rel="noopener noreferrer">{link}</a>'

    return f'  <li id="{cite_key}">{text}</li>'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--bib", default="publications.bib", help="Path to input .bib file"
    )
    parser.add_argument(
        "--out", default="publications.md", help="Path to output .md file"
    )
    args = parser.parse_args()

    entries = load_entries(args.bib)
    if not entries:
        sys.exit(f"No entries found in {args.bib}")

    entries.sort(key=sort_key, reverse=True)

    li_items = [format_entry(e) for e in entries]

    page = PAGE_HEADER.format(items="\n".join(li_items))

    with open(args.out, "w", encoding="utf-8") as f:
        f.write(page)

    print(f"Wrote {len(li_items)} entries from {args.bib} to {args.out}")


if __name__ == "__main__":
    main()