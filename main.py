import random
import string
import re

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
    # Check length
    if len(password) >= 8:
        strength += 1
    if re.search(r'[A-Z]', password):  # At least one uppercase letter
        strength += 1
    if re.search(r'[a-z]', password):  # At least one lowercase letter
        strength += 1
    if re.search(r'[0-9]', password):  # At least one digit
        strength += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):  # Special characters
        strength += 1
    
    if strength <= 2:
        return "Weak"
    elif strength == 3:
        return "Moderate"
    else:
        return "Strong"

# Main block to take user input and generate password
if __name__ == "__main__":
    try:
        length = int(input("Enter password length: "))
        use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
        use_punctuation = input("Include special characters? (yes/no): ").lower() == 'yes'

        password = generate_password(length, use_digits, use_punctuation)
        print("Your generated password is:", password)
        
        # Evaluate the password strength
        strength = evaluate_password_strength(password)
        print(f"Password strength: {strength}")

    except ValueError:
        print("Please enter a valid number for password length.")
