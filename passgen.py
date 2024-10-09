import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    character_pool = ''
    if use_letters:
        character_pool += string.ascii_letters  # Includes both lowercase and uppercase letters
    if use_numbers:
        character_pool += string.digits  # Includes digits 0-9
    if use_symbols:
        character_pool += string.punctuation  # Includes special characters

    if not character_pool:
        raise ValueError("At least one character type must be selected.")

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("Random Password Generator")
    
    # Get user input for password length and character types
    length = int(input("Enter desired password length: "))
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    try:
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()

