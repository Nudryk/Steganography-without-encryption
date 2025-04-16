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

## Usage
Command-line Interface (CLI)
You can interact with the tool via the command line with the following subcommands:

1. Embed a message in an image

```bash
python steganography.py embed <image_path> <output_image_path> "<message>"

<image_path>: Path to the input image where the message will be embedded.

<output_image_path>: Path where the resulting image with the embedded message will be saved.

<message>: The message you want to hide in the image.
