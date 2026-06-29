# Challenge 04 - String XOR

## Objective

Decrypt an encrypted ASCII string by XORing it with a given key using Python's `strxor()` function from the PyCryptodome library.

---

## Concepts Used

* XOR on strings
* ASCII encoding
* Bytes
* `encode()`
* `decode()`
* `strxor()`

---

## Theory

XOR operations can be applied not only to individual numbers or characters but also to entire strings.

A string XOR works **byte by byte**:

```
Encrypted : A   A   A
Key       : 1   6   /
              ↓   ↓   ↓
             XOR XOR XOR
              ↓   ↓   ↓
Output    : p   w   n
```

The `strxor()` function performs this byte-by-byte XOR automatically.

Since `strxor()` operates on **bytes**, Python strings must first be converted using `.encode()`. After the XOR operation, the resulting bytes are converted back into a readable string using `.decode()`.

---

## Python Solution

```python
from Crypto.Util.strxor import strxor

text = input("Enter the encrypted string: ")
key = input("Enter the XOR key: ")

text = text.encode()
key = key.encode()

result = strxor(text, key)

print(result.decode())
```

---

## Example

**Input**

```
Encrypted String: AAA
Key: 16/
```

**Process**

```
A ^ 1
A ^ 6
A ^ /
```

Result:

```
pwn
```

---

## What I Learned

* XOR can be applied to entire strings one byte at a time.
* Python strings and bytes are different data types.
* `.encode()` converts a string into bytes.
* `.decode()` converts bytes back into a string.
* `strxor()` performs byte-by-byte XOR on two byte strings of equal length.
