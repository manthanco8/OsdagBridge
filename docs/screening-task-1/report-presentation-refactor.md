# Task I — Report Presentation Changes

## Scope

I worked on shared presentation settings and table headings. I did not change engineering inputs, calculations, quantities, or result interpretation.

## Changes

- Added src/osdagbridge/core/reports/report_styles.py for common page margins, table padding/spacing, caption settings, line spacing, and related layout values.
- Updated report_generator.py to use the shared configuration.
- Added repeating headings to the Chapter 3 long tables and Chapter 7 bill-of-materials table, and to selected Chapter 2 tables.
- Added tests/unit/test_report_styles.py.

## Validation recorded

- Style tests: 4 passed.
- Full unit suite: 25 passed in a recorded run.

I have not compiled a report or reviewed its pages. A source check also found longtable header commands inside three regular Chapter 2 tabular environments. I removed those invalid commands from the short tables. Chapter 2 header coverage still needs review, and a report compile is required to confirm the generated LaTeX.

## Remaining Task I work

The task asks for more than the changes on this branch. I have not completed the live-load/footway table refactor or the utilization-ratio and material-quantity charts. I also have not provided the before/after PDFs or visual evidence.

This is a progress note, not a claim that Task I is complete.
