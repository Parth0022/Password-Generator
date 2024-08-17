import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    # Define the character set based on user preferences
    charset = string.ascii_lowercase  # always include lowercase letters
    
    if use_uppercase:
        charset += string.ascii_uppercase
    if use_digits:
        charset += string.digits
    if use_special_chars:
        charset += string.punctuation
    
    if not charset:
        raise ValueError("No character set selected! Please enable at least one option.")
    
    # Generate a password by randomly selecting characters from the charset
    password = ''.join(random.choice(charset) for _ in range(length))
    return password

# User input for customization
password_length = int(input("Enter password length: "))
include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
include_digits = input("Include digits? (y/n): ").lower() == 'y'
include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

# Generate and print the password
password = generate_password(password_length, include_uppercase, include_digits, include_special_chars)
print(f"Generated Password: {password}")
