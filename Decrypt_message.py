from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

# === LOAD SECRET KEY ===
with open("secret.key", "rb") as f:
    key = f.read()

# === INPUT ENCRYPTED MESSAGE ===
b64_input = input("Enter the encrypted message: ")
data = base64.b64decode(b64_input)

# === SPLIT IV AND CIPHERTEXT ===
iv = data[:16]
ciphertext = data[16:]

# === DECRYPT ===
cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

print("\n--- DECRYPTED MESSAGE ---")
print(plaintext.decode())
