#!/usr/bin/env python

import os
import subprocess
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
        if obj == self.text_edit and event.type() == event.Type.KeyPress:
            key = event.key()
            if key == Qt.Key.Key_J:
                self.text_edit.verticalScrollBar().setValue(
                    self.text_edit.verticalScrollBar().value() + 20
                )
            elif key == Qt.Key.Key_K:
                self.text_edit.verticalScrollBar().setValue(
                    self.text_edit.verticalScrollBar().value() - 20
                )
            elif key in [Qt.Key.Key_Q, Qt.Key.Key_Escape]:
                self.close()
            elif (
                key == Qt.Key.Key_G
                and event.modifiers() == Qt.KeyboardModifier.NoModifier
            ):
                self.text_edit.verticalScrollBar().setValue(
                    self.text_edit.verticalScrollBar().minimum()
                )
            elif (
                key == Qt.Key.Key_G
                and event.modifiers() == Qt.KeyboardModifier.ShiftModifier
            ):
                self.text_edit.verticalScrollBar().setValue(
                    self.text_edit.verticalScrollBar().maximum()
                )
            return True
        return super().eventFilter(obj, event)

    def add_text(self, translated_text):
        self.text_edit.setPlainText(translated_text)


def extract_translated_text(data):
    return " ".join(
        item[0] for item in data[0] if isinstance(item, list) and len(item) > 1
    )


def main():
    app = QApplication(sys.argv)

    subprocess.run(
        ["notify-send", "-u", "low", "qute-translate", "The text translation begins."]
    )

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

    response = requests.get(URL, params=params)
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
