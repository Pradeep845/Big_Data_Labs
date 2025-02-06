# RSA Encryption and Decryption

This repository implements RSA encryption and decryption in Python. It includes two primary scripts:

1. `main.py`: Contains functions for key generation, encryption, and decryption.
2. `analysis.py`: Performs performance testing and generates visualizations for encryption and decryption operations.

---

## Prerequisites

- Python 3.8 or higher

---

## Dependencies

Before running the scripts, you need to install the required Python packages. Use the following command to install dependencies:

```bash
pip install -r requirements.txt
```

### Contents of `requirements.txt`:

```plaintext
pycryptodome
matplotlib
psutil
```

---

## Steps to Run the Scripts

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run `main.py`**:

   ```bash
   python main.py
   ```

   This script generates RSA key pairs, encrypts a sample message, and decrypts it to verify correctness.

4. **Run `analysis.py`**:
   ```bash
   python analysis.py
   ```
   This script performs performance testing for RSA encryption and decryption and generates visualizations.

---

## Test Cases

### Test Case 1: Small Message Encryption/Decryption

- **Input**: `"Hello, RSA!"`
- **Expected Output**: The decrypted message matches the original message.

### Test Case 2: Large Message Encryption/Decryption

- **Input**: A string of 1000 characters.
- **Expected Output**: The decrypted message matches the original message.

### Test Case 3: Invalid Key Decryption

- **Input**: Attempt to decrypt with a mismatched private key.
- **Expected Output**: An error indicating decryption failure.

---

## Sample Data

You can use the following sample data for testing:

```plaintext
Sample Message 1: "This is a test message."
Sample Message 2: "A" * 500 (500 repeated 'A's)
Sample Message 3: "RSA encryption is awesome!"
```

---

## Performance Testing and Visualization

The `analysis.py` script performs the following:

1. Measures encryption and decryption times for different input sizes.
2. Compares memory usage.
3. Analyzes CPU utilization.
4. Generates visualizations for the results.

### Steps:

1. Run the script:

   ```bash
   python analysis.py
   ```

2. View the generated plots for:
   - Encryption and decryption times.
   - Memory usage.
   - CPU utilization.

---

## Recommendations

- For large input sizes, consider using hybrid encryption (e.g., AES for data and RSA for encrypting the AES key).
- Optimize RSA parameters (key size) based on performance needs.

---
