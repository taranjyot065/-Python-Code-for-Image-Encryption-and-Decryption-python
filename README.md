🔐 Python Code for Image Encryption and Decryption

🛠️ How It Works
The image is read using Pillow.

Each pixel’s RGB values are XOR’ed with a user-provided key (0–255).

XOR is symmetric: applying the same operation twice with the same key returns the original value — this enables both encryption and decryption.

✅ Example Usage
Encrypt:

Use any image (e.g., sample.jpg)

Choose a key (e.g., 123)

Output: encrypted.jpg

Decrypt:

Use encrypted.jpg as input

Use the same key (123)

Output: decrypted.jpg (which will match the original)

Let me know if you'd like:

A GUI version using tkinter

Drag-and-drop support

Saving the key in a file for reuse
