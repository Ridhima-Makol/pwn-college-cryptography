# Challenge 02 - Hexadecimal XOR

## Objective

Recover the original secret using a hexadecimal XOR key.

---

## Concepts Used

- Hexadecimal numbers
- Bitwise XOR
- Python `int(..., 16)`
- Python `hex()`

---

## Theory

Hexadecimal is a base-16 number system.

Python represents hexadecimal numbers using the `0x` prefix.

Example:

```python
0xFF
```

equals

```
255
```

To decrypt:

```
secret = encrypted ^ key
```

because XOR is self-inverse.

---

## Python Solution

```python
key = int(input("Enter the key (hex): "), 16)
encrypted = int(input("Enter the encrypted secret (hex): "), 16)

secret = key ^ encrypted

print(f"Secret (decimal): {secret}")
print(f"Secret (hex): {hex(secret)}")
```

---

## What I Learned

- How hexadecimal numbers work.
- How to convert hexadecimal strings to integers.
- How to convert integers back to hexadecimal.
- How XOR works with hexadecimal values.