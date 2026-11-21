"""Tests for the Qt-free Custom-input validation helpers."""
import pytest

from osdagbridge.core.bridge_types.plate_girder import additional_input_validation as v
from osdagbridge.core.utils.common import (
    TYPE_MODE_LINE, KEY_WL_GUST_FACTOR, KEY_CB_TYPE, KEY_CB_WIDTH, KEY_CB_DENSITY, KEY_WC_MATERIAL,
    KEY_WC_DENSITY,
)


def _schema():
    """Tiny schema with the same nesting style as the real one (rows/fields/tabs)."""
    return [{"label": "Loading", "schema": {"tabs": [{"rows": [{"fields": [{
        "id": KEY_WL_GUST_FACTOR, "label": "Drag Coefficient, C<sub>D</sub>:",
        "type": TYPE_MODE_LINE, "mode_choices": ["As per IRC 6", "Custom"]}]}]}]}}]


def _readers(modes, values):
    return modes.get, values.get


def test_strip_html_and_colon():
    assert v.strip_html("Drag Coefficient, C<sub>D</sub>:") == "Drag Coefficient, CD"
    assert v.strip_html("") == ""


def test_mode_line_discovered_from_schema_with_central_key():
    specs = v.build_custom_input_specs(_schema())
    spec = next(s for s in specs if s.trigger_name == KEY_WL_GUST_FACTOR + v.MODE_SUFFIX)
    assert spec.value_name == KEY_WL_GUST_FACTOR + v.VALUE_SUFFIX
    assert spec.label == "Drag Coefficient, CD"


def test_dependency_pairs_are_included():
    specs = v.build_custom_input_specs(_schema())
    pairs = {(s.trigger_name, s.value_name) for s in specs}
    assert (KEY_CB_TYPE, KEY_CB_WIDTH) in pairs
    assert (KEY_WC_MATERIAL, KEY_WC_DENSITY) in pairs


def test_empty_custom_is_reported_and_whitespace_counts_as_empty():
    specs = v.build_custom_input_specs(_schema())
    mode, value = KEY_WL_GUST_FACTOR + v.MODE_SUFFIX, KEY_WL_GUST_FACTOR + v.VALUE_SUFFIX
    for text in ("", "   "):
        t, val = _readers({mode: "Custom"}, {value: text})
        missing = v.find_missing_custom_values(specs, t, val)
        assert [m.label for m in missing] == ["Drag Coefficient, CD"]


def test_filled_custom_or_non_custom_mode_is_ok():
    specs = v.build_custom_input_specs(_schema())
    mode, value = KEY_WL_GUST_FACTOR + v.MODE_SUFFIX, KEY_WL_GUST_FACTOR + v.VALUE_SUFFIX
    t, val = _readers({mode: "Custom"}, {value: "1.5"})
    assert v.find_missing_custom_values(specs, t, val) == []
    t, val = _readers({mode: "As per IRC 6"}, {value: ""})
    assert v.find_missing_custom_values(specs, t, val) == []


def test_inactive_value_field_is_skipped():
    specs = v.build_custom_input_specs(_schema())
    # Custom crash barrier, but Density is hidden (None) while Width is shown and empty
    t, val = _readers({KEY_CB_TYPE: "Custom"}, {KEY_CB_WIDTH: ""})
    missing = v.find_missing_custom_values(specs, t, val)
    assert {m.value_name for m in missing} == {KEY_CB_WIDTH}
    assert KEY_CB_DENSITY not in {m.value_name for m in missing}


def test_multiple_missing_are_all_reported():
    specs = v.build_custom_input_specs(_schema())
    t, val = _readers({KEY_CB_TYPE: "Custom", KEY_WC_MATERIAL: "Custom"},
                      {KEY_CB_WIDTH: "", KEY_WC_DENSITY: ""})
    assert len(v.find_missing_custom_values(specs, t, val)) == 2


def test_error_message_format():
    assert v.format_empty_custom_error("Gust Factor, G") == \
        "Error: The custom value for 'Gust Factor, G' cannot be empty."


def test_real_schema_covers_all_mode_line_fields():
    pytest.importorskip("PySide6")
    from osdagbridge.core.bridge_types.plate_girder.ui_fields_additional_input import ADDITIONAL_INPUTS_SCHEMA
    specs = v.build_custom_input_specs(ADDITIONAL_INPUTS_SCHEMA)
    mode_line_specs = [s for s in specs if s.trigger_name.endswith(v.MODE_SUFFIX)]
    assert len(mode_line_specs) >= 13
    assert all(s.label and "<" not in s.label for s in specs)
