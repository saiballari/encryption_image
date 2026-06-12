# encryption_image
# Image Encryption using Pixel Manipulation in Python

## Overview

This project is a simple Image Encryption tool built using Python and the Pillow (PIL) library. It secures images by modifying the RGB values of each pixel using a secret key and swapping pixel positions horizontally. The encrypted image appears distorted and unreadable, providing a basic demonstration of image encryption techniques.

## Features

* Encrypt images using a user-defined key.
* Modify RGB values using a mathematical operation.
* Swap pixel positions horizontally for additional image distortion.
* Simple and beginner-friendly implementation.
* Demonstrates basic image security concepts.

## Technologies Used

* Python
* Pillow (PIL) Library

## How It Works

### Encryption

Each pixel's Red, Green, and Blue (RGB) values are increased by the secret key value and wrapped within the range 0–255 using the modulo operator. After modifying the RGB values, pixels are swapped horizontally across the image to further distort its appearance.

## Installation

1. Install Python.
2. Install Pillow:
   pip install pillow

## Usage

1. Place the image file (`img.jpg`) in the project folder.
2. Run the program:
   python image_encrypt.py
3. Enter the encryption key when prompted.
4. The encrypted image will be saved automatically as:

   * encrypted.png

## Example

* Original Image: img.jpg
* Encrypted Image: encrypted.png

## Learning Outcomes

* Understanding image processing basics.
* Working with pixel manipulation techniques.
* Using mathematical operations on image data.
* Implementing a simple image encryption concept.
* Using Python libraries for multimedia applications.

## Future Improvements

* Add image decryption functionality.
* Implement password-based encryption.
* Support multiple image formats.
* Create a GUI using Tkinter.
* Use stronger encryption algorithms for enhanced security.

##Screenshots

##image
![IMAGE](image.jpg)

##Encripted Image
![Encripted Image](encrypted.png)

## Author

Sai Ballari
Cybersecurity, Blockchain & IoT (CIC)
