import random
import string

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    while True:
        try:
            length = int(input("Enter the desired password length (default is 16): ") or 16)
            if length <= 0:
                print("Please enter a positive number.")
                continue
            password = generate_password(length)
            print(f"Your generated password is: {password}")
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        again = input("Do you want to generate another password? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("Thank you for using the Random Password Generator.")
            break

if __name__ == "__main__":
    main()
