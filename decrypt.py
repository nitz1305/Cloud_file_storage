from aes_utils import decrypt_file

# Read AES key
with open("encrypted_files/sample.key", "rb") as f:
    key = f.read()

# Read encrypted file
with open("encrypted_files/sample.enc", "rb") as f:
    data = f.read()

nonce = data[:16]
ciphertext = data[16:]

original_data = decrypt_file(key, nonce, ciphertext)

# Save decrypted file
with open("decrypted_files/sample.txt", "wb") as f:
    f.write(original_data)

print("File decrypted successfully")
