# Challenge 06 - One-Time Pad Tampering

## Objective

Modify an encrypted command so that the receiver executes `flag!` instead of `sleep`, without knowing the secret key.

---

## Concepts Used

- One-Time Pad (OTP)
- XOR
- Known Plaintext Attack
- Message Tampering
- Integrity vs Confidentiality
- `strxor()`
- `bytes.fromhex()`
- `.hex()`

---

## Theory

The dispatcher encrypts the command:

```
sleep
```

using a secret key.

```
Ciphertext = Plaintext XOR Key
```

Since the source code reveals that the original plaintext is `"sleep"` and also provides the ciphertext, the first five bytes of the key can be recovered:

```
Key = Ciphertext XOR Plaintext
```

Once the key is known, a new ciphertext can be forged for any 5-byte command.

To make the worker decrypt to `"flag!"`:

```
New Ciphertext = "flag!" XOR Key
```

When the worker decrypts it:

```
(New Ciphertext XOR Key)
= (flag! XOR Key) XOR Key
= flag!
```

The worker believes the original sender intended to execute `flag!` and prints the flag.

---

## Python Solution

```python
from Crypto.Util.strxor import strxor

ciphertext = bytes.fromhex(input("Enter the ciphertext (hex): "))

key = strxor(ciphertext, b"sleep")

new_ciphertext = strxor(b"flag!", key)

print(new_ciphertext.hex())
```

---

## What I Learned

- Encryption alone does not guarantee message integrity.
- A known plaintext-ciphertext pair reveals the XOR key.
- XOR allows attackers to forge valid ciphertexts if the corresponding key bytes are known.
- `.hex()` converts bytes into hexadecimal strings suitable for transmission.
- Reading the challenge source code is often an important part of solving cybersecurity challenges.