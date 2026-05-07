# Password Strength Analyzer
# Created by Kiran

import re
import random
import string


# Some common weak passwords
common_passwords = [
    "123456",
    "password",
    "qwerty",
    "abc123",
    "admin",
    "12345678",
    "password1",
    "iloveyou",
    "111111"
]


# Function to generate strong password
def generate_password(length=16):

    letters = string.ascii_letters
    numbers = string.digits
    symbols = "!@#$%^&*()_+-="

    all_characters = letters + numbers + symbols

    password = ""

    # adding important character types
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.ascii_lowercase)
    password += random.choice(numbers)
    password += random.choice(symbols)

    # filling remaining characters
    for i in range(length - 4):
        password += random.choice(all_characters)

    # shuffle password
    password_list = list(password)
    random.shuffle(password_list)

    final_password = "".join(password_list)

    return final_password


# Function to check password strength
def analyze_password(password):

    score = 0
    suggestions = []

    has_upper = False
    has_lower = False
    has_number = False
    has_special = False

    # checking uppercase
    if re.search(r"[A-Z]", password):
        has_upper = True
        score += 1
    else:
        suggestions.append(
            "Add at least one uppercase letter."
        )

    # checking lowercase
    if re.search(r"[a-z]", password):
        has_lower = True
        score += 1
    else:
        suggestions.append(
            "Add at least one lowercase letter."
        )

    # checking numbers
    if re.search(r"\d", password):
        has_number = True
        score += 1
    else:
        suggestions.append(
            "Include at least one number."
        )

    # checking special characters
    if re.search(r"[!@#$%^&*()_+=-]", password):
        has_special = True
        score += 1
    else:
        suggestions.append(
            "Use special characters like @ or #."
        )

    # checking length
    if len(password) >= 12:
        score += 2

    elif len(password) >= 8:
        score += 1

    else:
        suggestions.append(
            "Password should be at least 8 characters long."
        )

    # checking common passwords
    if password.lower() in common_passwords:
        score -= 2

        suggestions.append(
            "This password is too common."
        )

    # repeated characters check
    if len(set(password)) < 4:
        suggestions.append(
            "Avoid repeating same characters too much."
        )

    # deciding strength
    if score <= 2:
        strength = "Weak ❌"

    elif score <= 4:
        strength = "Medium ⚠️"

    else:
        strength = "Strong ✅"

    # printing result
    print("\n========== PASSWORD REPORT ==========")

    print(f"Password Length : {len(password)}")
    print(f"Password Strength : {strength}")
    print(f"Security Score : {score}/6")

    print("\nChecks")

    print(
        "Uppercase Letters :",
        "Yes" if has_upper else "No"
    )

    print(
        "Lowercase Letters :",
        "Yes" if has_lower else "No"
    )

    print(
        "Numbers :",
        "Yes" if has_number else "No"
    )

    print(
        "Special Characters :",
        "Yes" if has_special else "No"
    )

    # showing suggestions
    print("\nSuggestions")

    if len(suggestions) == 0:
        print("Great! Your password is secure 🔐")

    else:
        for tip in suggestions:
            print("-", tip)


# Main program starts here

print("===================================")
print("   PASSWORD STRENGTH ANALYZER 🔐")
print("===================================")

while True:

    user_password = input(
        "\nEnter password to analyze: "
    )

    # empty password check
    if user_password.strip() == "":
        print("Password cannot be empty.")
        continue

    # analyzing password
    analyze_password(user_password)

    # asking for generated password
    choice = input(
        "\nGenerate strong password? (y/n): "
    ).lower()

    if choice == "y":

        strong_password = generate_password()

        print("\nSuggested Strong Password:")
        print(strong_password)

    # asking to continue
    again = input(
        "\nCheck another password? (y/n): "
    ).lower()

    if again != "y":

        print("\nThank you for using Password Analyzer 🔐")

        break
