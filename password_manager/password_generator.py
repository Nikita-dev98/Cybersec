import random
import string
import secrets

def generate_password(length=16):
    special_chars = "!@#*/&"
    characters = string.ascii_letters + string.digits + special_chars

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

"""def main():
    password = generate_password()
    print("Generated password: ", password)

if __name__ == "__main__":
    main()
    """