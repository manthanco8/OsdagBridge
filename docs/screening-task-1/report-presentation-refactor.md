# Screening Task I — Report Presentation Refactoring

## Scope of this increment

This increment is limited to report presentation configuration. It does not change engineering inputs, structural calculations, result values, or interpretation of design checks.

## Changes

- Added `src/osdagbridge/core/reports/report_styles.py` to centralize page margin, table column padding, row stretch, longtable spacing, table rule thickness, extra row height, page-bottom guard threshold, and brand color.
- Updated `report_generator.py` to consume centralized page-margin and table-layout settings in its LaTeX preamble.
- Added `tests/unit/test_report_styles.py` to check centralized values, table layout strings, caption settings, and line spacing.
- Added repeated column headers for all 7 Chapter 3 longtables (5 parameter tables and 2 additional sections as counted in source), and for the Chapter 7 bill-of-materials table using LaTeX `\endfirsthead` / `\endhead`. Presentation-only changes; row values and quantity fields are untouched.
- Existing engineering calculation/report content is intentionally unchanged.
- Remote source audit counted longtable environments by chapter: Chapter 2 has 9 (1 repeating-header block), Chapter 3 has 7 (now all with repeating headers), Chapter 4 has 3 (1 repeating-header block), Chapter 5 has 30 (none), and Chapter 7 has 1 (now with a repeating header). This is a source-level count only; some tables may be short enough not to split. Chapter 5 needs per-table review because table structures vary.

## Validation status

- Local verification reported by the applicant: `pytest tests/unit/test_report_styles.py -q` → 4 passed; `pytest tests/unit -q` → 25 passed (26.50 seconds).
- PDF compilation, page-break behavior, and before/after PDF comparison remain pending local GUI/LaTeX validation.
- No structural calculation results have been verified or modified as part of this presentation-only work.

## Next safe work

1. Run the new unit tests locally and report any failures.
2. Generate a report using an existing approved sample without changing engineering inputs, then inspect page breaks, repeated table headers, and footer collisions.
3. Capture before/after PDF evidence using the same approved sample.
4. Review Chapter 2 and Chapter 4 longtable headers table-by-table, and defer Chapter 5's complex 30 tables until a safe visual review.
5. Complete the remaining presentation-only refactor after local validation.

## Submission checklist

- [ ] Before PDF captured
- [ ] After PDF captured
- [x] Local unit tests run (25 passed, applicant-reported)
- [ ] LaTeX compile and visual review completed
- [ ] Technical changes note updated with verified results
- [ ] Maintainer review of any changes affecting engineering result presentation