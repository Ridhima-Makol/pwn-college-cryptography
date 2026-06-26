# Challenge 01 - XOR

## Objective

Recover the original secret using the provided XOR key.

## Concepts

- Binary
- Bitwise XOR
- XOR is self-inverse

## Theory

XOR compares bits:

- Same bits give 0
- Different bits give 1

The important property is:

(A ^ B) ^ B = A

This allows the same key to be used for both encryption and decryption.

## Solution

```
key = 104
encrypted = 82

secret = encrypted ^ key

print(secret)
```

## Output

```
58
```

## What I Learned

- How XOR works on binary numbers.
- Why XOR is reversible.
- How Python uses the `^` operator for bitwise XOR.
- Why XOR is commonly used in cryptography.