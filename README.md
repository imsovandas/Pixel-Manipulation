# Pixel Manipulation for Image Encryption
This Python script provides a simple tool for encrypting and decrypting images using pixel manipulation. It allows you to swap the RGB values of each pixel in an image to encrypt it and then revert the process to decrypt the image.

## Features
- Encryption: Encrypt images by swapping RGB values of each pixel.
- Decryption: Decrypt encrypted images by reversing the swapping process.
- Supports Various Image Formats: Works with popular image formats such as PNG, JPEG, and others supported by the PIL library.
- Easy-to-Use Command Line Interface: Simple command line interface for interacting with the tool.

## Requirements
- Python 3.x
- tkinter library
- PIL (Python Imaging Library)
## Usage
1. Clone the repository:
```
git clone https://github.com/imsovandas/PRODIGY_CS_04.git
```
2. Navigate to the repository directory:
```
cd PRODIGY_CS_04
```
3. Run the script:
```
python Pixel-Manipulation.py
```
4. Choose between encryption and decryption by entering 1 or 2.
5. Enter the path of the image file when prompted.
6. Once the process completes, the modified image will be saved in the same directory.
## Example
Encrypting an image:
```
Choose Your Options 
1. Encryption 
2. Decryption

Enter Your Choice (1 or 2): 1
Enter the path of an image: image.png
------------------------- 
Image encrypted successfully. 
Encrypted image saved as: image_encrypted.png
```
Decrypting an image:
```
Choose Your Options 
1. Encryption 
2. Decryption 

Enter Your Choice (1 or 2): 2
Enter the path of an image: image_encrypted.png
------------------------- 
Image decrypted successfully. 
Decrypted image saved as : image_decrypted.png
```
## Author
Linkdin : [Sovan Das](https://www.linkedin.com/in/sovanking)
