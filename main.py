import hashlib
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# Colors for the terminal
CYAN = "\033[96m"
RESET = "\033[0m"

print(CYAN + "SHA-256 Hashing and AES Encryption" + RESET)
print()

# Ask the user for a message
message = input("Enter a message to encrypt: ")
message_bytes = message.encode("utf-8")

# Create the original SHA-256 hash
original_hash = hashlib.sha256(message_bytes).hexdigest()

print()
print(CYAN + "Original Message:" + RESET, message)
print(CYAN + "Original SHA-256 Hash:" + RESET, original_hash)

# Generate a random AES key and nonce
key = AESGCM.generate_key(bit_length=256)
nonce = os.urandom(12)

# Encrypt the message
aes = AESGCM(key)
encrypted_message = aes.encrypt(nonce, message_bytes, None)

print()
print(CYAN + "Encrypted Message (Hex):" + RESET)
print(encrypted_message.hex())

# Decrypt the message
decrypted_bytes = aes.decrypt(nonce, encrypted_message, None)
decrypted_message = decrypted_bytes.decode("utf-8")

print()
print(CYAN + "Decrypted Message:" + RESET, decrypted_message)

# Create a new hash from the decrypted message
decrypted_hash = hashlib.sha256(decrypted_bytes).hexdigest()

print(CYAN + "Decrypted SHA-256 Hash:" + RESET, decrypted_hash)

# Compare the two hashes
print()
if original_hash == decrypted_hash:
    print(CYAN + "Integrity Check:" + RESET, "PASSED")
    print("The original and decrypted hashes match.")
else:
    print(CYAN + "Integrity Check:" + RESET, "FAILED")
    print("The message may have been changed.")
