from cryptography.fernet import Fernet

def load_key(key_file):
    """
    Load the encryption key from a file
    """
    return open(key_file, "rb").read()

def decrypt_file(key_file, encrypted_file, decrypted_file):
    """
    Decrypt the contents of an encrypted file using a key file
    """
    # Load the encryption key
    key = load_key(key_file)

    # Create a Fernet cipher using the encryption key
    cipher = Fernet(key)

    # Read the encrypted file
    with open(encrypted_file, "rb") as file:
        encrypted_data = file.read()

    # Decrypt the encrypted data
    decrypted_data = cipher.decrypt(encrypted_data)

    # Write the decrypted data to a file
    with open(decrypted_file, "wb") as file:
        file.write(decrypted_data)
