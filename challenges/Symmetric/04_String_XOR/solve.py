from Crypto.Util.strxor import strxor

text = input("Enter the encrypted string: ")
key = input("Enter the XOR key: ")

text = text.encode()
key = key.encode()

result = strxor(text, key)

print(result.decode())