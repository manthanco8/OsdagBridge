# Additional Inputs Dialog: Custom-value Validation and Unsaved-changes Warning

Scope: FOSSEE Winter Internship 2026 screening, Task II (UI validation and state management).
Branch: `feature/screening-tasks` (fork: `manthanco8/OsdagBridge`).
This change only touches dialog behaviour. No structural design calculation, default value or
analysis code was modified.

## 1. Objective

1. Do not let the user save the Additional Inputs dialog while a parameter is set to **Custom**
   but its value field is empty.
2. Do not let the user lose edits by accident: warn when the dialog is closed with unsaved changes.
3. Use the central keys from `core/utils/common.py` instead of hard-coded parameter strings.

## 2. Behaviour

### 2.1 Save validation
- Clicking **Save** first checks every applicable "Custom" input.
- If any is empty, the save is cancelled and one error dialog (the existing `CustomMessageBox`,
  type Critical) lists **every** empty parameter, one per entry:

  `Error: The custom value for '<Parameter Name>' cannot be empty.`

  Below each entry the tab path is shown, for example `(Loading > Wind Load)`.
- Hidden or disabled value fields, and fields inside a disabled tab, are not checked
  (for example Density/Area are hidden for a Custom crash barrier).
- When all applicable Custom inputs are filled, Save works exactly as before.

### 2.2 Unsaved-changes warning
- `self.is_modified` becomes `True` when the user changes an input to a **different** value.
- On close (title-bar X, `close()`, or the Esc key) with `is_modified == True`, this warning is shown
  with the buttons **Discard** and **Cancel**:

  `You have unsaved changes. Closing this window will discard them. Do you want to proceed?`

- **Discard**: the dialog closes; on the next open it reloads from the saved input dictionary,
  so the discarded edits are gone.
- **Cancel** (or closing the warning itself): the dialog stays open with all entered values.
- No warning when nothing changed, or right after a successful Save (Save resets the flag).
- Opening the dialog, loading defaults and building the UI never set the flag
  (`_suppress_modified()` guard plus a reset when the dialog is shown).

## 3. Files changed

| File | Purpose |
|---|---|
| `src/osdagbridge/core/bridge_types/plate_girder/additional_input_validation.py` (new) | Qt-free helper: discovers Custom selector/value pairs, finds the empty ones, formats the error. |
| `src/osdagbridge/desktop/ui/dialogs/additional_input/additional_inputs.py` | Hooks the helper into `_save_inputs`; adds `is_modified`, `closeEvent`, `reject`, change tracking. |
| `tests/unit/test_additional_input_validation.py` (new) | 9 unit tests for the helper (no GUI). |
| `tests/unit/test_additional_inputs_dialog.py` (new) | 9 offscreen GUI tests on the real dialog. |

## 4. How it works

**Where Custom pairs come from (no hard-coded names).**
1. `TYPE_MODE_LINE` fields in `ADDITIONAL_INPUTS_SCHEMA` whose `mode_choices` contain "Custom" are
   discovered by walking the schema. The UI builder names their widgets `<field_id>.mode` and
   `<field_id>.value`, so the dialog looks them up by those central keys. A new mode/value field is
   validated automatically.
2. Some Custom selectors are plain combo boxes that unlock separate line edits (crash barrier,
   median, railing, wearing course). The schema does not link them, so
   `CUSTOM_VALUE_DEPENDENCIES` maps the combo key to the dependent keys, using the existing
   `KEY_CB_*`, `KEY_MD_*`, `KEY_RL_*` and `KEY_WC_*` constants.

**Keys.** The task text mentions `KEY_ADD_...`; in this repository the central keys use other
prefixes (`KEY_WL_*`, `KEY_CB_*`, ...). Existing constants were reused. No new key was added.

**Labels.** Schema labels contain HTML (`C<sub>D</sub>`); tags and a trailing colon are removed
for the message.

**Change tracking.** `_update_input_dict` marks the dialog modified only if the stored value really
changed. The segment table and member-bound dialogs, which write to the dictionary directly, do the
same check.

**Closing.** `closeEvent` and `reject` (used by Esc, which does not call `closeEvent`) share one
helper, `_confirm_discard_changes`. Anything other than the **Discard** button counts as Cancel.

## 5. Testing

Automated (run on the pushed commit `15e8bce`, from a fresh clone and on the developer machine):

```
python -m pytest tests -q
23 passed
```

18 of the 23 are new. They cover: helper discovery from the schema, empty and whitespace-only
Custom values, hidden fields being skipped, several errors at once, exact message format, save
blocked, save allowed, flag reset after save, Cancel, Discard, Esc, no warning when unmodified,
reopen after Discard. The GUI tests build the real `AdditionalInputs` dialog offscreen and replace
only the popup class with a recorder.

Manual GUI checks (app run with `python -m osdagbridge.desktop`):

| Check | Result |
|---|---|
| Custom + empty value, Save | Error popup names the parameter and tab path; nothing saved |
| Several empty Custom inputs | All listed together |
| Fill the value, Save again | The matching error disappears; save succeeds |
| Change a value, click X | Warning with Discard / Cancel and the exact text |
| Cancel | Dialog stays open, edited value kept |
| Discard, reopen | Dialog closes; edited value is back to the saved one |
| Save, then X without changes | Dialog closes with no warning |

Screenshots are in `docs/images/` (see the report).

## 6. Limitations

- The Esc key was verified by an automated test only, not by hand.
- Combo boxes that unlock separate line edits must be listed in `CUSTOM_VALUE_DEPENDENCIES`;
  a new field of that kind needs one line there.
- `is_modified` is driven by the central change handler plus the segment table and member-bound
  dialogs. Other special tables or dialogs inside the Additional Inputs window were not
  individually tested for change tracking.
- Adaptive "Custom" design-mode blocks are not part of this validation.
- Only the Additional Inputs dialog is covered; 2D CAD editing and plotting are separate tasks.
