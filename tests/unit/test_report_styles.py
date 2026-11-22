"""Unit tests for centralized report presentation settings."""
from osdagbridge.core.reports.report_styles import (
    REPORT_PAGE_MARGIN,
    REPORT_TABLE_COLUMN_PADDING_PT,
    REPORT_TABLE_ROW_STRETCH,
    REPORT_BRAND_GREEN_HEX,
    latex_table_layout,
    latex_document_style,
)

def test_report_style_settings_are_centralized():
    assert REPORT_PAGE_MARGIN == "1in"
    assert REPORT_TABLE_COLUMN_PADDING_PT == "6"
    assert REPORT_TABLE_ROW_STRETCH == "1.12"
    assert REPORT_BRAND_GREEN_HEX == "91B014"

def test_latex_table_layout_contains_shared_settings():
    layout = latex_table_layout()
    assert r"\setlength{\tabcolsep}{6}pt" in layout
    assert r"\renewcommand{\arraystretch}{1.12}" in layout
    assert r"\setlength{\LTpre}{0pt}" in layout
    assert r"\setlength{\LTpost}{6pt}" in layout
    assert r"\definecolor{osdagGreen}{HTML}{91B014}" in layout
    assert r"\BeforeBeginEnvironment{longtable}" in layout

def test_latex_table_layout_uses_newline_separators():
    layout = latex_table_layout()
    assert "\\n" not in layout
    assert layout.count("\n") >= 8
def test_latex_document_style_contains_caption_and_spacing_config():
    style = latex_document_style()
    assert r"\\captionsetup{" in style
    assert r"labelfont=bf" in style
    assert r"justification=raggedright" in style
    assert r"singlelinecheck=false" in style
    assert r"format=plain" in style
    assert r"\\setstretch{1.15}" in style
