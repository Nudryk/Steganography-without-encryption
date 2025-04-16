# Steganography Tool - Hide and Extract Messages in Images

This Python tool allows you to hide messages inside images (image steganography) and later extract those hidden messages. It supports two main operations:

1. **Embedding a message into an image**
2. **Extracting a hidden message from an image**

The messages are hidden by modifying the least significant bits of the RGB values of the image pixels, making it almost impossible to detect visually.

## Features

- **Embed a Message:** Embed a message into an image file.
- **Extract a Message:** Extract a hidden message from a steganographed image.
- **Support for PNG and JPEG Images.**

## Requirements

- Python 3.x
- Pillow library (Python Imaging Library fork)

You can install the required libraries using:

```bash
pip install pillow
