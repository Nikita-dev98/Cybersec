import random
import string

def generate_pass(length=16):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    special = string.punctuation
    digits = string.digits
    all_char = lowercase + uppercase + special + digits

    password = (random.choice(lowercase) + random.choice(uppercase) + random.choice(special) + random.choice(digits) + 
                ''.join(random.choice(all_char) for _ in range(length-4))
                )
    password = ''.join(random.sample(password, len(password)))
    
    return password

def main():
    length = int(input("enter desired length: "))
    print(f"password is: {generate_pass(length)}")

if __name__ == '__main__':
    main()