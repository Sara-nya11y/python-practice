import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ''
    digits = string.digits if use_digits else ''
    symbols = "!@#$%^&*" if use_symbols else ''

    all_chars = lower + upper + digits + symbols

    if not all_chars:
        return "Error: At least one character type select chey"

    password = [
        random.choice(lower),
        random.choice(upper) if use_upper else None,
        random.choice(digits) if use_digits else None,
        random.choice(symbols) if use_symbols else None
    ]

    password = [p for p in password if p] # None teesey

    while len(password) < length:
        password.append(random.choice(all_chars))

    random.shuffle(password)
    return ''.join(password)

# CLI Start
if __name__ == "__main__":
    print("=== Password Generator ===")
    try:
        length = int(input("Password length [12]: ") or 12)
        upper = input("Uppercase letters? y/n [y]: ").lower()!= 'n'
        digits = input("Numbers? y/n [y]: ").lower()!= 'n'
        symbols = input("Symbols? y/n [y]: ").lower()!= 'n'

        pwd = generate_password(length, upper, digits, symbols)
        print(f"\nGenerated Password: {pwd}")
        print(f"Length: {len(pwd)}")

    except ValueError:
        print("Number ivvu ra length ki")

# this is important 
