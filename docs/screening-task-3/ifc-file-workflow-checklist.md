# Task III — IFC File Workflow Checklist

This is a checklist I prepared for file-handling checks in the IFC workflow. It is not an implementation of the substructure or IFC task.

## Before testing

- Use a maintainer-approved sample file and project.
- Keep the original file unchanged; work with a copy.
- Record the software version, operating system, Python environment, and sample-file source.

## File checks

- Confirm the file exists and is non-empty.
- Check that its extension and format agree.
- Confirm that the approved parser can read it and reports a supported schema.
- Check that opening and closing the file does not raise a parser exception.
- If export is part of the approved workflow, confirm the output exists and can be reopened.

These checks confirm file handling only; they do not establish geometry or engineering correctness.

## UI checks

- Open and cancel the file picker.
- Confirm the selected path is displayed correctly.
- Record how missing paths and unsupported file types are handled.
- Check that existing output files are not overwritten without confirmation.

## Evidence

For each check, record the test ID, date/time, app version/commit, sample identifier, expected and actual behavior, result (PASS/FAIL/NOT RUN), and screenshot/log reference.

## Status

No substructure geometry or IFC integration code was added for this task. The checklist itself has not been completed against an approved IFC fixture.
