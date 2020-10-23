import random

# Function statement.
def password_generator():
    capital_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
    lowercase      = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    symbols        = ['!', '#', '$', '&', '/', '(', ')', '"', '@', '|', '°', '=', '?', '¡', ';', ':', ',', '.', '-', '{', '}', '[', ']', '´', '+', '¨', '*', '_', '>','<']
    numbers        = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    characters = capital_letter + lowercase + symbols + numbers
    password = []
    
    # Size of Password
    for i in range(15):
        character_random = random.choice(characters)
        password.append(character_random)
    password = "".join(password)
    return password

# Execution.
def run():
    password = password_generator()
    print('I can suggest this password: ' + password)

if __name__ == '__main__':
    run()
