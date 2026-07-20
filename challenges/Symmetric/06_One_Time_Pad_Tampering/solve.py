from Crypto.Util.strxor import strxor

ciphertext = bytes.fromhex(input("Enter the ciphertext (hex): "))

key = strxor(ciphertext, b"sleep")

new_ciphertext = strxor(b"flag!", key)

print(new_ciphertext.hex())