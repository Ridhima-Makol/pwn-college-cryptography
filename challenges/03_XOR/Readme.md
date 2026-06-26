# Challenge 03 - ASCII XOR

## Objective

Decrypt an encrypted character by XORing its ASCII value with the given hexadecimal key.

---

## Concepts Used

* ASCII Encoding
* Bitwise XOR (`^`)
* `ord()` – Character to ASCII value
* `chr()` – ASCII value to Character
* Hexadecimal Input (`int(..., 16)`)

---

## Theory

Computers store characters as numerical values according to the ASCII standard.

For example:

| Character | ASCII (Decimal) |  Hex |
| --------- | --------------: | ---: |
| A         |              65 | 0x41 |
| B         |              66 | 0x42 |
| @         |              64 | 0x40 |

To decrypt the character:

1. Convert the encrypted character to its ASCII value using `ord()`.
2. XOR the ASCII value with the given hexadecimal key.
3. Convert the resulting ASCII value back to a character using `chr()`.

Since XOR is self-inverse,

```
(message ^ key) ^ key = message
```

the same XOR operation can be used for both encryption and decryption.

---

## Python Solution

```python
encrypted = input("Enter the encrypted character: ")
ascii_value = ord(encrypted)

key = int(input("Enter the key (hex): "), 16)

secret = ascii_value ^ key

result = chr(secret)

print(result)
```

---

## Example

**Input**

```
Encrypted Character: A
Key: 0x01
```

**Process**

```
'A' → ord() → 65

65 ^ 1 = 64

64 → chr() → '@'
```

**Output**

```
@
```

---

## What I Learned

* Characters are stored internally as ASCII values.
* `ord()` converts a character to its ASCII value.
* `chr()` converts an ASCII value back to a character.
* XOR operations work on numbers, so characters must first be converted to their ASCII representation.
* `int(value, 16)` converts hexadecimal input into an integer.
