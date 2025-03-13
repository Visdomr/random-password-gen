import random
import string


def generate_password():
    length = int(input("Enter the desired password length: ").strip())
    include_uppercase = input(
        "Include uppercase letters? (yes/no): ").strip().lower()
    include_special = input(
        "Include special characters? (yes/no): ").strip().lower()
    include_digits = input("Include digits? (yes/no): ").strip().lower()

    if length < 4:
        print("Password length must be at least 4 characters.")
        return

    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase == "yes" else ""
    special = string.punctuation if include_special == "yes" else ""
    digits = string.digits if include_digits == "yes" else ""
    all_characters = lower + uppercase + special + digits

    print(all_characters)


generate_password()
