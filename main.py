from cryptography.fernet import Fernet
import random
import string
import os

# Generate or load the encryption key
def load_key():
    try:
        # Check if 'secret.key' file exists; if not, generate a new encryption key
        if not os.path.exists("secret.key"):
            key = Fernet.generate_key()  # Generate encryption key
            with open("secret.key", "wb") as key_file:  # Save key to file
                key_file.write(key)
        else:
            # If 'secret.key' exists, load the key
            with open("secret.key", "rb") as key_file:
                key = key_file.read()
        return key
    except Exception as e:
        print(f"Error loading key: {e}")
        return None

# Encrypt the message using the loaded key
def encrypt_message(message, key):
    if not message:
        return None
    try:
        f = Fernet(key)
        encrypted_message = f.encrypt(message.encode())
        return encrypted_message
    except Exception as e:
        print(f"Error encrypting message: {e}")
        return None

# Decrypt the message using the loaded key
def decrypt_message(encrypted_message, key):
    try:
        f = Fernet(key)  # Create a Fernet object with the key
        decrypted_message = f.decrypt(encrypted_message).decode()  # Decrypt the message
        return decrypted_message
    except Exception as e:
        print(f"Error decrypting message: {e}")
        return None

# Generate a random password with specified length (default 12 characters)
def generate_password(length=12):
    try:
        if length < 4:  # Ensure at least 1 of each character type
            raise ValueError("Password length must be at least 4.")
        if length > 100:  # Set a maximum limit for password length
            raise ValueError("Password length must not exceed 100 characters.")
        
        # Combine all character sets
        characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        
        # Ensure at least one character from each type
        password = [
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]
        
        # Fill the remaining length with random characters
        if length > 4:
            password += random.choices(characters, k=length-4)
        
        # Shuffle to avoid predictable order
        random.shuffle(password)
        
        return ''.join(password)
    
    except ValueError as ve:
        print(f"Value Error: {ve}")
        return None
    except Exception as e:
        print(f"Error generating password: {e}")
        return None

# Save the encrypted password to a file
def save_password(encrypted_password):
    try:
        with open("passwords.txt", "a") as file:  # Open file in append mode
            file.write(encrypted_password.decode() + "\n")  # Write encrypted password to file
        print("Password saved successfully!")
    except Exception as e:
        print(f"Error saving password: {e}")

# Retrieve and decrypt saved passwords from the file
def retrieve_passwords(key):
    try:
        if os.path.exists("passwords.txt"):  # Check if password file exists
            with open("passwords.txt", "r") as file:
                encrypted_passwords = file.readlines()  # Read all encrypted passwords
                for encrypted_password in encrypted_passwords:
                    decrypted_password = decrypt_message(encrypted_password.strip().encode(), key)
                    if decrypted_password:
                        print(f"Decrypted Password: {decrypted_password}")  # Print each decrypted password
        else:
            print("No passwords found.")
    except Exception as e:
        print(f"Error retrieving passwords: {e}")

# Main function to handle user interaction
def main():
    key = load_key()  # Load or generate the encryption key
    if not key:
        print("Unable to load encryption key. Exiting...")
        return

    while True:
        # Ask the user to choose an action: Generate a new password, Retrieve passwords, or Quit
        choice = input("Generate a new password (G), Retrieve saved passwords (R), or Quit (Q)? ").upper()
        
        if choice == "G":  # Generate a new password
            length = input("Enter desired password length (default is 12): ")
            try:
                length = int(length) if length else 12  # Default to 12 if no input
            except ValueError:
                print("Invalid input for length. Using default of 12.")
                length = 12

            password = generate_password(length)  # Generate the password
            if password:
                print(f"Generated Password: {password}")
                encrypted_password = encrypt_message(password, key)  # Encrypt the generated password
                if encrypted_password:
                    save_password(encrypted_password)  # Save the encrypted password

        elif choice == "R":  # Retrieve saved passwords
            retrieve_passwords(key)  # Retrieve and decrypt saved passwords

        elif choice == "Q":  # Quit the program
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")  # Handle invalid input

# Entry point of the program
if __name__ == "__main__":
    main()
