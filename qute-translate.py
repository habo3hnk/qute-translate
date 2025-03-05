#!/usr/bin/env python

import os
import subprocess
import sys
import tkinter as tk
from tkinter import ttk


TARGET_LANG = "ru"
BG_COLOR = "#1a1b26"
FG_COLOR = "#ffffff"
FONT = ("JetBrainsMono Nerd Font", 12)
GEOMETRY = "400x300"


class TranslatedWindow:
    def __init__(self, root):
        self.root = root
        self.root.geometry(GEOMETRY)

        self.root.bind("j", self.scroll_down)
        self.root.bind("k", self.scroll_up)
        self.root.bind("q", self.close_window)
        self.root.bind("gg", self.scroll_to_top)
        self.root.bind("G", self.scroll_to_bottom)

        self.frame = ttk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.text = tk.Text(self.frame, wrap=tk.WORD, padx=10, pady=10)
        self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.text.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.text.config(
            yscrollcommand=self.scrollbar.set,
            font=FONT,
            fg=FG_COLOR,
            bg=BG_COLOR
        )

    def scroll_down(self, event):
        self.text.yview_scroll(1, tk.UNITS)

    def scroll_up(self, event):
        self.text.yview_scroll(-1, tk.UNITS)

    def scroll_to_top(self, event):
        self.text.yview_moveto(0.0)

    def scroll_to_bottom(self, event):
        self.text.yview_moveto(1.0)

    def close_window(self, event):
        self.root.destroy()

    def add_text(self, translated_text):
        self.text.insert(tk.END, translated_text)


def get_translation(text):
    try:
        result = subprocess.run(
            ["trans", "-b", f":{TARGET_LANG}", text],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip("\n").strip()
        return result

    except subprocess.CalledProcessError as e:
        sys.exit(0)


def main():
    root = tk.Tk()
    app = TranslatedWindow(root)

    selected_text = os.getenv("QUTE_SELECTED_TEXT", "")

    translated_text = get_translation(selected_text)

    if translated_text:
        app.add_text(translated_text)
        root.mainloop()
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()

