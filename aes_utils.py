from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt_file(data):
    key = get_random_bytes(16)      # Create AES key
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return key, cipher.nonce, ciphertext

def decrypt_file(key, nonce, ciphertext):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt(ciphertext)
