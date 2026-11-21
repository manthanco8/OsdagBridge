"""Validation helpers for the Additional Inputs dialog ("Custom" values).

This module has no Qt dependency, so the logic can be unit-tested without a GUI.
The dialog supplies two small callables that read the live widgets; everything
else (which fields to check, how to word the error) lives here.

Two kinds of "Custom" input exist in the schema:

1. ``TYPE_MODE_LINE`` fields: a mode combo plus a value line-edit, created by
   the UI builder with the object names ``<id>.mode`` and ``<id>.value``.
   These are discovered automatically by walking the schema, so any new
   mode/value field is validated without touching this file.
2. A plain combo that contains a "Custom" choice and unlocks *other* line-edits
   (crash barrier, median, railing, wearing course). The schema does not link
   them, so ``CUSTOM_VALUE_DEPENDENCIES`` records the link using central keys.
"""

import re
from dataclasses import dataclass
from typing import Callable, Iterable, Optional

from osdagbridge.core.utils.common import (
    TYPE_MODE_LINE,
    KEY_CB_TYPE, KEY_CB_DENSITY, KEY_CB_WIDTH, KEY_CB_HEIGHT, KEY_CB_AREA, KEY_CB_LOAD,
    KEY_MD_TYPE, KEY_MD_DENSITY, KEY_MD_WIDTH, KEY_MD_HEIGHT, KEY_MD_AREA, KEY_MD_LOAD,
    KEY_RL_TYPE, KEY_RL_WIDTH, KEY_RL_HEIGHT, KEY_RL_LOAD_MODE, KEY_RL_LOAD_VALUE,
    KEY_WC_MATERIAL, KEY_WC_DENSITY,
)

CUSTOM = "Custom"

# Object-name suffixes used by UIBuilder._create_mode_line_field
MODE_SUFFIX = ".mode"
VALUE_SUFFIX = ".value"

# combo key -> line-edit keys that must be filled when that combo is "Custom".
# Only widgets that are visible AND enabled at save time are actually checked
# (e.g. Density/Area are hidden for a Custom crash barrier), see find_missing_custom_values.
CUSTOM_VALUE_DEPENDENCIES = {
    KEY_CB_TYPE: [KEY_CB_DENSITY, KEY_CB_WIDTH, KEY_CB_HEIGHT, KEY_CB_AREA, KEY_CB_LOAD],
    KEY_MD_TYPE: [KEY_MD_DENSITY, KEY_MD_WIDTH, KEY_MD_HEIGHT, KEY_MD_AREA, KEY_MD_LOAD],
    KEY_RL_TYPE: [KEY_RL_WIDTH, KEY_RL_HEIGHT],
    KEY_RL_LOAD_MODE: [KEY_RL_LOAD_VALUE],
    KEY_WC_MATERIAL: [KEY_WC_DENSITY],
}


@dataclass(frozen=True)
class CustomInputSpec:
    """One "Custom selector -> value field" pair."""
    trigger_name: str   # objectName of the QComboBox that can be set to "Custom"
    value_name: str     # objectName of the QLineEdit that must then be filled
    label: str          # human readable parameter name for the error message


def strip_html(text: str) -> str:
    """'Drag Coefficient, C<sub>D</sub>' -> 'Drag Coefficient, CD'; drops a trailing colon."""
    plain = re.sub(r"<[^>]+>", "", text or "")
    return plain.strip().rstrip(":").strip()


def _walk(node):
    """Yield every dict nested anywhere inside lists/dicts of the schema."""
    if isinstance(node, dict):
        yield node
        for value in node.values():
            yield from _walk(value)
    elif isinstance(node, (list, tuple)):
        for item in node:
            yield from _walk(item)


def build_custom_input_specs(schema_tabs: Iterable[dict]) -> list:
    """Build the list of CustomInputSpec from ADDITIONAL_INPUTS_SCHEMA."""
    fields = [d for tab in schema_tabs for d in _walk(tab.get("schema", {})) if d.get("id")]
    labels = {d["id"]: d.get("label", "") for d in fields}

    specs, seen = [], set()

    def add(spec: CustomInputSpec):
        marker = (spec.trigger_name, spec.value_name)
        if marker not in seen:
            seen.add(marker)
            specs.append(spec)

    # 1. mode combo + value line-edit pairs (discovered from the schema)
    for field in fields:
        if field.get("type") == TYPE_MODE_LINE and CUSTOM in (field.get("mode_choices") or []):
            add(CustomInputSpec(
                trigger_name=field["id"] + MODE_SUFFIX,
                value_name=field["id"] + VALUE_SUFFIX,
                label=strip_html(field.get("label", "")) or field["id"],
            ))

    # 2. combo "Custom" choice that unlocks separate line-edits
    for trigger_key, value_keys in CUSTOM_VALUE_DEPENDENCIES.items():
        for value_key in value_keys:
            add(CustomInputSpec(
                trigger_name=trigger_key,
                value_name=value_key,
                label=strip_html(labels.get(value_key, "")) or value_key,
            ))
    return specs


def find_missing_custom_values(
    specs: Iterable[CustomInputSpec],
    get_trigger_text: Callable[[str], Optional[str]],
    get_value_text: Callable[[str], Optional[str]],
) -> list:
    """Return the specs whose selector is "Custom" but whose value is empty.

    get_trigger_text(name) -> current text of the selector, or None if it does not exist.
    get_value_text(name)   -> text of the value field, or None when the field does not
                              exist / is hidden / is disabled (i.e. not applicable).
    """
    missing = []
    for spec in specs:
        trigger = get_trigger_text(spec.trigger_name)
        if trigger is None or trigger.strip() != CUSTOM:
            continue
        value = get_value_text(spec.value_name)
        if value is None:          # not applicable right now
            continue
        if not value.strip():
            missing.append(spec)
    return missing


def format_empty_custom_error(label: str) -> str:
    return f"Error: The custom value for '{label}' cannot be empty."
