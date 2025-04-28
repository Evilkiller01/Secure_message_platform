from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import base64
import os

# === LOAD OR CREATE SHARED SECRET KEY ===
KEY_FILE = "secret.key"
if os.path.exists(KEY_FILE):
    with open(KEY_FILE, "rb") as f:
        key = f.read()
else:
    key = get_random_bytes(16)
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    print("Generated and saved new secret key.")

# === ENCRYPT MESSAGE ===
message = input("Enter your message: ")
iv = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))

# === COMBINE IV + CIPHERTEXT AND ENCODE ===
combined = base64.b64encode(iv + ciphertext).decode()

print("\n--- ENCRYPTED MESSAGE TO SEND ---")
print(combined)
