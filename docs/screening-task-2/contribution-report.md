# Screening Task II — Contribution Report

## Task
UI, 2D CAD, and Plotting Enhancements — focused contribution on Additional Inputs validation and unsaved-state behavior in the desktop UI.

## Changes implemented
- Added validation for required fields when Custom mode is selected.
- Validation messages include missing field names and tab/input-path context.
- Multiple missing fields are reported together.
- Saving is blocked when required Custom values are missing.
- Added modified/unsaved-state tracking.
- Added a close confirmation for unsaved changes with Cancel and Discard options.
- Escape-key handling was included in the dialog workflow.
- Modified state is reset after successful save.

## Testing and evidence
- Automated tests: 18 passed (previously reported and recorded for this task).
- GUI verification: applicant-confirmed checks of validation messages, multiple missing fields, and unsaved-changes behavior.
- Screenshot evidence was reported as collected under `docs/screenshots/task-2/`; repository presence and image contents should be re-checked before final packaging.

## Limitations / remaining verification
- This report documents UI behavior only.
- Any 2D CAD or plotting changes beyond the above are not claimed here.
- Re-run relevant tests on the current branch before final submission and verify screenshots are committed and viewable.
- No structural calculations, engineering inputs, or result interpretations were changed as part of this UI validation contribution.

## Summary
The task contribution focuses on user-facing validation and safe unsaved-state handling. Final submission should include the current commit reference, fresh test output, and verified screenshot evidence.
