import cv2
import numpy as np

def encode_message(image_path, message, output_path):
    """Encodes a hidden message inside an image using LSB steganography."""
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found!")
        return

    binary_msg = ''.join(format(ord(char), '08b') for char in message) + '1111111111111110'  # Delimiter

    msg_index = 0
    for row in image:
        for pixel in row:
            for i in range(3):  # Modify R, G, B channels
                if msg_index < len(binary_msg):
                    pixel[i] = (pixel[i] & ~1) | int(binary_msg[msg_index])
                    msg_index += 1

    cv2.imwrite(output_path, image)
    print("Message encoded successfully in", output_path)

def decode_message(image_path):
    """Decodes and retrieves the hidden message from an image."""
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found!")
        return

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
    image_file = "sample.jpg"
    encoded_file = "encoded_image.png"
    secret_message = "This is a hidden message!"

    # Encoding process
    encode_message(image_file, secret_message, encoded_file)

    # Decoding process
    decode_message(encoded_file)
