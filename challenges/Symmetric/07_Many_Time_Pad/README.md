# Challenge 07 - Many-Time Pad

## Objective

Decrypt the encrypted flag without directly knowing the key.

Unlike the previous challenge, the program reuses the same One-Time Pad (OTP) key for multiple encryptions and allows us to encrypt arbitrary plaintexts.

---

## Concepts Used

- One-Time Pad (OTP)
- XOR
- Encryption Oracle
- Key Reuse Vulnerability
- Known Plaintext Attack
- `strxor()`
- `bytes.fromhex()`

---

## Theory

A One-Time Pad encrypts data using

```
Ciphertext = Plaintext XOR Key
```

It is perfectly secure only if the key is used exactly once.

In this challenge, the same key is reused for both the flag and every plaintext we choose to encrypt.

Since we can choose our own plaintext, we know both

```
Plaintext
```

and

```
Ciphertext
```

for that message.

Therefore,

```
Key = Ciphertext XOR Plaintext
```

After recovering the required bytes of the key, the flag can be decrypted using

```
Flag = FlagCiphertext XOR Key
```

---

## Attack Algorithm

1. Copy the encrypted flag.
2. Determine the flag length.
3. Encrypt a known plaintext of the same length (60 bytes of `A`).
4. Recover the key using

```
Key = KnownCiphertext XOR KnownPlaintext
```

5. Recover the flag using

```
Flag = FlagCiphertext XOR Key
```

---

## Python Solution

```python
from Crypto.Util.strxor import strxor

flag_cipher = bytes.fromhex(input("Enter the Flag Ciphertext (hex): "))
known_cipher = bytes.fromhex(input("Enter the Ciphertext of 60 A's (hex): "))

known_plain = b"A" * 60

key = strxor(known_cipher, known_plain)

flag = strxor(flag_cipher, key)

print(flag.decode())
```

---

## What I Learned

- Reusing a One-Time Pad completely breaks its security.
- A chosen plaintext attack can recover the encryption key.
- Once the key is known, every ciphertext encrypted with that key can be decrypted.
- Encryption oracles are dangerous when the same key is reused.