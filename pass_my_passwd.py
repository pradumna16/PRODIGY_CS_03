import random
import string
import re

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[\W_]', password))

    # Password score
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Medium"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Provide feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_char_criteria:
        feedback.append("Password should include at least one special character (e.g., !, @, #, $, etc.).")

    return strength, feedback

# Adding service for password generation
def generate_password(length=12):
    if length < 8:
        length = 8

    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))

    # Ensure password meets all criteria
    while not (re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) and re.search(r'[0-9]', password) and re.search(r'[\W_]', password)):
        password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

# User choice
user_choice = input("Do you want to create your own password or have one generated for you? (enter 'create' or 'generate'): ").strip().lower()

if user_choice == 'create':
    password = input("Enter a password to assess its strength: ")
    strength, feedback = assess_password_strength(password)
elif user_choice == 'generate':
    password = generate_password()
    strength, feedback = assess_password_strength(password)
    print(f"Generated Password: {password}")

print(f"Password Strength: {strength}")
if feedback:
    print("Feedback:")
    for item in feedback:
        print(f" - {item}")
