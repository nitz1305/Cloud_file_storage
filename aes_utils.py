from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# Generate AES key
def generate_key():
    return get_random_bytes(16)

# Pad data
def pad(data):
    while len(data) % 16 != 0:
        data += b' '
    return data

# Encrypt file
def encrypt_file(file_data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_data = pad(file_data)
    encrypted = cipher.encrypt(padded_data)
    return encrypted

# Decrypt file
def decrypt_file(encrypted_data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(encrypted_data)
    return decrypted.rstrip()