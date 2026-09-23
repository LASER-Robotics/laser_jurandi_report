#!/usr/bin/env python3
"""Gera o PDF completo e organizado do relatório do Projeto Jurandi.

Fluxo:
1. Usa a documentação HTML já compilada pelo Sphinx (``build/html``).
2. Imprime cada página do relatório em PDF com o Chromium (Playwright),
   removendo a navegação do tema e aplicando ``source/_static/print.css``.
3. Monta capa e sumário com numeração real de páginas.
4. Junta tudo e aplica o rodapé numerado.

Uso:
    python tools/build_pdf.py --html build/html \
        --output build/html/_static/relatorio-jurandi.pdf
"""

from __future__ import annotations

import argparse
import asyncio
import datetime as dt
import html as html_mod
import json
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"

TITLE = "Projeto Jurandi — Relatório Técnico"
SUBTITLE = (
    "Desenvolvimento, integração e validação de um Veículo de Superfície "
    "Autônomo (ASV) em formato de catamarã."
)
AUTHOR = "Vitor Manuel Soares Araújo"
REGISTRATION = "20230046536"
INSTITUTION = "UFPB · Universidade Federal da Paraíba"
LAB = "LASER — Laboratory of Systems Engineering and Robotics"
SITE_URL = "https://laser-robotics.github.io/laser_jurandi_report/"
REPO_URL = "https://github.com/LASER-Robotics/laser_jurandi_report"

MONTHS_PT = [
    "janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro",
]

# JS executado em cada página antes da impressão: isola o conteúdo,
# remove a moldura do tema e devolve os títulos para o sumário.
PREPARE_JS = r"""
() => {
  const content = document.querySelector('.rst-content') || document.body;
  const article = content.cloneNode(true);
  document.body.innerHTML = '';
  document.body.className = 'pdf-print-body';

  const main = document.createElement('main');
  main.className = 'pdf-body rst-content';
  main.appendChild(article);
  document.body.appendChild(main);

  main.querySelectorAll(
    '.headerlink, .wy-breadcrumbs, .wy-breadcrumbs-aside, .rst-footer-buttons,' +
    ' [role="navigation"], .rst-versions, footer hr, .sphinx-tabs-hidden'
  ).forEach((el) => el.remove());

  main.querySelectorAll('.video-frame').forEach((frame) => {
    const iframe = frame.querySelector('iframe');
    const note = document.createElement('p');
    note.className = 'pdf-link-note';
    note.textContent = iframe && iframe.src
      ? 'Vídeo disponível na versão online do relatório: ' + iframe.src
      : 'Vídeo disponível na versão online do relatório.';
    frame.replaceWith(note);
  });

  // Links internos viram texto simples com o destino explícito no papel.
  main.querySelectorAll('a[href^="http"]').forEach((a) => {
    const href = a.getAttribute('href');
    if (href && a.textContent && !a.textContent.includes('http') && !a.querySelector('img')) {
      a.setAttribute('data-print-href', href);
    }
  });

  const headings = [];
  main.querySelectorAll('h1, h2').forEach((h) => {
    const text = (h.textContent || '').replace('\uf0c1', '').trim();
    if (text) headings.push({ level: h.tagName === 'H1' ? 1 : 2, text });
  });
  return headings;
}
"""


def cover_html(date_str: str) -> str:
    rows = [
        ("Autor", AUTHOR),
        ("Matrícula", REGISTRATION),
        ("Instituição", INSTITUTION),
        ("Laboratório", LAB),
        ("Versão online", SITE_URL),
        ("Repositório", REPO_URL),
        ("Emissão", date_str),
    ]
    meta = "".join(
        f"<tr><td>{html_mod.escape(k)}</td><td>{html_mod.escape(v)}</td></tr>"
        for k, v in rows
    )
    return f"""
    <div class="pdf-cover">
      <div class="pdf-cover__top">
        <span class="pdf-cover__kicker">Relatório Técnico · ASV 001</span>
        <h1 class="pdf-cover__title">{html_mod.escape(TITLE)}</h1>
        <p class="pdf-cover__subtitle">{html_mod.escape(SUBTITLE)}</p>
        <img class="pdf-cover__image" src="_images/jurandi.jpg" alt="Catamarã autônomo Jurandi" />
      </div>
      <table class="pdf-meta">{meta}</table>
    </div>
    """


def toc_html(entries: list[dict]) -> str:
    items = []
    for entry in entries:
        top = entry["level"] == 1
        cls = "level-1" if top else "level-2"
        label = html_mod.escape(entry["text"])
        # Só os capítulos recebem número de página (a paginação é por documento).
        page = f'<span class="pdf-toc__page">{entry["page"]}</span>' if top else ""
        items.append(
            f'<li class="{cls}"><span class="pdf-toc__text">{label}</span>{page}</li>'
        )
    return (
        '<nav class="pdf-toc"><h2>Sumário</h2><ol>' + "".join(items) + "</ol></nav>"
    )


def doc_order(html_dir: Path) -> list[Path]:
    """Ordem de leitura: index seguido dos documentos do toctree."""
    index = html_dir / "index.html"
    raw = index.read_text(encoding="utf-8")
    menu = re.search(
        r'<div class="wy-menu wy-menu-vertical".*?</div>', raw, re.S
    )
    names: list[str] = []
    if menu:
        for href in re.findall(r'href="([^"#]+\.html)"', menu.group(0)):
            if href not in names:
                names.append(href)
    pages = [index]
    for name in names:
        candidate = html_dir / name
        if candidate.exists() and candidate != index:
            pages.append(candidate)
    return pages


