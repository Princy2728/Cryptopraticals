text = input("Enter text: ")
k = int(input("Enter key (1-25): "))

result = ""

for ch in text:
    if ch.isalpha():
        s = 65 if ch.isupper() else 97
        result += chr((ord(ch) - s + k) % 26 + s)
    else:
        result += ch

print("Encrypted text:", result)
