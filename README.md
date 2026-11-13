# 🖌️ Custom-Font-Drawer

A custom lightweight character and typography rendering engine for NumWorks (MicroPython) supporting 115+ symbols, accents, variable sizing, and hex-compressed glyph data.

---

## ℹ️ Versions & Scripts

This repository contains both iterations of the custom font engine:

- **`lowercase_v2.py`** *(Recommended)* : Glyphs are stored with hexadecimal compression, drastically reducing RAM and flash footprint on the calculator while providing full rendering capabilities.
- **`lowercase_v1.py`** : The initial version storing raw binary patterns.

### 🔧 Glyph Converters (`converters/`)

The helper scripts used to build and compress the font glyph database from 2D integer matrices:

- **`converters/get_letters.py`** *(Created May 29, 2024)* : Converts a 2D binary integer array (`0`/`1` pixel matrix) into a semicolon-separated binary string (`v1` format).
- **`converters/bin_to_hex.py`** *(Created June 12, 2024)* : Encodes semicolon-separated binary glyph strings into the compact width-prefixed hexadecimal format used by `lowercase_v2.py`.

---

## 🚀 Usage

Import `write_string` and call it with your coordinates and parameters:

```python
from lowercase_v2 import write_string

# write_string(text, x, y, text_color, background_color, scale)
write_string("Hello World!", 10, 20, (0, 0, 0), (255, 255, 255), 1)
```

### Parameters
1. **text** : Text string to display on screen.
2. **x, y** : Pixel coordinates.
3. **color** *(optional)* : RGB text color (defaults to black).
4. **background** *(optional)* : RGB background color (`0` for transparent).
5. **scale** *(optional)* : Integer scaling multiplier (default: `1`).

---

## 🔤 Supported Characters (115+ symbols)

- Full Latin alphabet (lowercase & uppercase): `a-z`, `A-Z`
- Numbers: `0-9`
- 37 Special characters: `' " , : . ! ? ( ) % _ + - * / = [ ] { } < > ; π √ ~ ^ ∞ → | ° ± @ # & $ \`
- 16 French accented letters: `à â ä é è ê ë î ï ô ö ù û ü ÿ ç`
- Space
- Unknown characters fallback gracefully to a generic placeholder block (`▯`).

---

## 🖥️ Requirements & Environment

- Designed and optimized for the **NumWorks** calculator (**MicroPython**).
- Works with the standard `kandinsky` module (`fill_rect`).

---

## 🛠️ Details

The project has been created the November 20 of 2023.
