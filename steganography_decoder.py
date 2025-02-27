import cv2
import numpy as np

def decode_message(image_path):
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
# decode_message("encrypted_image.png")
