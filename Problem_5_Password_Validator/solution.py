def check_password_strength():
    name = input("Enter your name: ")
    password = input("Enter your password: ")

    missing_rules = []

    if len(password) < 8:
        missing_rules.append("Password must be at least 8 characters long.")
    if not any(char.isdigit() for char in password):
        missing_rules.append("Password must contain at least one digit.")
    if password.lower() == name.lower():
        missing_rules.append("Password must not be the same as your name.")

    if missing_rules:
        print("⚠️ Password is weak. Issues:")
        for rule in missing_rules:
            print(f"- {rule}")
    else:
        print("✅ Password is strong!")
check_password_strength()
