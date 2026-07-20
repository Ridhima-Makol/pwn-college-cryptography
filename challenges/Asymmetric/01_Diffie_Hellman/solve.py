from pwn import *
from Crypto.Random.random import getrandbits

# Start the challenge
p = process("/challenge/run")

# Receive the public Diffie-Hellman parameters
p.recvuntil(b"p = ")
prime = int(p.recvline().strip(), 16)

p.recvuntil(b"g = ")
g = int(p.recvline().strip(), 16)

# Receive Alice's public value: A = g^a mod p
p.recvuntil(b"A = ")
A = int(p.recvline().strip(), 16)

# Generate Bob's private value
b = getrandbits(2048)

# Calculate Bob's public value:
# B = g^b mod p
B = pow(g, b, prime)

# Send B to Alice
p.recvuntil(b"B? ")
p.sendline(hex(B).encode())

# Calculate the shared secret:
# s = A^b mod p
s = pow(A, b, prime)

# Send the shared secret
p.recvuntil(b"s? ")
p.sendline(hex(s).encode())

# Receive the flag
print(p.recvall().decode())