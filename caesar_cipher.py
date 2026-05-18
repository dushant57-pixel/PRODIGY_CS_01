def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# Example Usage
message = input("Enter your message: ")
shift_value = int(input("Enter shift value: "))

choice = input("Do you want to Encrypt or Decrypt? (E/D): ").lower()

if choice == 'e':
    print("Encrypted message:", encrypt(message, shift_value))
elif choice == 'd':
    print("Decrypted message:", decrypt(message, shift_value))
else:
    print("Invalid choice.")
