import cv2
import numpy as np

def encode_message(image_path, message, output_path):
    """Encodes a hidden message into an image using LSB steganography."""
    image = cv2.imread(image_path)
    binary_msg = ''.join(format(ord(char), '08b') for char in message) + '1111111111111110'  # End delimiter

    msg_index = 0
    for row in image:
        for pixel in row:
            for i in range(3):  # Modify RGB channels
                if msg_index < len(binary_msg):
                    pixel[i] = (pixel[i] & ~1) | int(binary_msg[msg_index])
                    msg_index += 1

    cv2.imwrite(output_path, image)
    print("Message encoded successfully in", output_path)

def decode_message(image_path):
    """Decodes the hidden message from an image using LSB steganography."""
    image = cv2.imread(image_path)
    binary_msg = ""

    for row in image:
        for pixel in row:
            for i in range(3):  
                binary_msg += str(pixel[i] & 1)

    binary_chars = [binary_msg[i:i+8] for i in range(0, len(binary_msg), 8)]
    message = ''.join(chr(int(char, 2)) for char in binary_chars if int(char, 2) != 254)  # Stop at delimiter
    print("Decoded Message:", message)

# Example usage
if __name__ == "__main__":
    # Encoding
    encode_message("sample.jpg", "Hello, this is a secret!", "encoded_image.png")

    # Decoding
    decode_message("encoded_image.png")
