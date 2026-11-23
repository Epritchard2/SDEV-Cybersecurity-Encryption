# SHA-256 Hashing and AES Encryption

## About the Project

For this assignment, I created a Python program that takes a message from the user, hashes it using SHA-256, and encrypts it using AES. The program then decrypts the message and compares the hashes to make sure the original message wasn't changed.

## How It Works

The program asks the user to enter a message. It creates a SHA-256 hash of that message and then generates a random encryption key. After encrypting the message, it decrypts it and creates another hash. If both hashes match, the program displays an integrity check of PASSED.

## Confidentiality, Integrity, and Availability

Confidentiality: AES encryption protects the message by making it unreadable without the correct key.

Integrity: SHA-256 is used to compare the original and decrypted messages. If the hashes match, it shows that the message hasn't changed during the process. AES-GCM also checks for tampering when decrypting.

Availability: The program allows the user to encrypt and decrypt messages when it is running and the required information is available. It does not include features such as backups or recovery.

## Entropy and Key Generation

Entropy refers to randomness, which is important when creating encryption keys. If a key is predictable, it could be easier for someone to guess.

My program uses the cryptography library to generate a random 256-bit AES key. It also generates a random nonce for encryption. This helps make each encryption different, even when the same message is entered.

## Requirements

Python 3
cryptography library

Install the library using:

python -m pip install cryptography

Run the program using:

python main.py

## Testing

I tested the program using the message "Evan Pritchard" The program successfully encrypted and decrypted the message, and the integrity check passed.

## Video Demonstration

[Download my encryption demonstration (MP4, 58.7 MB)](Demo/Module%204%20Midterm%20-%20Evan%20Pritchard.mp4) - Click view raw to download.
