from aes_utils import encrypt_file

# Read original file
with open("original_files/sample.txt", "rb") as f:
    data = f.read()

key, nonce, encrypted_data = encrypt_file(data)

# Save encrypted file
with open("encrypted_files/sample.enc", "wb") as f:
    f.write(nonce + encrypted_data)

# Save AES key
with open("encrypted_files/sample.key", "wb") as f:
    f.write(key)

print("File encrypted successfully")
