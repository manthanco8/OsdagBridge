# Screening Task I — Report Presentation Refactoring

## Scope of this increment

This increment is limited to report presentation configuration. It does not change engineering inputs, structural calculations, result values, or interpretation of design checks.

## Changes

- Added `src/osdagbridge/core/reports/report_styles.py` to centralize page margin, table column padding, row stretch, longtable spacing, table rule thickness, extra row height, page-bottom guard threshold, and brand color.
- Updated `report_generator.py` to consume centralized page-margin and table-layout settings in its LaTeX preamble.
- Added `tests/unit/test_report_styles.py` to check centralized values and generated LaTeX layout string formatting.
- Existing chapter code and engineering calculation/report content are intentionally unchanged.
- Remote source audit counted longtable environments by chapter: Chapter 2 has 9 (1 repeating-header block), Chapter 3 has 7 (none), Chapter 4 has 3 (1 repeating-header block), Chapter 5 has 30 (none), and Chapter 7 has 1 (none). This is a source-level count only; some tables may be short enough not to split. Header refactoring needs per-table review because table structures vary.

## Validation status

- Automated tests have been authored but **not run in this remote editing session**. Run locally from repository root: `pytest tests/unit/test_report_styles.py -q`.
- PDF compilation, page-break behavior, and before/after PDF comparison remain pending local GUI/LaTeX validation.
- No structural calculation results have been verified or modified as part of this presentation-only work.

## Next safe work

1. Run the new unit tests locally and report any failures.
2. Generate a report using an existing approved sample without changing engineering inputs, then inspect page breaks, repeated table headers, and footer collisions.
3. Capture before/after PDF evidence using the same approved sample.
4. Review chapter-specific longtable headers table-by-table; avoid blanket edits to tables with complex header structures.
5. Complete the remaining presentation-only refactor after local validation.

## Submission checklist

- [ ] Before PDF captured
- [ ] After PDF captured
- [ ] Local tests run
- [ ] LaTeX compile and visual review completed
- [ ] Technical changes note updated with verified results
- [ ] Maintainer review of any changes affecting engineering result presentation