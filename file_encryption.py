from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad
import getpass

def generate_key_from_password(password, salt):
    key = PBKDF2(password, salt, dkLen=32)  # Derive a 256-bit (32-byte) key
    return key

def encrypt_file_with_password(input_file, output_file):
    password = getpass.getpass("Enter password: ").encode('utf-8')  # Convert password to bytes
    salt = get_random_bytes(16)  # Generate a random salt

    # Derive AES key from password and salt
    key = generate_key_from_password(password, salt)

    # Encrypt file with derived key
    cipher = AES.new(key, AES.MODE_CBC)
    with open(input_file, 'rb') as f:
        data = f.read()
    padded_data = pad(data, AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    with open(output_file, 'wb') as f:
        f.write(salt + encrypted_data)


# Prompt the user to input file names
input_file = input("Enter the name or path of the input file: ")
encrypted_file = input("Enter the name or path for the encrypted file: ")


# Encrypt file with password
encrypt_file_with_password(input_file, encrypted_file)
print("File encrypted successfully.")
