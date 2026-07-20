from pwn import *
import string

# Start the challenge
p = process("/challenge/run")

# All possible printable characters that may appear in the flag
chars = string.printable

# Store recovered flag
flag = ""

# Try each position in the flag
for index in range(100):

    # ------------------------------------
    # Get ciphertext of flag[index]
    # ------------------------------------

    p.recvuntil(b"Choice? ")
    p.sendline(b"2")

    p.recvuntil(b"Index? ")
    p.sendline(str(index).encode())

    p.recvuntil(b"Length? ")
    p.sendline(b"1")

    p.recvuntil(b"Result: ")
    target_cipher = p.recvline().strip()

    found = False

    # ------------------------------------
    # Try every possible character
    # ------------------------------------

    for ch in chars:

        # Option 1: Encrypt chosen plaintext
        p.recvuntil(b"Choice? ")
        p.sendline(b"1")

        p.recvuntil(b"Data? ")
        p.sendline(ch.encode())

        p.recvuntil(b"Result: ")
        test_cipher = p.recvline().strip()

        # ECB property:
        # same plaintext + same key = same ciphertext
        if test_cipher == target_cipher:

            flag += ch

            print("Flag so far:", flag)

            found = True
            break

    # No character matched -> likely reached end of flag
    if not found:
        break


print("\nRecovered flag:")
print(flag)

p.close()