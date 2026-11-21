"""GUI tests (offscreen) for Additional Inputs: Custom validation and unsaved-changes warning.

These build the real AdditionalInputs dialog. Only the popup (CustomMessageBox) is replaced
by a recorder, so nothing blocks; all validation / state logic under test is the real code.
"""
import os

import pytest

pytest.importorskip("PySide6")
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtWidgets import QApplication, QComboBox, QLineEdit  # noqa: E402

import osdagbridge.desktop.ui.dialogs.additional_input.additional_inputs as ai_module  # noqa: E402
from osdagbridge.core.bridge_types.plate_girder.defaults import (  # noqa: E402
    BASIC_INPUT_DICT, solve_extend_basic_input_dict,
)
from osdagbridge.core.utils.common import (  # noqa: E402
    KEY_SPAN, KEY_CARRIAGEWAY_WIDTH, KEY_WL_GUST_FACTOR, KEY_WL_DRAG_COEFF, KEY_CB_TYPE, KEY_CB_WIDTH,
)

UNSAVED_TEXT = "You have unsaved changes. Closing this window will discard them. Do you want to proceed?"


def _make_dict():
    data = dict(BASIC_INPUT_DICT)
    data[KEY_SPAN] = 20
    data[KEY_CARRIAGEWAY_WIDTH] = 5
    solve_extend_basic_input_dict(data)
    return data


@pytest.fixture(scope="module")
def qapp():
    return QApplication.instance() or QApplication([])


@pytest.fixture
def env(qapp, monkeypatch):
    popups, answers = [], {"discard": "Cancel"}

    class RecordingBox:
        def __init__(self, title="", text="", informativeText="", buttons=("OK",), dialogType=None):
            self.title, self.text, self.buttons = title, text, list(buttons)

        def exec(self):
            popups.append((self.title, self.text, self.buttons))
            return answers["discard"] if "Discard" in self.buttons else "OK"

    monkeypatch.setattr(ai_module, "CustomMessageBox", RecordingBox)
    dlg = ai_module.AdditionalInputs()
    saved = []
    dlg.update_template_page_2d_cad.connect(lambda params: saved.append(params))
    dlg.set_input_dictionary(_make_dict())
    dlg.show()
    yield dlg, popups, answers, saved
    dlg.is_modified = False
    dlg.close()


def _combo(dlg, key):
    return dlg.findChild(QComboBox, key)


def _line(dlg, key):
    return dlg.findChild(QLineEdit, key)


def test_fresh_dialog_is_not_modified(env):
    dlg, *_ = env
    assert dlg.is_modified is False


def test_empty_custom_mode_line_blocks_save_with_named_error(env):
    dlg, popups, _, saved = env
    _combo(dlg, KEY_WL_GUST_FACTOR + ".mode").setCurrentText("Custom")
    _line(dlg, KEY_WL_GUST_FACTOR + ".value").setText("")
    popups.clear()
    dlg._save_inputs()
    assert saved == []
    assert [p[0] for p in popups] == ["Error"]
    assert "Error: The custom value for 'Gust Factor, G' cannot be empty." in popups[0][1]
    assert dlg.is_modified is True


def test_all_empty_custom_fields_are_listed(env):
    dlg, popups, *_ = env
    for key in (KEY_WL_GUST_FACTOR, KEY_WL_DRAG_COEFF):
        _combo(dlg, key + ".mode").setCurrentText("Custom")
    popups.clear()
    dlg._save_inputs()
    text = popups[0][1]
    assert "Gust Factor, G" in text and "Drag Coefficient, CD" in text


def test_empty_custom_crash_barrier_width_blocks_save(env):
    dlg, popups, _, saved = env
    _combo(dlg, KEY_CB_TYPE).setCurrentText("Custom")
    _line(dlg, KEY_CB_WIDTH).setText("")
    popups.clear()
    dlg._save_inputs()
    assert saved == [] and popups and popups[0][0] == "Error"
    assert "cannot be empty" in popups[0][1]


def test_valid_custom_saves_and_resets_modified(env):
    dlg, popups, _, saved = env
    _combo(dlg, KEY_WL_GUST_FACTOR + ".mode").setCurrentText("Custom")
    edit = _line(dlg, KEY_WL_GUST_FACTOR + ".value")
    edit.setText("2.0")
    edit.editingFinished.emit()
    popups.clear()
    dlg._save_inputs()
    assert [p[0] for p in popups] == ["Saved"]
    assert len(saved) == 1
    assert dlg.is_modified is False


def test_no_warning_when_closing_unmodified_or_after_save(env):
    dlg, popups, *_ = env
    popups.clear()
    dlg.close()
    assert not dlg.isVisible()
    assert not any("Discard" in p[2] for p in popups)


def test_cancel_keeps_dialog_and_values_discard_closes(env):
    dlg, popups, answers, _ = env
    combo = _combo(dlg, KEY_WL_GUST_FACTOR + ".mode")
    combo.setCurrentText("Custom")
    assert dlg.is_modified is True

    popups.clear()
    answers["discard"] = "Cancel"
    dlg.close()
    assert [p[1] for p in popups if "Discard" in p[2]] == [UNSAVED_TEXT]
    assert dlg.isVisible() and combo.currentText() == "Custom" and dlg.is_modified is True

    answers["discard"] = "Discard"
    dlg.close()
    assert not dlg.isVisible()
    assert dlg.is_modified is False


def test_escape_path_also_warns(env):
    dlg, popups, answers, _ = env
    _combo(dlg, KEY_WL_GUST_FACTOR + ".mode").setCurrentText("Custom")
    answers["discard"] = "Cancel"
    popups.clear()
    dlg.reject()
    assert any("Discard" in p[2] for p in popups)
    assert dlg.isVisible()


def test_reopen_after_discard_restores_saved_values(env):
    dlg, _, answers, _ = env
    _combo(dlg, KEY_WL_GUST_FACTOR + ".mode").setCurrentText("Custom")
    answers["discard"] = "Discard"
    dlg.close()
    dlg.set_input_dictionary(_make_dict())
    dlg.show()
    assert _combo(dlg, KEY_WL_GUST_FACTOR + ".mode").currentText() != "Custom"
    assert dlg.is_modified is False
