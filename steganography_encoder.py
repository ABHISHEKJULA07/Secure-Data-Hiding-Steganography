import cv2
import numpy as np

def encode_message(image_path, message, output_path):
    image = cv2.imread(image_path)
    binary_msg = ''.join(format(ord(char), '08b') for char in message) + '1111111111111110'  # Delimiter

    msg_index = 0
    for row in image:
        for pixel in row:
            for i in range(3):  # Modify RGB channels
                if msg_index < len(binary_msg):
                    pixel[i] = (pixel[i] & ~1) | int(binary_msg[msg_index])
                    msg_index += 1

    cv2.imwrite(output_path, image)
    print("Message encoded successfully in", output_path)

# Example usage
# encode_message("sample.jpg", "Secret Message", "encrypted_image.png")
