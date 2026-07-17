# Challenge 08 - AES ECB Decryption

## Objective

Decrypt an AES-encrypted flag using the provided AES key.

Unlike the previous challenges, we are not attacking the encryption. We are simply using the correct key to decrypt the ciphertext.

---

## Concepts Used

- AES (Advanced Encryption Standard)
- Symmetric Encryption
- ECB (Electronic Codebook) Mode
- Block Cipher
- Padding
- `bytes.fromhex()`
- `AES.new()`
- `decrypt()`
- `unpad()`

---

## Theory

AES is a symmetric encryption algorithm, meaning the same key is used for both encryption and decryption.

AES operates on blocks of 16 bytes.

If the plaintext is not a multiple of 16 bytes, padding is added before encryption.

During decryption, the padding must be removed to recover the original plaintext.

---

## Encryption

```
Plaintext
    │
    ▼
Pad to 16-byte blocks
    │
    ▼
AES Encryption (ECB)
    │
    ▼
Ciphertext
```

---

## Decryption

```
Ciphertext
    │
    ▼
AES Decryption
    │
    ▼
Padded Plaintext
    │
    ▼
Remove Padding
    │
    ▼
Original Plaintext
```

---

## Solution

```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

key = bytes.fromhex(input("Enter AES Key (hex): "))
ciphertext = bytes.fromhex(input("Enter Ciphertext (hex): "))

cipher = AES.new(key, AES.MODE_ECB)

plaintext = cipher.decrypt(ciphertext)

flag = unpad(plaintext, cipher.block_size)

print(flag.decode())
```

---

## What I Learned

- AES is a block cipher that operates on 16-byte blocks.
- AES uses the same key for encryption and decryption.
- ECB encrypts each block independently.
- `AES.new()` creates an AES cipher object.
- `decrypt()` decrypts ciphertext using the configured key and mode.
- `unpad()` removes the padding added during encryption.