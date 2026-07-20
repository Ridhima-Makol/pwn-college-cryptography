encrypted = input("Enter the value of encrypted character: ")
ascii_value = ord(encrypted)

key = int(input("Enter the value of key (hex): "), 16)

secret = ascii_value ^ key

result = chr(secret)

print(result)