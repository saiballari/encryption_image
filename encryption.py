from PIL import Image

def encrypt_image(input_image, output_image, key):
    img = Image.open(input_image)
    pixels = img.load()

    width, height = img.size

    # Modify RGB values
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256

            pixels[x, y] = (r, g, b)

    # Swap pixels horizontally
    for y in range(height):
        for x in range(width // 2):
            pixels[x, y], pixels[width - x - 1, y] = (
                pixels[width - x - 1, y],
                pixels[x, y]
            )

    img.save(output_image)
    print("Image encrypted successfully!")

# Main Program
key = int(input("Enter encryption key: "))
encrypt_image("img.jpg", "encrypted.png", key)