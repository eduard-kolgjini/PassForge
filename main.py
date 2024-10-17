import random
import string
import re
import os

# Password generator with options for customization
def generate_password(length=12, use_digits=True, use_punctuation=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to evaluate the strength of the password
def evaluate_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search(r'[A-Z]', password):
        strength += 1
    if re.search(r'[a-z]', password):
        strength += 1
    if re.search(r'[0-9]', password):
        strength += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    
    if strength <= 2:
        return "Weak"
    elif strength == 3:
        return "Moderate"
    else:
        return "Strong"

# Function to save password to a file
def save_password(password):
    with open("saved_passwords.txt", "a") as file:
        file.write(password + "\n")
    print("Password saved successfully.")

# Function to retrieve and display saved passwords
def retrieve_passwords():
    if os.path.exists("saved_passwords.txt"):
        with open("saved_passwords.txt", "r") as file:
            saved_passwords = file.readlines()
            if saved_passwords:
                print("Saved passwords:")
                for idx, pwd in enumerate(saved_passwords, 1):
                    print(f"{idx}: {pwd.strip()}")
            else:
                print("No passwords saved.")
    else:
        print("No saved passwords found.")

# Main block
if __name__ == "__main__":
    try:
        length = int(input("Enter password length: "))
        use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
        use_punctuation = input("Include special characters? (yes/no): ").lower() == 'yes'

        password = generate_password(length, use_digits, use_punctuation)
        print("Your generated password is:", password)
        
        # Evaluate password strength
        strength = evaluate_password_strength(password)
        print(f"Password strength: {strength}")
        
        # Save password option
        save_option = input("Do you want to save this password? (yes/no): ").lower()
        if save_option == 'yes':
            save_password(password)
        
        # Retrieve saved passwords option
        retrieve_option = input("Do you want to retrieve saved passwords? (yes/no): ").lower()
        if retrieve_option == 'yes':
            retrieve_passwords()

    except ValueError:
        print("Please enter a valid number for password length.")
