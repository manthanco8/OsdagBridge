# Task IV — Software Test Evidence Log

Use this log for checks that have actually been performed. Leave the status as NOT RUN until the test is executed. This log is for software/UI behavior only and excludes structural design validation.

## Test environment
- Date/time:
- OS:
- Python version:
- Conda environment:
- Repository branch and commit:
- Tester:

## Test record template
| ID | Software check | Preconditions | Steps performed | Expected behavior | Actual behavior | Status (PASS/FAIL/NOT RUN) | Evidence/log reference | Notes |
|---|---|---|---|---|---|---|---|
| UI-01 | Application startup | Environment configured | Launch desktop app | App opens or provides clear error | | NOT RUN | | |
| UI-02 | Cancel file picker | App open | Open picker; cancel | Dialog closes without unintended state change | | NOT RUN | | |
| UI-03 | Invalid file path handling | App open | Use approved invalid-path scenario | Clear error; no crash | | NOT RUN | | |
| UI-04 | Unsaved-state dialog | Safe UI test context | Trigger documented unsaved-state flow | Choices are clear; cancel preserves state | | NOT RUN | | |
| UI-05 | Input validation UI | Approved software test fixture | Submit intentionally incomplete UI fixture only | Validation message is clear; no silent save | | NOT RUN | | |
| UI-06 | Report destination handling | Approved fixture, no design execution | Check path selection/validation only | Clear path handling; no unintended overwrite | | NOT RUN | | |

## Evidence naming
Use `task-4/<test-id>-<short-description>.png` for screenshots and `task-4/logs/<test-id>.txt` for logs. Do not include sensitive personal paths or project data in shared evidence.

## Issue report
If a software issue is observed, copy the details into `software-issue-template.md`, include exact software/environment versions, steps, expected and actual behavior, and sanitized evidence. Do not speculate about structural correctness or propose design-logic fixes.

## Boundary
This log does not cover engineering calculations, structural input combinations, load cases, design adequacy, reinforcement, or geometry correctness. Such testing requires approved procedures and qualified review.
