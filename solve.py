
key=int(input ("Enter the key (hex):" ),16)
encrypted=int (input("Enter the encrypted text (hex):"),16)
secret= (key)^(encrypted)

print(secret)
print(hex(secret))