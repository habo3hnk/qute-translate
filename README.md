# qute-translate

This Python script allows you to quickly translate selected text in the Qutebrowser browser into a target language (default is Russian) and display the result in a separate window using the PyQt6 graphical interface.

![example](media/example.gif)
## Main Features

- **Text Translation**: The script uses the unofficial Google Translate API to translate selected text into the target language.
- **Graphical Interface**: The translated text is displayed in a frameless window with scroll functionality.
- **Hotkeys**:
  - `j` — Scroll down.
  - `k` — Scroll up.
  - `g` — Scroll to the beginning of the text.
  - `G` — Scroll to the end of the text.
  - `q` — Close the window.

## Installation and Usage

1. Ensure you have the following components installed:
   - Python 3.x
   - PyQt6 (`pip install PyQt6`)
   - `requests` library (`pip install requests`)

2. Copy the script to the Qutebrowser userscripts directory (usually located in the Qutebrowser configuration directory). Then make it executable:
   ```bash
   chmod +x ~/.config/qutebrowser/userscripts/qute-translate.py
   ```

3. Configure Qutebrowser to use the script. For example, add the following lines to the `config.py` configuration file:
   ```python
   config.bind(',t', 'spawn --userscript qute-translate.py', mode='normal')
   config.bind('t', 'spawn --userscript qute-translate.py', mode='caret')
   ```

4. Select text in Qutebrowser and press the hotkey (e.g., `,t`). The translated text will appear in a new window.

## Configuration

- **Target Language**: Change the `TARGET_LANG` variable to the desired language (e.g., "es" for Spanish).
- **Appearance**: Adjust the `BG_COLOR`, `FG_COLOR`, `FONT`, `FONT_SIZE`, and `GEOMETRY` variables to customize the window's appearance.

## Example Usage

1. Select text in Qutebrowser.
2. Press the hotkey (e.g., `,t`).
3. The translated text will appear in a new window. Use the hotkeys for navigation.

## Dependencies

- Python 3.x
- PyQt6 (`pip install PyQt6`)
- `requests` library (`pip install requests`)

---

### Script Updates

The script has been updated to use **PyQt6** for the graphical interface and the **unofficial Google Translate API** for translation. Here are the main changes:

#### Key Changes:
- **Graphical Interface**: Tkinter has been replaced with PyQt6.
- **Translation Method**: The script now uses the unofficial Google Translate API via the endpoint `https://translate.googleapis.com/translate_a/single`.
- **Hotkeys**: Convenient hotkeys for scrolling and closing the window have been added.

---------------------------------
### Notes:
- **Unofficial API**: The script uses an unofficial Google Translate endpoint, which may be restricted or blocked by Google.
