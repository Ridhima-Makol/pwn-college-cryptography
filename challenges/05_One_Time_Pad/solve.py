from Crypto.Util.strxor import strxor

ciphertext = bytes.fromhex(input("Enter the ciphertext (hex): "))
key = bytes.fromhex(input("Enter the key (hex): "))

result = strxor(ciphertext, key)

print(result.decode())