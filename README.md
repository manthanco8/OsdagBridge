# OsdagBridge

OsdagBridge is a modular plugin for the Osdag project. It currently supports plate-girder bridges and provides desktop (PySide6), web (Django + React), and command-line interfaces through a shared Python core.

## Key features

- Shared core for input handling, analysis, design, CAD, and reports.
- Bridge-type modules and reusable components.
- Native, OpenSeesPy, and OspGrillage solver adapters.
- Indian standards support in the codebase.

## Screening-task work on this branch

### Task I — LaTeX Report Generator (partial)

I made presentation-focused changes: added a shared style-settings module, connected report generation to it, and added repeating headings to selected long tables. Unit tests were added for the style settings.

The work is incomplete. The report has not been compiled or visually reviewed, and the requested before/after PDFs are not available. Utilization-ratio and material-quantity charts, and the live-load/footway table refactor, were not implemented. Chapter 2's short tabular tables were also corrected so they no longer contain longtable-only header commands.

Recorded test results: 4 report-style tests passed; a later full unit run reported 25 passed. These are recorded runs, not a fresh run of the current head.

### Task II — UI, 2D CAD, and Plotting (partial)

I implemented the Additional Inputs validation/state-management part only:
- Blocks Save when applicable Custom fields are blank.
- Shows the missing field names and groups multiple errors.
- Tracks changed values and warns before closing with unsaved changes.
- Cancel keeps the dialog open; Discard closes it; successful Save clears the modified flag.

The 18 tests in the two new Task II test files were recorded as passing. The manual checks are documented, and screenshots are stored in docs/images/. The interactive 2D CAD editing and transverse-member plotting subtasks were not done.

### Task III — Substructure / IFC

This branch contains a file-workflow checklist only. No parametric substructure geometry or IFC integration code was implemented.

### Task IV — Software Testing and Issue Reporting (partial)

I documented a software-only test plan, issue template, evidence log, and an observed Qt message. Startup and file-picker cancellation were recorded as PASS. Other UI checks remain NOT RUN, and the Qt message has not been reproduced. This is not a complete Task IV testing report.

## Run the desktop app

From the repository's configured environment:

```bash
python -m osdagbridge.desktop
```

## Tests

```bash
pytest -q
```

## Project structure

```
OsdagBridge/
├── docs/
├── examples/
├── tests/
└── src/
    └── osdagbridge/
        ├── core/
        ├── bridge_types/
        ├── bridge_components/
        ├── cli/
        ├── desktop/
        └── web/
```

## License

See LICENSE.
