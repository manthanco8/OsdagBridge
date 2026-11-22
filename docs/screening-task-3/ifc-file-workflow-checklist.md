# Task III — Safe IFC Workflow Validation Checklist

## Scope
This checklist covers file/workflow validation only. It does not validate bridge geometry, structural dimensions, reinforcement, load cases, calculations, or design adequacy. Those checks must be performed by qualified maintainers using approved examples.

## Preconditions
- Use a maintainer-approved sample IFC file and project.
- Do not alter design parameters or engineering inputs.
- Record software version, OS, Python environment, and sample-file provenance.
- Keep the original IFC unchanged; use a copy for validation.

## File-level checks
- [ ] File exists at the selected path.
- [ ] File extension and reported format are consistent.
- [ ] File is non-empty and readable by the approved IFC parser.
- [ ] Parser reports a supported IFC schema/version.
- [ ] Opening and closing the file produces no parser exception.
- [ ] If export is part of the approved workflow, confirm an output file is created and can be reopened.
- [ ] Compare file metadata and parser status only; do not infer engineering correctness from successful parsing.

## UI workflow checks
- [ ] File selection dialog opens and can be cancelled safely.
- [ ] Selected path is displayed correctly.
- [ ] Invalid or missing path produces a clear message.
- [ ] Unsupported file type is handled without crashing.
- [ ] Existing output files are not overwritten without explicit confirmation.

## Evidence to capture
For each check, record: check ID, date/time, software commit/version, sample identifier (not sensitive path), expected behavior, actual behavior, PASS/FAIL/NOT RUN, screenshot/log reference, and reviewer.

## Reporting
- Mark checks NOT RUN until actually executed.
- Report parser/file handling observations only.
- Escalate geometry, reinforcement, coordinate, quantity, or structural-result discrepancies to a qualified maintainer; do not attempt to resolve them by changing design logic or parameters.
