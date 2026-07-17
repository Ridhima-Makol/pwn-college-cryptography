# Useful Python Functions

## Hexadecimal

```python
hex(58)
# '0x3a'
int("3a",16)
# 58
# Python for Cryptography

## Input

```python
name = input("Enter your name: ")
```

---

## Integer Input

```python
age = int(input("Enter age: "))
```

---

## Hexadecimal to Integer

```python
num = int(input("Enter hex: "), 16)
```

Accepts:

```
df
```

or

```
0xdf
```

---

## Decimal to Hexadecimal

```python
hex(255)
# 0xff
```

---

## f-Strings

```python
name = "Alice"

print(f"Hello {name}")
```

Output:

```
Hello Alice
```
# Input
name = input("Enter your name: ")

# Integer Input
age = int(input("Enter age: "))

# Hexadecimal Input
key = int(input("Enter key: "), 16)

# XOR
secret = key ^ encrypted

# Decimal → Hex
hex(secret)

# f-String
print(f"Secret = {secret}")

# Bytes and String XOR

## String → Bytes

```python
text = "Hello"
text.encode()
# b'Hello'

b"Hello".decode()
# "Hello"

from Crypto.Util.strxor import strxor

strxor(b"AAA", b"16/")
# b'pwn'

# One-Time Pad (OTP)

## What is a One-Time Pad?

A One-Time Pad (OTP) is an encryption technique where each byte of the plaintext is XORed with a random key of the same length.

Encryption:

```text
Ciphertext = Plaintext ^ Key
```

Decryption:

```text
Plaintext = Ciphertext ^ Key
```

Since XOR is self-inverse:

```text
(A ^ B) ^ B = A
```

the same key is used for both encryption and decryption.

---

## `bytes.fromhex()`

Converts a hexadecimal string into bytes.

Example:

```python
bytes.fromhex("414243")
```

Output:

```python
b'ABC'
```

---

## Difference between `encode()` and `bytes.fromhex()`

### `encode()`

Converts **text → bytes**

```python
"ABC".encode()
```

Output:

```python
b'ABC'
```

---

### `bytes.fromhex()`

Converts a **hexadecimal string → bytes**

```python
bytes.fromhex("414243")
```

Output:

```python
b'ABC'
```

---

## Quick Reference

| Function | Purpose |
|----------|---------|
| `encode()` | String → Bytes |
| `decode()` | Bytes → String |
| `bytes.fromhex()` | Hex String → Bytes |
| `strxor()` | XOR two byte strings |

# One-Time Pad Tampering

## Security Properties

### Confidentiality

Protects the secrecy of the message.

Question:

> Can an attacker read the plaintext?

A One-Time Pad provides perfect confidentiality if the key is random, secret, and used only once.

---

### Integrity

Protects the message from unauthorized modification.

Question:

> Can an attacker change the message?

A One-Time Pad **does not** provide integrity.

---

## Known Plaintext Attack

If

```
Ciphertext = Plaintext ^ Key
```

and both the plaintext and ciphertext are known,

the key can be recovered:

```
Key = Ciphertext ^ Plaintext
```

---

## Forging a Ciphertext

To make the receiver decrypt to a chosen message:

```
Desired Ciphertext = Desired Plaintext ^ Key
```

---

## Useful Functions

```python
bytes.fromhex()
```

Hex string → Bytes

```python
strxor()
```

Byte-wise XOR

```python
.hex()
```

Bytes → Hex string

---

## Important Lesson

Encryption **does not automatically provide integrity**.

Modern cryptographic systems combine encryption with authentication (e.g., AES-GCM) to prevent message tampering.

# Many-Time Pad

## One-Time Pad

```
Ciphertext = Plaintext ^ Key
```

```
Plaintext = Ciphertext ^ Key
```

---

## Recovering the Key

If both plaintext and ciphertext are known,

```
Key = Ciphertext ^ Plaintext
```

---

## Chosen Plaintext Attack

If an attacker can choose the plaintext and observe its ciphertext,

the corresponding key bytes can be recovered.

Example:

```
Plaintext = AAAAA...
```

```
Ciphertext = AAAAA... ^ Key
```

Therefore,

```
Key = Ciphertext ^ AAAAA...
```

---

## Recovering Another Message

Once the key is known,

```
Message = Ciphertext ^ Key
```

can decrypt any ciphertext encrypted using that same key.

---

## Important Lesson

A One-Time Pad is perfectly secure **only when the key is never reused**.

Reusing the key turns it into a **Many-Time Pad**, making key recovery possible through chosen plaintext attacks.

# AES ECB

## AES

AES stands for Advanced Encryption Standard.

It is a symmetric block cipher.

The same key is used for encryption and decryption.

---

## Block Size

AES always encrypts blocks of

```
16 bytes
```

If the plaintext is shorter than a multiple of 16 bytes, padding is added.

---

## AES Object

```python
cipher = AES.new(key, AES.MODE_ECB)
```

This creates an AES cipher object.

No encryption or decryption happens here.

The object is configured with

- the secret key
- the encryption mode

---

## Encryption

```python
cipher.encrypt(data)
```

Encrypts the plaintext.

---

## Decryption

```python
cipher.decrypt(ciphertext)
```

Decrypts the ciphertext.

---

## Removing Padding

```python
unpad(data, cipher.block_size)
```

Removes the padding added before encryption.

---

## Hex to Bytes

```python
bytes.fromhex(hex_string)
```

Converts hexadecimal text into bytes so AES can process it.