async def print_pages(pages: list[Path], css: str, workdir: Path):
    """Imprime cada documento em um PDF e coleta seus títulos."""
    from playwright.async_api import async_playwright
    from pypdf import PdfReader

    results = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1280, "height": 1600})
        page = await context.new_page()
        for i, doc in enumerate(pages):
            await page.goto(doc.as_uri(), wait_until="networkidle")
            headings = await page.evaluate(PREPARE_JS)
            await page.add_style_tag(content=css)
            await page.wait_for_timeout(300)
            out = workdir / f"doc-{i:02d}.pdf"
            await page.pdf(
                path=str(out),
                format="A4",
                print_background=True,
                margin={"top": "16mm", "bottom": "18mm", "left": "16mm", "right": "16mm"},
            )
            results.append(
                {"pdf": out, "headings": headings, "pages": len(PdfReader(out).pages)}
            )
        await browser.close()
    return results


async def print_html_fragment(
    body_html: str, css: str, base_dir: Path, out: Path
) -> int:
    """Imprime um trecho de HTML (capa ou sumário) usando o mesmo estilo."""
    from playwright.async_api import async_playwright
    from pypdf import PdfReader

    page_html = (
        '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700'
        '&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">'
        f"<style>{css}</style></head><body class=\"pdf-print-body\">{body_html}</body></html>"
    )
    tmp = base_dir / f"__pdf_tmp_{out.stem}.html"
    tmp.write_text(page_html, encoding="utf-8")
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page(viewport={"width": 1280, "height": 1600})
            await page.goto(tmp.as_uri(), wait_until="networkidle")
            await page.wait_for_timeout(300)
            await page.pdf(
                path=str(out),
                format="A4",
                print_background=True,
                margin={"top": "16mm", "bottom": "18mm", "left": "16mm", "right": "16mm"},
            )
            await browser.close()
    finally:
        tmp.unlink(missing_ok=True)
    return len(PdfReader(out).pages)


def stamp_footers(merged: Path, output: Path, skip_first: int = 1) -> None:
    """Aplica rodapé com título, autor e numeração no PDF final."""
    from io import BytesIO
    from pypdf import PdfReader, PdfWriter
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    import subprocess

    font_name = "Helvetica"
    try:
        path = subprocess.check_output(
            ["fc-match", "-f", "%{file}", "DejaVu Sans"], text=True
        ).strip()
        if path:
            pdfmetrics.registerFont(TTFont("PdfFooter", path))
            font_name = "PdfFooter"
    except Exception:  # pragma: no cover - fallback silencioso
        pass

    reader = PdfReader(merged)
    writer = PdfWriter()
    total = len(reader.pages)
    width, height = A4

    for i, page in enumerate(reader.pages):
        if i >= skip_first:
            from reportlab.pdfgen import canvas as rl_canvas

            buf = BytesIO()
            c = rl_canvas.Canvas(buf, pagesize=A4)
            c.setFont(font_name, 7.5)
            c.setFillColorRGB(0.39, 0.45, 0.55)
            c.drawString(45, 30, f"{TITLE} · {AUTHOR} · Matrícula {REGISTRATION}")
            c.drawRightString(width - 45, 30, f"{i + 1} / {total}")
            c.setStrokeColorRGB(0.86, 0.89, 0.93)
            c.line(45, 42, width - 45, 42)
            c.save()
            buf.seek(0)
            page.merge_page(PdfReader(buf).pages[0])
        writer.add_page(page)

    output.parent.mkdir(parents=True, exist_ok=True)
    with open(output, "wb") as fh:
        writer.write(fh)


async def build(html_dir: Path, output: Path) -> None:
    from pypdf import PdfWriter

    css = (SOURCE / "_static" / "print.css").read_text(encoding="utf-8")
    today = dt.date.today()
    date_str = f"{today.day} de {MONTHS_PT[today.month - 1]} de {today.year}"

    with tempfile.TemporaryDirectory() as tmpdir:
        work = Path(tmpdir)
        docs = await print_pages(doc_order(html_dir), css, work)

        cover_pdf = work / "cover.pdf"
        cover_pages = await print_html_fragment(
            cover_html(date_str), css, html_dir, cover_pdf
        )

        # O sumário é gerado duas vezes: a segunda já conhece seu próprio tamanho.
        toc_pages = 1
        toc_pdf = work / "toc.pdf"
        entries: list[dict] = []
        for _ in range(3):
            entries = []
            cursor = cover_pages + toc_pages + 1
            for doc in docs:
                for h in doc["headings"]:
                    entries.append({**h, "page": cursor})
                cursor += doc["pages"]
            produced = await print_html_fragment(
                toc_html(entries), css, html_dir, toc_pdf
            )
            if produced == toc_pages:
                break
            toc_pages = produced

        writer = PdfWriter()
        for part in [cover_pdf, toc_pdf, *[d["pdf"] for d in docs]]:
            writer.append(str(part))
        merged = work / "merged.pdf"
        with open(merged, "wb") as fh:
            writer.write(fh)

        stamp_footers(merged, output, skip_first=1)

    print(f"PDF gerado em {output} ({len(entries)} entradas no sumário)")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--html", default=str(ROOT / "build" / "html"))
    parser.add_argument(
        "--output", default=str(ROOT / "build" / "html" / "_static" / "relatorio-jurandi.pdf")
    )
    args = parser.parse_args()

    html_dir = Path(args.html).resolve()
    if not (html_dir / "index.html").exists():
        print(
            f"HTML não encontrado em {html_dir}. Rode antes: "
            "sphinx-build -b html source build/html",
            file=sys.stderr,
        )
        return 1

    asyncio.run(build(html_dir, Path(args.output)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
