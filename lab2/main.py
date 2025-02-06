from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
import base64

def generate_key_pair():
    """
    Generate RSA key pairs (private and public keys).
    :return: tuple (private_key, public_key) as PEM strings
    """
    key = RSA.generate(2048)
    private_key = key.export_key().decode()
    public_key = key.publickey().export_key().decode()
    return private_key, public_key

def encrypt_message(public_key_pem, message):
    """
    Encrypt a message using the provided public key.
    :param public_key_pem: PEM string of the public key
    :param message: Message to be encrypted (string)
    :return: Encrypted message (base64 encoded string)
    """
    try:
        public_key = RSA.import_key(public_key_pem)
        cipher = PKCS1_OAEP.new(public_key)
        encrypted_data = cipher.encrypt(message.encode())
        return base64.b64encode(encrypted_data).decode()
    except Exception as e:
        raise ValueError(f"Error during encryption: {str(e)}")

def decrypt_message(private_key_pem, encrypted_message):
    """
    Decrypt an encrypted message using the provided private key.
    :param private_key_pem: PEM string of the private key
    :param encrypted_message: Encrypted message (base64 encoded string)
    :return: Decrypted message (string)
    """
    try:
        private_key = RSA.import_key(private_key_pem)
        cipher = PKCS1_OAEP.new(private_key)
        encrypted_data = base64.b64decode(encrypted_message)
        return cipher.decrypt(encrypted_data).decode()
    except Exception as e:
        raise ValueError(f"Error during decryption: {str(e)}")

def main():
    # Step 1: Generate key pair
    print("Generating RSA key pair...")
    private_key, public_key = generate_key_pair()
    print("Private Key:")
    print(private_key)
    print("\nPublic Key:")
    print(public_key)

    # Step 2: Encrypt a message
    message = "Hello, RSA Encryption!"
    print(f"\nOriginal Message: {message}")
    encrypted_message = encrypt_message(public_key, message)
    print(f"Encrypted Message: {encrypted_message}")

    # Step 3: Decrypt the message
    decrypted_message = decrypt_message(private_key, encrypted_message)
    print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
