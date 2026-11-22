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
| UI-01 | Application startup | Environment configured | Launched desktop app locally | App opens or provides clear error | App opened successfully | PASS | `screenshots/task-4/01-app-startup.png` | Screenshot captured and verified present locally on 2026-11-22 |
| UI-02 | Cancel file picker | App open | Clicked Select Location; opened picker; cancelled without selecting | Dialog closes without unintended state change | App returned normally; no crash/freeze reported | PASS | User-confirmed picker cancellation |
| UI-03 | Invalid file path handling | App open | Use approved invalid-path scenario | Clear error; no crash | | NOT RUN | | |
| UI-04 | Unsaved-state dialog | Safe UI test context | Closed Additional Inputs without editing anything | Warning not shown (no changes made; expected) | NOT RUN | User-confirmed no warning appeared | Test requires safe approved UI fixture with actual unsaved change; not attempted |
| UI-05 | Input validation UI | Approved software test fixture | Submit intentionally incomplete UI fixture only | Validation message is clear; no silent save | | NOT RUN | | |
| UI-06 | Report destination handling | Approved fixture, no design execution | Check path selection/validation only | Clear path handling; no unintended overwrite | | NOT RUN | | |
| OBS-01 | Qt runtime message observation | App had been opened during UI checks | User shared terminal excerpt; trigger not captured | No unexpected window-handle/event-dispatch error | Qt message and stack excerpt observed; cause/repro unknown | OBSERVED (not a test) | `observed-qt-runtime-message.md` | Full log and triggering action unavailable; do not treat as reproduced

## Evidence naming
Use `task-4/<test-id>-<short-description>.png` for screenshots and `task-4/logs/<test-id>.txt` for logs. Do not include sensitive personal paths or project data in shared evidence.

## Issue report
If a software issue is observed, copy the details into `software-issue-template.md`, include exact software/environment versions, steps, expected and actual behavior, and sanitized evidence. Do not speculate about structural correctness or propose design-logic fixes.

## Boundary
This log does not cover engineering calculations, structural input combinations, load cases, design adequacy, reinforcement, or geometry correctness. Such testing requires approved procedures and qualified review.
