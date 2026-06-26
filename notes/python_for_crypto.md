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