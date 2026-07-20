# Challenge 05 - One-Time Pad

## Objective

Decrypt a flag that has been encrypted using a One-Time Pad (OTP). The challenge provides both the ciphertext and the key in hexadecimal format.

---

## Concepts Used

- One-Time Pad (OTP)
- XOR
- `bytes.fromhex()`
- `strxor()`
- `.decode()`

---

## Theory

A One-Time Pad (OTP) is one of the simplest and most secure encryption techniques. It encrypts data by XORing each byte of the plaintext with a unique random key of the same length.

Encryption:

```
Ciphertext = Plaintext XOR Key
```

Decryption:

```
Plaintext = Ciphertext XOR Key
```

Since XOR is self-inverse, applying the same key again recovers the original plaintext.

The challenge provides the ciphertext and key as hexadecimal strings, so they must first be converted into bytes using `bytes.fromhex()`. After XORing the two byte sequences, the result is decoded into a readable string.

---

## Python Solution

```python
from Crypto.Util.strxor import strxor

ciphertext = bytes.fromhex(input("Enter the ciphertext (hex): "))
key = bytes.fromhex(input("Enter the key (hex): "))

result = strxor(ciphertext, key)

print(result.decode())
```

---

## What I Learned

- A One-Time Pad encrypts data by XORing it with a random key.
- XOR is self-inverse, so the same operation is used for both encryption and decryption.
- `bytes.fromhex()` converts a hexadecimal string into bytes.
- Cryptographic operations are performed on bytes rather than text.
- The decrypted bytes can be converted back to a readable string using `.decode()`.