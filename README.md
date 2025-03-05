# qute-translate

This Python script allows you to quickly translate selected text in the Qutebrowser browser into a target language (default is Russian) and display the result in a separate window using the Tkinter graphical interface.

## Key Features

- **Text Translation**: The script uses the `trans` utility (from the [translate-shell](https://github.com/soimort/translate-shell) package) to translate selected text into the target language.
- **Graphical Interface**: The translated text is displayed in a separate window with scroll functionality.
- **Hotkeys**:
  - `j` — Scroll down.
  - `k` — Scroll up.
  - `gg` — Scroll to the top of the text.
  - `G` — Scroll to the bottom of the text.
  - `q` — Close the window.

## Installation and Usage

1. Ensure you have the following installed:
   - Python 3.x
   - Tkinter (usually included in Python's standard library)
   - The `trans` utility (translate-shell)

2. Copy the script to your Qutebrowser userscripts directory (usually located in the Qutebrowser configuration directory). Then make it executable:
   ```bash
   chmod +x ~/.config/qutebrowser/userscripts/qute-translate.py
   ```

3. Configure Qutebrowser to use the script. For example, add the following to the `config.py` configuration file:
   ```python
   config.bind(',t', 'spawn --userscript qute-translate.py', mode='normal')
   config.bind('t', 'spawn --userscript qute-translate.py', mode='caret')
   ```

4. Highlight text in Qutebrowser and press the hotkey (e.g., `,t`). The translated text will appear in a new window.

## Customization

- **Target Language**: Change the `TARGET_LANG` variable to the desired language (e.g., "es" for Spanish).
- **Appearance**: Modify the `BG_COLOR`, `FG_COLOR`, `FONT`, and `GEOMETRY` variables to customize the window's appearance.

## Example Usage

1. Highlight text in Qutebrowser.
2. Press the hotkey (e.g., `,t`).
3. The translated text will appear in a new window. Use the hotkeys to navigate.

## Dependencies

- Python 3.x
- Tkinter
- translate-shell (`trans`)
