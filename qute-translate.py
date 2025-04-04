#!/usr/bin/env python

import sh
import os
import sys
import requests
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

TARGET_LANG = "ru"
BG_COLOR = "#1a1b26"
FG_COLOR = "#ffffff"
FONT = "JetBrainsMono Nerd Font"
FONT_SIZE = 12
GEOMETRY = (400, 300)
URL = "https://translate.googleapis.com/translate_a/single"


class TranslatedWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setWindowTitle("Translated Text")
        self.setGeometry(0, 0, *GEOMETRY)

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.text_edit.setFont(QFont(FONT, FONT_SIZE))
        self.text_edit.installEventFilter(self)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.text_edit)
        self.setCentralWidget(central_widget)

        self.setStyleSheet(f"background-color: {BG_COLOR}; color: {FG_COLOR};")

    def eventFilter(self, obj, event):
        if obj != self.text_edit or event.type() != event.Type.KeyPress:
            return super().eventFilter(obj, event)

        key = event.key()
        modifiers = event.modifiers()

        key_actions = {
            (Qt.Key.Key_J, Qt.KeyboardModifier.NoModifier): self.scroll_down,
            (Qt.Key.Key_K, Qt.KeyboardModifier.NoModifier): self.scroll_up,
            (Qt.Key.Key_Q, Qt.KeyboardModifier.NoModifier): self.close_window,
            (Qt.Key.Key_Escape, Qt.KeyboardModifier.NoModifier): self.close_window,
            (Qt.Key.Key_G, Qt.KeyboardModifier.NoModifier): self.scroll_to_top,
            (Qt.Key.Key_G, Qt.KeyboardModifier.ShiftModifier): self.scroll_to_bottom,
        }

        action = key_actions.get((key, modifiers))
        if action:
            action()
            return True

        return super().eventFilter(obj, event)

    def scroll_down(self):
        scroll_bar = self.text_edit.verticalScrollBar()
        if scroll_bar:
            scroll_bar.setValue(scroll_bar.value() + 20)
        else:
            print("Scroll bar not found")

    def scroll_up(self):
        scroll_bar = self.text_edit.verticalScrollBar()
        if scroll_bar:
            scroll_bar.setValue(scroll_bar.value() - 20)
        else:
            print("Scroll bar not found")

    def scroll_to_top(self):
        scroll_bar = self.text_edit.verticalScrollBar()
        if scroll_bar:
            scroll_bar.setValue(scroll_bar.minimum())
        else:
            print("Scroll bar not found")

    def scroll_to_bottom(self):
        scroll_bar = self.text_edit.verticalScrollBar()
        if scroll_bar:
            scroll_bar.setValue(scroll_bar.maximum())
        else:
            print("Scroll bar not found")

    def close_window(self):
        self.close()

    def add_text(self, translated_text):
        self.text_edit.setPlainText(translated_text)


def extract_translated_text(data):
    return " ".join(
        item[0] for item in data[0] if isinstance(item, list) and len(item) > 1
    )


def main():
    app = QApplication(sys.argv)

    sh.notify_send("-u", "low", "qute-translate", "The text translation begins.")

    selected_text = os.getenv("QUTE_SELECTED_TEXT", "")
    if not selected_text:
        sys.exit(0)

    params = {
        "client": "gtx",
        "sl": "auto",
        "tl": TARGET_LANG,
        "dt": "t",
        "q": selected_text,
    }

    response = requests.get(URL, params=params, timeout=10)
    if response.status_code != 200:
        sys.exit(0)

    translated_text = extract_translated_text(response.json())
    if translated_text:
        window = TranslatedWindow()
        window.add_text(translated_text)
        window.show()
        sys.exit(app.exec())

    sys.exit(0)


if __name__ == "__main__":
    main()
