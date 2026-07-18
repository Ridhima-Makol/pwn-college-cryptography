# Challenge 09 - AES ECB Chosen Plaintext Attack

## Objective

Recover a secret flag encrypted using AES in ECB mode without knowing the AES key.

The challenge provides an encryption oracle that allows us to:

1. Encrypt plaintext of our choice.
2. Encrypt a selected portion of the secret flag.

By exploiting the deterministic nature of AES-ECB, we can recover the flag one character at a time.

## Concepts Used

- AES
- ECB Mode
- Encryption Oracle
- Chosen Plaintext Attack
- Codebook Attack
- Python slicing
- Pwntools
- Automated process interaction

## Vulnerability

AES itself is not broken.

The weakness comes from ECB mode:

```text
Same Plaintext + Same Key
        ↓
Same Ciphertext
```

The challenge lets us encrypt individual bytes of the secret flag:

```python
pt = flag[index:index+length]
```

For example:

```text
Index = 0
Length = 1
```

encrypts only the first character.

We can then encrypt possible characters ourselves and compare their ciphertexts.

```text
Secret character ciphertext = ABC123

"a" → XYZ111  ❌
"b" → XYZ222  ❌
...
"p" → ABC123  ✅
```

Therefore, the secret character must be `p`.

Repeating this for every index reconstructs the entire flag.

## Solution

```python
from pwn import *
import string

p = process("/challenge/run")

chars = string.printable
flag = ""

for index in range(100):

    # Encrypt one unknown character of the flag
    p.recvuntil(b"Choice? ")
    p.sendline(b"2")

    p.recvuntil(b"Index? ")
    p.sendline(str(index).encode())

    p.recvuntil(b"Length? ")
    p.sendline(b"1")

    p.recvuntil(b"Result: ")
    target_cipher = p.recvline().strip()

    found = False

    # Try possible plaintext characters
    for ch in chars:

        p.recvuntil(b"Choice? ")
        p.sendline(b"1")

        p.recvuntil(b"Data? ")
        p.sendline(ch.encode())

        p.recvuntil(b"Result: ")
        test_cipher = p.recvline().strip()

        if test_cipher == target_cipher:
            flag += ch
            print("Flag so far:", flag)

            found = True
            break

    if not found:
        break

print("\nRecovered flag:")
print(flag)

p.close()
```

## Initial Bug

Initially, the candidate set was:

```python
chars = string.ascii_letters + string.digits + "{}_-"
```

The script recovered:

```text
pwn
```

and then stopped.

The next character was:

```text
.
```

but `.` was missing from the candidate set.

Therefore, no ciphertext matched and:

```python
if not found:
    break
```

terminated the recovery.

Using:

```python
chars = string.printable
```

included `.` and other punctuation, allowing the complete flag to be recovered.

## What I Learned

- AES itself was not broken; the weakness came from how ECB mode was used.
- ECB encryption is deterministic.
- An encryption oracle allows an attacker to encrypt chosen plaintexts.
- Ciphertexts can act like fingerprints for known plaintexts under ECB.
- Secret data can be recovered by comparing encrypted guesses.
- Pwntools can automate interaction with interactive challenge programs.
- `recvuntil()` waits for a prompt.
- `sendline()` sends input automatically.
- Candidate sets must include every possible secret character.