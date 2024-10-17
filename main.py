import random
import string

# Password generator with options for customization
def generate_password(length=12, use_digits=True, use_punctuation=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main block to take user input
if __name__ == "__main__":
    try:
        length = int(input("Enter password length: "))
        use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
        use_punctuation = input("Include special characters? (yes/no): ").lower() == 'yes'

        password = generate_password(length, use_digits, use_punctuation)
        print("Your generated password is:", password)
    except ValueError:
        print("Please enter a valid number for password length.")