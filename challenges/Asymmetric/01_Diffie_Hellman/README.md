# Diffie-Hellman Key Exchange

## Objective

Perform a Diffie-Hellman Key Exchange with the challenge and calculate the correct shared secret to retrieve the flag.

## Concept

Diffie-Hellman allows two parties to establish the same shared secret over a public communication channel without directly transmitting the secret.

The public parameters are:

- `p` - a large prime modulus
- `g` - a generator

Alice generates a private value:

```text
a
```

and calculates her public value:

```text
A = g^a mod p
```

Bob generates his own private value:

```text
b
```

and calculates:

```text
B = g^b mod p
```

Alice and Bob exchange `A` and `B` publicly.

They then independently calculate the shared secret.

Alice:

```text
s = B^a mod p
```

Bob:

```text
s = A^b mod p
```

Both values are equal because:

```text
B^a = (g^b)^a = g^(ab)

A^b = (g^a)^b = g^(ab)
```

Therefore, both parties obtain the same shared secret without transmitting it directly.

## Challenge Logic

The challenge acts as **Alice**.

It generates:

```python
a = getrandbits(2048)
A = pow(g, a, p)
```

and gives us:

```text
p
g
A
```

We act as **Bob**.

First, we generate our private value:

```python
b = getrandbits(2048)
```

Then calculate our public value:

```python
B = pow(g, b, p)
```

We send `B` to the challenge.

Finally, we calculate the shared secret using Alice's public value:

```python
s = pow(A, b, p)
```

The challenge independently calculates:

```python
s = pow(B, a, p)
```

Both shared secrets are identical.

## Solution

```python
from pwn import *
from Crypto.Random.random import getrandbits

p = process("/challenge/run")

p.recvuntil(b"p = ")
prime = int(p.recvline().strip(), 16)

p.recvuntil(b"g = ")
g = int(p.recvline().strip(), 16)

p.recvuntil(b"A = ")
A = int(p.recvline().strip(), 16)

b = getrandbits(2048)

B = pow(g, b, prime)

p.recvuntil(b"B? ")
p.sendline(hex(B).encode())

s = pow(A, b, prime)

p.recvuntil(b"s? ")
p.sendline(hex(s).encode())

print(p.recvall().decode())
```

## Important Python Concepts

### Modular Exponentiation

Python provides:

```python
pow(base, exponent, modulus)
```

Therefore:

```python
B = pow(g, b, p)
```

means:

```text
B = g^b mod p
```

This is much more efficient for large cryptographic numbers than calculating:

```python
(g ** b) % p
```

### Hexadecimal Conversion

The challenge communicates large numbers in hexadecimal.

To convert received hex into an integer:

```python
value = int(hex_value, 16)
```

To send an integer as hexadecimal:

```python
hex(value).encode()
```

## What I Learned

- Diffie-Hellman solves the key-exchange problem.
- Public values can safely be transmitted without revealing private values.
- `a` and `b` are private values.
- `A` and `B` are public values.
- Both parties independently derive the same shared secret.
- The shared secret itself is never transmitted.
- `pow(base, exponent, modulus)` efficiently performs modular exponentiation.
- Pwntools can automate interaction with an interactive cryptographic challenge.