from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

key = bytes.fromhex(input("Enter AES Key (hex): "))
ciphertext = bytes.fromhex(input("Enter Ciphertext (hex): "))

cipher = AES.new(key, AES.MODE_ECB)

plaintext = cipher.decrypt(ciphertext)

flag = unpad(plaintext, AES.block_size)

print(flag.decode())