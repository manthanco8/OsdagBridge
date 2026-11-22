# Screening Task IV — Software-Only Test Plan

## Scope and safety boundary
This plan covers software/UI behavior and evidence handling only. It does not prescribe structural input values, design runs, engineering calculations, result comparisons, or validation of bridge safety. Engineering-specific test scenarios must be supplied and reviewed by the project maintainer using approved test fixtures.

## Environment record
Record these before a test session:
- OS and version
- Python version
- Conda environment name
- Repository branch and commit
- App launch method
- Date/time
- Tester

## Safe software checks
| ID | Area | Software-only check | Expected behavior | Evidence |
|---|---|---|---|---|
| SW-UI-01 | Startup | Launch using documented command in configured environment | App opens or reports a clear error; record exact error if startup fails | Screenshot/log |
| SW-UI-02 | Navigation | Open/close available tabs or panels without editing engineering inputs | UI navigation works and no unexpected crash | Screenshot |
| SW-UI-03 | Input validation UI | On maintainer-approved fixture, check validation feedback for an intentionally blank required UI field only if the maintainer confirms this is a safe UI test | Clear field-specific validation message; no unintended save | Screenshot |
| SW-UI-04 | Unsaved-state prompt | Use a non-engineering UI setting or maintainer-approved fixture to observe modified-state prompt | Prompt offers expected safe actions; record behavior | Screenshot |
| SW-UI-05 | File dialog | Open and cancel a file/location dialog | Cancel returns to prior screen without unexpected state change | Screenshot |
| SW-UI-06 | Error handling | Record any reproducible software exception using the issue template | Error is logged or presented clearly; no assumptions about engineering correctness | Log/screenshot |
| SW-UI-07 | Report path handling | Inspect report destination selection and cancellation behavior without initiating a bridge design calculation | UI path selection/cancel behavior is clear and stable | Screenshot |
| SW-UI-08 | Documentation | Follow setup/run instructions as written | Instructions are reproducible; note missing or stale steps | Notes |

## Procedure
1. Confirm the maintainer-approved test fixture or a non-engineering UI workflow. Do not create or alter bridge design parameters.
2. Record environment and repository commit.
3. Run only the software/UI checks within the safe scope.
4. For each issue, capture a screenshot and/or exact error text, then complete the issue template.
5. Avoid duplicate reports; search existing issues or ask the maintainer before filing.
6. Share evidence with the maintainer for engineering-specific review where needed.

## Result status
Use only: PASS, FAIL, BLOCKED, NOT RUN.
Do not mark tests PASS without actually executing them and recording evidence.
