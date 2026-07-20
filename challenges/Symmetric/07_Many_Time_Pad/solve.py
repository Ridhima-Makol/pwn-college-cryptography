from Crypto.Util.strxor import strxor

# Flag ciphertext printed by the challenge
flag_cipher = bytes.fromhex(
    input("Enter the Flag Ciphertext (hex): ")
)

# Ciphertext returned after encrypting 60 A's
known_cipher = bytes.fromhex(
    input("Enter the Ciphertext of 60 A's (hex): ")
)

# Our known plaintext (60 bytes)
known_plain = b"A" * 60

# Recover the key
key = strxor(known_cipher, known_plain)

# Decrypt the flag
flag = strxor(flag_cipher, key)

print("Flag:")
print(flag.decode())