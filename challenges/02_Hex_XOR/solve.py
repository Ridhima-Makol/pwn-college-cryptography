
key = int(input("Enter the key (hex): "), 16)


encrypted = int(input("Enter the encrypted secret (hex): "), 16)


secret = key ^ encrypted


print(f"Secret (decimal): {secret}")
print(f"Secret (hex): {hex(secret)}")