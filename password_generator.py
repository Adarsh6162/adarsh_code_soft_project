import secrets
import string

def generate_password(length):
    # Define character sets for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password of the specified length
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def get_password_length():
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length > 0:
                return length
            else:
                print("Invalid length. Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("Password Generator")

    # Get desired password length from the user
    length = get_password_length()

    # Generate and display the password
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
