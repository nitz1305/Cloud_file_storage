from aes_utils import decrypt_file

# Read encrypted file
with open("encrypted.bin", "rb") as f:
    encrypted_data = f.read()

# Read key
with open("key.key", "rb") as f:
    key = f.read()

# Decrypt
decrypted_data = decrypt_file(encrypted_data, key)

# Save decrypted file
with open("decrypted.txt", "wb") as f:
    f.write(decrypted_data)

print("Decryption complete.")