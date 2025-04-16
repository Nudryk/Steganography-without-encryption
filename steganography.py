import argparse
from PIL import Image
import os

# --- Fonctions Steganographie ---

def message_to_bits(message):
    return ''.join(format(ord(char), '08b') for char in message) + '1111111111111110'

def bits_to_message(bits):
    chars = [bits[i:i+8] for i in range(0, len(bits), 8)]
    message = ''
    for char in chars:
        if char == '11111110':
            break
        message += chr(int(char, 2))
    return message.replace("ÿ", "")

def embed_message(image_path, output_path, message):
    img = Image.open(image_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    pixels = list(img.getdata())
    
    bits = message_to_bits(message)
    if len(bits) > len(pixels) * 3:
        raise ValueError("Message is too long to hide in this image.")

    new_pixels = []
    bit_idx = 0
    for pixel in pixels:
        r, g, b = pixel
        if bit_idx < len(bits):
            r = (r & ~1) | int(bits[bit_idx])
            bit_idx += 1
        if bit_idx < len(bits):
            g = (g & ~1) | int(bits[bit_idx])
            bit_idx += 1
        if bit_idx < len(bits):
            b = (b & ~1) | int(bits[bit_idx])
            bit_idx += 1
        new_pixels.append((r, g, b))

    img.putdata(new_pixels)
    img.save(output_path)

def extract_message(image_path):
    img = Image.open(image_path)
    pixels = list(img.getdata())

    bits = ''
    for pixel in pixels:
        for color in pixel[:3]:
            bits += str(color & 1)

    return bits_to_message(bits)

# --- Fonction principale pour CLI ---

def main():
    parser = argparse.ArgumentParser(description="Steganography Tool - Hide and Extract Messages in Images")
    subparsers = parser.add_subparsers(dest="command")

    # Subcommand: Embed
    embed_parser = subparsers.add_parser('embed', help="Embed a message in an image")
    embed_parser.add_argument('image', help="Path to the input image")
    embed_parser.add_argument('output', help="Path to save the output image")
    embed_parser.add_argument('message', help="Message to embed in the image")

    # Subcommand: Extract
    extract_parser = subparsers.add_parser('extract', help="Extract a hidden message from an image")
    extract_parser.add_argument('image', help="Path to the image with hidden message")

    args = parser.parse_args()

    if args.command == 'embed':
        try:
            embed_message(args.image, args.output, args.message)
            print(f"Message successfully embedded into {args.output}")
        except Exception as e:
            print(f"Error: {str(e)}")

    elif args.command == 'extract':
        try:
            message = extract_message(args.image)
            print(f"Extracted message: {message}")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
