from database import add_password, get_passwords, delete_password
from encryption import encrypt_password, decrypt_password
from password_generator import generate_password

def run_cli():
    while True:
        print("Password manager")
        user_input = input("Enter 1 to add password, 2 to get password and 3 to delete password: ")
    
        if user_input == '1':
            site = input("Enter site name: ")
            username = input("Enter username: ")
            password = generate_password()
            encrypted_password = encrypt_password(password)
            add_password(site, username, encrypted_password)
            print("Generated password: {password}")
            print("Password saved.")

        elif user_input == '2':
            site = input("enter site name to get username and password for: ")
            passwords = get_passwords(site)
            print("\n Passwords for site '{site}: ")
            for record in passwords:
                password_id, site, username, encrypted_password = record
                decrypted_password = decrypt_password(encrypted_password.decode())
                print(f"Username: {username}, Password: {decrypted_password}")

        elif user_input == '3':
            site = input("enter site name to delete password for: ")
            passwords = get_passwords(site)
            for record in passwords:
                password_id, site, username, encrypted_password = record
                decrypted_password = decrypt_password(encrypted_password.decode())

            delete_id = int(input("enter id of password to delete: "))
            delete_password(delete_id)
            print("password deleted successfully")

        else:
            print("Invalid option. Please try again.")


