def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        # If it's not a letter, keep it as it is
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Caesar Cipher")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? \n").upper()
    if choice not in ['E', 'D']:
        print("Invalid choice. Please select 'E' or 'D'.")
        return
    
    message = input("Enter your message: \n")
    shift = int(input("Enter the shift value: \n"))
    
    if choice == 'E':
        result = encrypt(message, shift)
        print(f"Encrypted Message: {result}")
    elif choice == 'D':
        result = decrypt(message, shift)
        print(f"Decrypted Message: {result}")

if __name__ == "__main__":
    main()
