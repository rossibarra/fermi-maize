"""Build the site from content.md.

    python scripts/build.py            # writes _site/index.html and _site/fermi-maize-cheatsheet.pdf
    python scripts/build.py --no-pdf   # HTML only (no Playwright needed)

Needs pandoc (3.x) on the PATH; the PDF also needs `pip install playwright` and
`playwright install chromium`, plus the Roboto font so the PDF matches the web page.
"""
import datetime
import pathlib
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "_site"
PDF_NAME = "fermi-maize-cheatsheet.pdf"

FOOTER = (
    '<div style="font-family:Roboto,sans-serif;font-size:7.5pt;color:#555;width:100%;'
    'padding:0 12mm;display:flex;justify-content:space-between;">'
    "<span>Maize Population Genetics — Fermi Math Cheatsheet</span>"
    '<span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>'
)


def build_html():
    SITE.mkdir(exist_ok=True)
    (SITE / ".nojekyll").touch()
    out = SITE / "index.html"
    subprocess.run(
        [
            "pandoc", "content.md",
            "--from", "markdown",
            "--to", "html5",
            "--standalone",
            "--template", "template.html",
            "--citeproc",
            "--mathml",
            "--columns", "10000",  # keep pipe-table widths under CSS control
            "--metadata", f"build_date={datetime.date.today().isoformat()}",
            "--output", str(out),
        ],
        cwd=ROOT,
        check=True,
    )
    print("wrote", out)
    return out


def build_pdf(html):
    from playwright.sync_api import sync_playwright

    out = SITE / PDF_NAME
    with sync_playwright() as p:
        browser = p.chromium.launch()
        # viewport = US Letter width minus 12 mm side margins, so text wraps as on paper
        page = browser.new_page(viewport={"width": 725, "height": 956})
        page.emulate_media(media="print")
        page.goto(html.as_uri())
        page.wait_for_timeout(500)
        page.evaluate("document.body.classList.add('pdf')")
        sizes = page.evaluate("window.fitAll()")
        print("PDF page font sizes (pt):", [round(x, 2) for x in sizes])
        if sizes[0] < 7.5:
            print("warning: page 1 is getting crowded (font below 7.5 pt)")
        page.pdf(
            path=str(out),
            format="Letter",
            print_background=True,
            prefer_css_page_size=True,
            display_header_footer=True,
            header_template="<div></div>",
            footer_template=FOOTER,
        )
        browser.close()
    print("wrote", out)


if __name__ == "__main__":
    html = build_html()
    if "--no-pdf" not in sys.argv:
        build_pdf(html)
