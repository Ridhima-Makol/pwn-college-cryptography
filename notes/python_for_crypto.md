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