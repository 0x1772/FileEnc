import os
from cryptography.fernet import Fernet

def encrypt_file(file_path, key):
    """
    Encrypts a file at the given file path using the provided encryption key
    """
    # Read the contents of the file
    with open(file_path, 'rb') as file:
        original_content = file.read()

    # Create a Fernet cipher using the encryption key
    cipher = Fernet(key)

    # Encrypt the file contents using the Fernet cipher
    encrypted_content = cipher.encrypt(original_content)

    # Write the encrypted contents back to the file
    with open(file_path, 'wb') as file:
        file.write(encrypted_content)

if __name__ == '__main__':
    # Get the encryption key from an environment variable
    key = os.environ.get('ENCRYPTION_KEY')
    if not key:
        raise ValueError('ENCRYPTION_KEY environment variable not set')

    # Encrypt the file at the given path using the encryption key
    file_path = input('Enter the path to the file you want to encrypt: ')
    encrypt_file(file_path, key)
