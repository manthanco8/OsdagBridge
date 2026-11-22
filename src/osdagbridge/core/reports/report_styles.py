"""Centralized visual settings for OsdagBridge report presentation."""
REPORT_PAGE_MARGIN = "1in"
REPORT_TABLE_COLUMN_PADDING_PT = "6"
REPORT_TABLE_ROW_STRETCH = "1.12"
REPORT_LONGTABLE_PRE_SKIP = "0pt"
REPORT_LONGTABLE_POST_SKIP = "6pt"
REPORT_TABLE_RULE_WIDTH_PT = "0.5pt"
REPORT_EXTRA_ROW_HEIGHT = "0.6pt"
REPORT_TABLE_PAGE_GUARD_BASELINES = "5"
REPORT_BRAND_GREEN_HEX = "91B014"


def latex_table_layout():
    """Return shared LaTeX table spacing and page guard settings."""
    lines = [
        r"\setlength{\tabcolsep}{" + REPORT_TABLE_COLUMN_PADDING_PT + r"}pt",
        r"\renewcommand{\arraystretch}{" + REPORT_TABLE_ROW_STRETCH + r"}",
        r"\setlength{\LTpre}{" + REPORT_LONGTABLE_PRE_SKIP + r"}",
        r"\setlength{\LTpost}{" + REPORT_LONGTABLE_POST_SKIP + r"}",
        r"\setlength{\arrayrulewidth}{" + REPORT_TABLE_RULE_WIDTH_PT + r"}",
        r"\setlength{\extrarowheight}{" + REPORT_EXTRA_ROW_HEIGHT + r"}",
        r"\BeforeBeginEnvironment{table}{\needspace{" + REPORT_TABLE_PAGE_GUARD_BASELINES + r"\baselineskip}}",
        r"\BeforeBeginEnvironment{longtable}{\needspace{" + REPORT_TABLE_PAGE_GUARD_BASELINES + r"\baselineskip}}",
        r"\definecolor{osdagGreen}{HTML}{" + REPORT_BRAND_GREEN_HEX + r"}",
    ]
    return "\n".join(lines)


REPORT_CAPTION_LABEL_STYLE = "bf"
REPORT_CAPTION_ALIGNMENT = "raggedright"
REPORT_CAPTION_SINGLELINE_CHECK = "false"
REPORT_CAPTION_FORMAT = "plain"
REPORT_DOCUMENT_LINE_SPACING = "1.15"


def latex_document_style():
    """Return shared caption and body line-spacing configuration."""
    return chr(10).join([
        r"\captionsetup{",
        r"    labelfont=" + REPORT_CAPTION_LABEL_STYLE + r",",
        r"    justification=" + REPORT_CAPTION_ALIGNMENT + r",",
        r"    singlelinecheck=" + REPORT_CAPTION_SINGLELINE_CHECK + r",",
        r"    format=" + REPORT_CAPTION_FORMAT,
        r"}",
        r"\setstretch{" + REPORT_DOCUMENT_LINE_SPACING + r"}",
    ])
