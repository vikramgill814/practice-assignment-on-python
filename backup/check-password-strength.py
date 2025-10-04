import re

def check_password_strength(password: str) -> str:
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password) is not None
    lower_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    score = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria])

    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Medium"
    else:
        return "Poor"

def main():
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print(f"Password strength: {strength}")

    if strength == "Strong":
        print("Your password is strong and meets all criteria.")
    elif strength == "Medium":
        print("Your password is medium. Consider adding more complexity.")
    else:
        print("Your password is poor. Please use at least 8 characters, mix uppercase, lowercase, digits, and special characters.")

if __name__ == "__main__":
    main()