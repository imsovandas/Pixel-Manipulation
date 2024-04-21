import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os
import sys

def encrypt_image(image_path):
    if image_path:
        image = Image.open(image_path)
        width, height = image.size

        # Iterate through each pixel and swap RGB values
        for x in range(width):
            for y in range(height):
                r, g, b = image.getpixel((x, y))
                image.putpixel((x, y), (g, b, r))  # Swapping RGB values

        encrypted_image_path = image_path.split('.')[0] + "_encrypted.png"
        image.save(encrypted_image_path)
        print("------------------------- ")
        print("Image encrypted successfully. \n")
        print(f"Encrypted image saved as: {encrypted_image_path} \n ")

def decrypt_image(image_path):
    if image_path:
        image = Image.open(image_path)
        width, height = image.size

        # Iterate through each pixel and swap RGB values back to original
        for x in range(width):
            for y in range(height):
                r, g, b = image.getpixel((x, y))
                image.putpixel((x, y), (b, r, g))  # Swapping RGB values back to original

        decrypted_image_path = image_path.split('_encrypted')[0] + "_decrypted.png"
        image.save(decrypted_image_path)
        print("------------------------- ")
        print("Image decrypted successfully. \n")
        print(f"Decrypted image saved as : {decrypted_image_path} \n")

def main():
    print("\n------------------------- ")
    print("Pixel Manipulation for Image Encryption By Sovan Das")
    print("------------------------- ")
    print("Choose Your Options \n1. Encryption \n2. Decryption \n")

    # Get user's choice
    choice = int(input("Enter Your Choice (1 or 2): "))

    # Get image path
    image_path = input("Enter the path of an image: ")

    if choice == 1:
        encrypt_image(image_path)
    elif choice == 2:
        decrypt_image(image_path)
    else:
        print("Invalid choice. Please choose either 1 or 2.")

if __name__ == "__main__":
    main()