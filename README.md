# Maize Population Genetics — Fermi Math Cheatsheet

Rules of thumb for maize genomes and population genetics: a "top 10" table of constants, genomic length scales, genome composition and selection, an evolutionary timeline, and worked back-of-the-envelope (Fermi) problems. Every number carries a reference, and values we derived or computed ourselves are explained in the notes.

- **Read it online:** https://rossibarra.github.io/fermi-maize/
- **Download the PDF:** https://rossibarra.github.io/fermi-maize/fermi-maize-cheatsheet.pdf (3 pages, US Letter)

## Contributing

Everything is generated from two plain-text files, so corrections and additions are ordinary pull requests:

| File | What to edit there |
|---|---|
| [`content.md`](content.md) | All the text, numbers and worked examples ([pandoc markdown](https://pandoc.org/MANUAL.html#pandocs-markdown)). |
| [`references.bib`](references.bib) | The sources, as BibTeX entries. |

The quickest route is GitHub's web editor: open `content.md`, click the pencil icon, make your change, and propose it as a pull request. GitHub Actions builds the web page and PDF for every pull request; download them from the **fermi-maize-preview** artifact on the PR's *Checks* tab to see how your change looks.

A few conventions:

- **Superscript, subscript, italics:** `10^9^`, `N~e~`, `*π*`.
- **Citations:** put `[@key]` right after the text it supports, with no space (`39,756 genes[@b73v5]`); several sources are `[@key1; @key2]`. The key is the first field of the entry in `references.bib`. Numbering and the reference list are generated automatically, so never number references by hand.
- **New sources:** add a BibTeX entry to `references.bib` with a DOI where one exists.
- **Math** in the worked examples is LaTeX between `$…$`.
- **Pages:** the three `::: {#p1 .page}` blocks are the three PDF pages. The PDF build scales each page's font so the page is full, so a long addition makes that page's text smaller. The build prints the font sizes and warns if page 1 drops below 7.5 pt.
- **Derived values:** if a number is your own calculation rather than a reported value, explain it in the notes section.

Please open an [issue](https://github.com/rossibarra/fermi-maize/issues) for anything you'd like discussed before editing.

## Building locally

```bash
# pandoc 3.x: https://pandoc.org/installing.html (e.g. `brew install pandoc`)
pip install playwright
playwright install chromium
python scripts/build.py           # writes _site/index.html and _site/fermi-maize-cheatsheet.pdf
python scripts/build.py --no-pdf  # HTML only
```

Install the Roboto font so the local PDF matches the published one.

## How it's built

| File | Role |
|---|---|
| `template.html` | Page layout and styles (pandoc template). |
| `nature-compact.csl` | Citation style: *Nature* style, shortened to "First author *et al.*" for three or more authors. |
| `scripts/build.py` | Runs pandoc (with citeproc and MathML) to make `_site/index.html`, then prints it to PDF with headless Chromium. |
| `.github/workflows/build.yml` | Builds on every push and pull request; deploys `main` to GitHub Pages. |

## Citation

Ross-Ibarra J and contributors (2026). *Maize Population Genetics — Fermi Math Cheatsheet.* https://github.com/rossibarra/fermi-maize

## License

Content (`content.md`, `references.bib` and the generated page and PDF) is licensed [CC BY 4.0](LICENSE). Code (`scripts/`, `template.html`, the workflow) is licensed [MIT](scripts/LICENSE). `nature-compact.csl` is adapted from the Citation Style Language project's *Nature* style and keeps its CC BY-SA 3.0 license.
