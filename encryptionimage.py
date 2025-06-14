from PIL import Image
import os

def encrypt_decrypt_image(input_path, output_path, key):
    # Open image
    image = Image.open(input_path)
    image = image.convert("RGB")  # Ensure it's in RGB mode

    # Load pixel data
    pixels = image.load()

    # Process each pixel
    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]
            # XOR each color channel with the key
            pixels[i, j] = (r ^ key, g ^ key, b ^ key)

    # Save the new image
    image.save(output_path)
    print(f"Processed image saved at: {output_path}")

def main():
    print("=== Image Encryptor / Decryptor ===")
    input_file = input("Enter path to image file: ")
    output_file = input("Enter path to save encrypted/decrypted image: ")
    try:
        key = int(input("Enter numeric key (0-255): "))
        if not (0 <= key <= 255):
            raise ValueError("Key must be in range 0-255.")
    except ValueError as e:
        print("Invalid key:", e)
        return

    if not os.path.exists(input_file):
        print("Error: Input file does not exist.")
        return

    encrypt_decrypt_image(input_file, output_file, key)

if __name__ == "__main__":
    main()
