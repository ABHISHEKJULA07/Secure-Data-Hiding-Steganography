# Secure-Data-Hiding-Steganography
A Python-based image steganography project for secure data hiding using LSB technique.
# Secure Data Hiding in Image Using Steganography

## 🔍 Overview
This project implements **image steganography** to securely hide and retrieve secret messages inside an image using **Least Significant Bit (LSB) encoding**. It ensures that the hidden data remains undetectable while maintaining image quality.

## 🚀 Features
- **Secure Message Embedding**: Hide a secret message inside an image without noticeable distortion.
- **Password Protection**: Optional encryption before embedding for enhanced security.
- **Easy Message Extraction**: Retrieve the hidden message using the decryption algorithm.
- **Supports Multiple Image Formats**: Works with **JPG, PNG, BMP** formats.
- **Lightweight & Efficient**: Uses Python and OpenCV for optimized performance.

## 🛠️ Technologies Used
- **Programming Language**: Python
- **Libraries**: OpenCV, NumPy, PIL (Pillow)
- **Concepts**: LSB Steganography, Image Processing

## 📂 Project Structure
```
Secure-Data-Hiding-Steganography/
│-- encrypt.py   # Script to hide message in an image
│-- decrypt.py   # Script to extract hidden message
│-- sample_image.png  # Example image for testing
│-- README.md  # Documentation
```

## 🔧 Installation & Usage
### **1️⃣ Install Dependencies**
Ensure Python 3.x is installed, then run:
```bash
pip install opencv-python numpy pillow
```

### **2️⃣ Encrypt (Hide a Message)**
```bash
python encrypt.py --image sample_image.png --message "Secret text" --output encrypted.png
```

### **3️⃣ Decrypt (Retrieve Message)**
```bash
python decrypt.py --image encrypted.png
```

## 📌 Example
**Original Image** → **Encrypted Image (visually unchanged)** → **Message Retrieved**

## 🎯 Applications
- **Cybersecurity**: Secure messaging and confidential data transmission.
- **Digital Watermarking**: Embedding ownership details in images.
- **Forensics**: Hiding sensitive information in media files.

- ## 👨‍💻 Developed By

**Abhishek Jula** 
🔗 [LinkedIn](https://www.linkedin.com/in/abhi-jula0711)  
💻 [GitHub](https://github.com/ABHISHEKJULA07)  
🌐 [Portfolio](https://abhipinku66.wixsite.com/07112000)  
📧 abhishekjula018@gmail.com

## 🔮 Future Scope
- Implementing **AES encryption** before embedding data.
- Extending to **video and audio steganography**.
- Developing a **GUI-based tool** for user-friendly interaction.


