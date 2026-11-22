# Task II — Additional Inputs Dialog

## What I implemented

I worked on the Additional Inputs dialog part of the UI task. The change covers validation of Custom fields and protection against losing edits:

- Save is blocked if an applicable Custom field is blank.
- The validation message names the missing field and shows its tab/input context.
- Multiple missing fields are reported together.
- The dialog tracks changes and warns before closing if there are unsaved edits.
- Cancel keeps the dialog open; Discard closes it.
- Saving clears the modified flag.

The helper is in additional_input_validation.py; the dialog changes are in additional_inputs.py. The tests are in the two tests/unit/test_additional_input_*.py files.

## Tests and screenshots

The two new test files contain 18 tests. A recorded run reported 23 tests passing on commit 15e8bce; a later full unit run reported 25 passed. These are recorded results and have not been rerun on the latest branch head.

Five screenshots are committed under docs/images/:
- 01_empty_custom_validation_error.png
- 02_multiple_empty_custom_errors.png
- 03_unsaved_changes_warning.png
- 04_cancel_keeps_dialog_and_value.png
- 05_discard_then_reopen_value_restored.png

I have verified the files are present in the repository listing, but I have not re-opened every image for a visual quality check in this final review.

## Scope not covered

The interactive 2D CAD editing and transverse-member plotting subtasks were not implemented. This report covers only the Additional Inputs dialog part of Task II.
