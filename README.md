# QR Code Generator (Python)

A simple terminal-based QR Code Generator built using Python.

This program allows users to enter text or a URL, customize QR code colors, and generate a QR code image saved as a PNG file with a unique timestamped filename.

---

## Features

* Generate QR codes from text or URLs
* Custom QR code color selection
* Custom background color selection
* Automatic timestamped filenames to prevent overwriting
* Input validation for empty data
* Saves QR codes as PNG images
* Displays the saved file name after generation
* Beginner-friendly and easy to modify

---

## Technologies Used

* Python 3
* qrcode
* Pillow (PIL)

---

## Installation

### 1. Verify Python Installation

```bash
python --version
```

### 2. Install Required Libraries

```bash
python -m pip install qrcode pillow
```

---

## Usage

Run the program:

```bash
python qr_generator.py
```

Example:

```text
Enter text or URL to generate QR code: https://example.com
Enter file name (without extension): website
Enter QR color (default: black): blue
Enter background color (default: white): white
```

Output:

```text
QR Code generated successfully.
Saved as: website_20260603_143210.png


## Future Improvements

* Logo embedding
* Batch QR code generation
* QR code history log
* Automatic output folder creation
* GUI version using Tkinter
* QR code scanner integration

---

## License

This project is free to use, modify, and distribute for educational and personal projects.
