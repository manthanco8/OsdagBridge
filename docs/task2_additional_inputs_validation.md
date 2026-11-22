# Additional Inputs Dialog — Validation and Unsaved Changes

This note describes the part of Task II I implemented: checking required Custom values before saving and warning when the dialog is closed with unsaved edits.

## Save validation

When Save is clicked, the dialog checks the applicable Custom selectors. If a Custom value is empty, saving is stopped and the error message lists the field name and its tab/input context. Multiple missing values are shown together.

Hidden, disabled, or inactive fields are skipped. The check uses central keys from common.py and discovers mode/value pairs from the input schema. A small dependency map handles Custom selectors that unlock separate value fields.

## Unsaved changes

The dialog sets is_modified when a value actually changes. If the user closes the dialog with unsaved edits, it asks whether to Discard or Cancel. Cancel keeps the dialog open with the edits; Discard closes it without saving. Saving clears the modified flag.

## Files changed

- additional_input_validation.py: Qt-free validation helper.
- additional_inputs.py: dialog validation, modified-state tracking, and close handling.
- test_additional_input_validation.py: helper tests.
- test_additional_inputs_dialog.py: dialog tests.

## Tests recorded

The two Task II test files contain 18 tests. A recorded run at commit 15e8bce reported python -m pytest tests -q → 23 passed. A later run of the full unit suite reported 25 passed. These results are historical; I have not rerun them on the current branch head.

## Screenshots

The five screenshots are stored in docs/images/ and referenced by the contribution report. I checked the repository listing for the files, but the final visual review is still pending.

## Limitations

This contribution covers the Additional Inputs dialog only. The interactive 2D CAD parameter editing and transverse-member plotting tasks are not implemented. Some special tables/dialogs may not be covered by change tracking, and the Esc path was covered by a test rather than a manual check.
