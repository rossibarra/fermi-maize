"""Render index.html to a three-page US Letter PDF.

Usage (from the repository root):
    pip install playwright && playwright install chromium
    python scripts/render_pdf.py            # writes fermi-maize-cheatsheet.pdf

The page uses the Roboto font; install it locally (e.g. `fonts-roboto` on Debian/Ubuntu,
or from Google Fonts on macOS) so the PDF matches the web version.
"""
import pathlib
import sys

from playwright.sync_api import sync_playwright

root = pathlib.Path(__file__).resolve().parent.parent
src = root / "index.html"
out = root / (sys.argv[1] if len(sys.argv) > 1 else "fermi-maize-cheatsheet.pdf")

FOOTER = (
    '<div style="font-family:Roboto,sans-serif;font-size:7.5pt;color:#555;width:100%;'
    'padding:0 12mm;display:flex;justify-content:space-between;">'
    "<span>Maize Population Genetics — Fermi Math Cheatsheet</span>"
    '<span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>'
)

with sync_playwright() as p:
    browser = p.chromium.launch()
    # viewport width = US Letter width minus 12 mm side margins, so text wraps as on paper
    page = browser.new_page(viewport={"width": 725, "height": 956})
    page.emulate_media(media="print")
    page.goto(src.as_uri())
    page.wait_for_timeout(500)
    page.evaluate("document.body.classList.add('pdf')")
    sizes = page.evaluate("window.fitAll()")
    print("page font sizes (pt):", [round(x, 2) for x in sizes])
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
