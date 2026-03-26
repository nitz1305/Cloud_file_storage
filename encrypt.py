from aes_utils import generate_key, encrypt_file

# Read file
with open("sample.txt", "rb") as f:
    data = f.read()

# Generate key
key = generate_key()

# Encrypt
encrypted_data = encrypt_file(data, key)

# Save encrypted file
with open("encrypted.bin", "wb") as f:
    f.write(encrypted_data)

# Save key
with open("key.key", "wb") as f:
    f.write(key)

print("Encryption complete. Files saved.")