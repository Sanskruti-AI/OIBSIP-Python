import random
import string

print("===== PASSWORD GENERATOR =====")

length = int(input("Enter password length: "))

if length < 4:
    print("Password length should be at least 4")
else:
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # ensure password has at least one of each type
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    all_characters = letters + digits + symbols

    for i in range(length - 3):
        password.append(random.choice(all_characters))

    random.shuffle(password)

    final_password = "".join(password)

    print("\nGenerated Password:")
    print(final_password)