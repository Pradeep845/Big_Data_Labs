import time
import psutil
import matplotlib.pyplot as plt
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import math

def encrypt_message(public_key_pem, message):
    """
    Encrypts a message in chunks using the provided public key.
    :param public_key_pem: PEM string of the public key
    :param message: Message to be encrypted (bytes or string)
    :return: Encrypted message (base64 encoded string)
    """
    public_key = RSA.import_key(public_key_pem)
    cipher = PKCS1_OAEP.new(public_key)
    
    if isinstance(message, str):
        message = message.encode()  # Convert to bytes if it's a string

    max_chunk_size = (public_key.size_in_bytes() - 42)  # For OAEP padding
    encrypted_chunks = []
    
    for i in range(0, len(message), max_chunk_size):
        chunk = message[i:i + max_chunk_size]  # Take a chunk of bytes
        encrypted_chunk = cipher.encrypt(chunk)
        encrypted_chunks.append(base64.b64encode(encrypted_chunk).decode())
    
    return "::".join(encrypted_chunks)  # Use "::" as a separator


def decrypt_message(private_key_pem, encrypted_message):
    """
    Decrypts a message in chunks using the provided private key.
    :param private_key_pem: PEM string of the private key
    :param encrypted_message: Encrypted message (base64 encoded string)
    :return: Decrypted message (string)
    """
    private_key = RSA.import_key(private_key_pem)
    cipher = PKCS1_OAEP.new(private_key)
    
    encrypted_chunks = encrypted_message.split("::")
    decrypted_message = ""
    
    for chunk in encrypted_chunks:
        encrypted_chunk = base64.b64decode(chunk)
        decrypted_message += cipher.decrypt(encrypted_chunk).decode()
    
    return decrypted_message


# Function to generate RSA keys
def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key


# Performance testing
def measure_performance():
    private_key, public_key = generate_rsa_keys()
    input_sizes = [10, 100, 500, 1000, 2000]  # Input sizes in bytes
    encryption_times = []
    decryption_times = []
    memory_usages = []
    cpu_usages = []

    for size in input_sizes:
        message = b"A" * size

        # Measure encryption time
        start_time = time.perf_counter()
        encrypted_message = encrypt_message(public_key, message)
        encryption_time = time.perf_counter() - start_time
        encryption_times.append(encryption_time)

        # Measure decryption time
        start_time = time.perf_counter()
        decrypted_message = decrypt_message(private_key, encrypted_message)
        decryption_time = time.perf_counter() - start_time
        decryption_times.append(decryption_time)

        # Measure memory usage
        process = psutil.Process()
        memory_usage = process.memory_info().rss / 1024 ** 2  # Convert to MB
        memory_usages.append(memory_usage)

        # Measure CPU usage
        cpu_usage = psutil.cpu_percent(interval=0.1)
        cpu_usages.append(cpu_usage)

    return input_sizes, encryption_times, decryption_times, memory_usages, cpu_usages

# Visualization of results
def visualize_results(input_sizes, encryption_times, decryption_times, memory_usages, cpu_usages):
    plt.figure(figsize=(12, 8))

    # Encryption and Decryption Times
    plt.subplot(2, 2, 1)
    plt.plot(input_sizes, encryption_times, marker='o', label="Encryption Time")
    plt.plot(input_sizes, decryption_times, marker='o', label="Decryption Time")
    plt.title("Encryption and Decryption Times")
    plt.xlabel("Input Size (bytes)")
    plt.ylabel("Time (seconds)")
    plt.legend()

    # Memory Usage
    plt.subplot(2, 2, 2)
    plt.plot(input_sizes, memory_usages, marker='o', color="orange")
    plt.title("Memory Usage")
    plt.xlabel("Input Size (bytes)")
    plt.ylabel("Memory Usage (MB)")

    # CPU Utilization
    plt.subplot(2, 2, 3)
    plt.plot(input_sizes, cpu_usages, marker='o', color="green")
    plt.title("CPU Utilization")
    plt.xlabel("Input Size (bytes)")
    plt.ylabel("CPU Utilization (%)")

    plt.tight_layout()
    plt.show()
    plt.savefig('combined_analysis1.png')
    print("Combined analysis saved as 'combined_analysis.png'")

def main():
    print("Running performance tests...")
    input_sizes, encryption_times, decryption_times, memory_usages, cpu_usages = measure_performance()
    visualize_results(input_sizes, encryption_times, decryption_times, memory_usages, cpu_usages)

if __name__ == "__main__":
    main()
