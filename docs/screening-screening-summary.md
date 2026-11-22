# Winter Internship Screening — Contribution Summary (Applicant)

## Repository / branch
- Fork: `manthanco8/OsdagBridge`
- Working branch: `feature/screening-tasks`
- Local working copy: `C:\\Users\\Manthan\\OsdagBridge` (do not include this personal path in public evidence)

## Task I — Report Generator Presentation Refactor
**Progress: implementation and applicant-run unit tests recorded; PDF visual verification pending.**
- Centralized report style settings and updated report generator to use them.
- Added repeated headings to reviewed continuation tables.
- Applicant-run results recorded: targeted style tests 4 passed; unit suite 25 passed.
- Not verified: PDF compilation, generated PDF visual inspection, before/after evidence, complex Chapter 5 tables.
- Report: `docs/screening-task-1/contribution-report.md`.

## Task II — UI, 2D CAD, Plotting Enhancements
**Progress: Additional Inputs validation/unsaved-state implementation and reported tests documented.**
- Custom-field validation with context and grouped missing-field messages.
- Save blocked for missing required custom values.
- Unsaved-state confirmation and state reset after save.
- Recorded 18 tests passed; applicant GUI checks reported.
- Screenshot directory `docs/screenshots/task-2/` needs existence/content verification before submission.
- Contribution report: `docs/screening-task-2/contribution-report.md`.
- No claim is made for unverified 2D CAD/plotting work.

## Task III — Parametric Substructure / IFC
**Progress: safe file-workflow checklist only; implementation/engineering validation not done.**
- Checklist covers file presence/readability/schema, open/close, path handling and evidence capture with approved fixtures.
- No bridge geometry, structural dimensions, reinforcement, calculation, or design adequacy checks are claimed.
- Checklist: `docs/screening-task-3/ifc-file-workflow-checklist.md`.

## Task IV — Software Testing & Issue Reporting
**Progress: two software checks confirmed; remaining checks not run.**
- UI-01 Startup: PASS (app opened, user confirmed).
- UI-02 Picker cancellation: PASS (cancel returned to app normally, user confirmed).
- UI-03 Invalid path: NOT RUN.
- UI-04 Unsaved-state warning: NOT RUN (window closed with no edits; no warning was expected).
- UI-05 Input validation UI: NOT RUN.
- UI-06 Report destination: NOT RUN.
- OBS-01 Qt runtime message: observed excerpt documented; trigger and reproducibility unknown, root cause not established.
- Evidence log: `docs/screening-task-4/software-test-evidence-log.md`.
- Observation report: `docs/screening-task-4/observed-qt-runtime-message.md`.

## Final verification checklist (complete before submission)
- [ ] Pull latest branch locally and confirm `git status` clean.
- [ ] Re-run relevant applicant-safe unit tests for Tasks I and II; save exact output.
- [ ] Confirm Task II screenshot files exist, open correctly, and are committed; remove any personal/sensitive paths from screenshots.
- [ ] Confirm contribution reports and this summary are present on branch.
- [ ] Do not claim PDF visual verification unless an approved sample/report is generated and reviewed.
- [ ] Do not mark Task IV tests PASS unless actually performed; retain NOT RUN for untested items.
- [ ] Review branch commit history and prepare a concise submission message with fork/branch and documented work.

## Limitations
This summary reflects recorded changes and user-confirmed test observations. It does not claim maintainer acceptance, complete screening-task coverage, or engineering validation.
