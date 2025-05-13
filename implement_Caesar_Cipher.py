def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Program ===")
    choice = input("Choose an option: (E)ncrypt or (D)ecrypt: ").strip().upper()
    
    if choice not in ['E', 'D']:
        print("Invalid choice. Please select 'E' or 'D'.")
        return

    message = input("Enter your message: ")
    
    try:
        shift = int(input("Enter shift value (integer): "))
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        return

    if choice == 'E':
        result = caesar_encrypt(message, shift)
        print("Encrypted message:", result)
    else:
        result = caesar_decrypt(message, shift)
        print("Decrypted message:", result)

if __name__ == "__main__":
    main()
