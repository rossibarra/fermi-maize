# Maize Population Genetics — Fermi Math Cheatsheet

Rules of thumb for maize genomes and population genetics: a "top 10" table of constants, genomic length scales, genome composition and selection, an evolutionary timeline, and worked back-of-the-envelope (Fermi) problems. Every number carries a reference; values we derived or computed ourselves are explained in the notes.

- **Read it online:** https://rossibarra.github.io/fermi-maize/
- **Download the PDF:** [fermi-maize-cheatsheet.pdf](fermi-maize-cheatsheet.pdf) (3 pages, US Letter)

## Contents

| File | What it is |
|---|---|
| `index.html` | The single source. Renders as a web page, and as the PDF when `scripts/render_pdf.py` adds the `pdf` class to `<body>`. |
| `fermi-maize-cheatsheet.pdf` | The PDF built from `index.html`. |
| `scripts/render_pdf.py` | Rebuilds the PDF with headless Chromium (Playwright). Each page's font size is scaled so the content fills it. |

## Editing

Edit `index.html`, then rebuild the PDF:

```bash
pip install playwright
playwright install chromium
python scripts/render_pdf.py
```

The page uses the Roboto font. Install it locally so the PDF matches the web version; the web page loads it from Google Fonts. Citations are hard-coded superscripts (`<sup class="c">n</sup>`) that point into the numbered reference list at the end of the notes, so keep the two in step when adding or removing references.

## Citation

Ross-Ibarra J (2026). *Maize Population Genetics — Fermi Math Cheatsheet.* https://github.com/rossibarra/fermi-maize

Corrections and suggestions are welcome as [issues](https://github.com/rossibarra/fermi-maize/issues) or pull requests.

## License

Content (`index.html`, the PDF) is licensed [CC BY 4.0](LICENSE). The script in `scripts/` is licensed [MIT](scripts/LICENSE).
