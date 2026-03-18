import re

password = input("Enter a password: ")

print("\nChecking password strength...\n")

score = 0

# Check length
if len(password) >= 8:
    print("Password length is good")
    score += 1
else:
    print("Password should be at least 8 characters")

# Check uppercase letters
if re.search("[A-Z]", password):
    print("Contains uppercase letter")
    score += 1
else:
    print("Add uppercase letters")

# Check lowercase letters
if re.search("[a-z]", password):
    print("Contains lowercase letter")
    score += 1
else:
    print("Add lowercase letters")

# Check numbers
if re.search("[0-9]", password):
    print("Contains numbers")
    score += 1
else:
    print("Add numbers")

# Check special characters
if re.search("[@#$%^&*!]", password):
    print("Contains special character")
    score += 1
else:
    print("Add special characters")

# Final result
print("\nPassword Strength Result:")

if score <= 2:
    print("Weak Password")
elif score == 3 or score == 4:
    print("Medium Password")
else:
    print("Strong Password")
