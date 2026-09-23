project = "Jurandi"
copyright = "2026, Vitor M. S. Araújo"
author = "Vitor M. S. Araújo"
release = "1.0"

extensions = ["myst_parser", "sphinx_design"]
templates_path = ["_templates"]
exclude_patterns = []
language = "pt_BR"

myst_enable_extensions = ["colon_fence", "attrs_inline"]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["theme.css"]
html_js_files = ["theme.js"]
html_logo = "_static/laser.png"
html_favicon = "_static/favicon.png"
html_baseurl = "https://laser-robotics.github.io/laser_jurandi_report/"
html_show_sourcelink = False
html_show_sphinx = False
# Nome do PDF gerado por tools/build_pdf.py e usado pelo botão de download.
html_context = {"pdf_filename": "relatorio-jurandi.pdf"}
html_title = "Projeto Jurandi — Relatório Técnico"
html_meta = {
    "description": "Relatório técnico do veículo de superfície autônomo Jurandi, desenvolvido na UFPB.",
    "keywords": "Jurandi, ASV, robótica marinha, catamarã, Pixhawk, UFPB, LASER",
    "author": author,
}
html_theme_options = {
    "logo_only": False,
    "navigation_depth": 3,
    "collapse_navigation": False,
    "sticky_navigation": True,
    "style_external_links": True,
}
