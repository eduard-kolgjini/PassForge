from cryptography.fernet import Fernet
import random
import string
import os

# Generate or load the encryption key
def load_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
    return key

def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password(encrypted_password):
    with open("passwords.txt", "a") as file:
        file.write(encrypted_password.decode() + "\n")

def retrieve_passwords(key):
    if os.path.exists("passwords.txt"):
        with open("passwords.txt", "r") as file:
            encrypted_passwords = file.readlines()
            for encrypted_password in encrypted_passwords:
                decrypted_password = decrypt_message(encrypted_password.strip().encode(), key)
                print(f"Decrypted Password: {decrypted_password}")
    else:
        print("No passwords found.")

def main():
    key = load_key()
    while True:
        choice = input("Generate a new password (G) or Retrieve saved passwords (R) or Quit (Q)? ").upper()
        if choice == "G":
            password = generate_password()
            print(f"Generated Password: {password}")
            encrypted_password = encrypt_message(password, key)
            save_password(encrypted_password)
        elif choice == "R":
            retrieve_passwords(key)
        elif choice == "Q":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
