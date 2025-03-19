import random
import string

def generate_password():
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    password_list = []

    number_of_letters = random.randint(5, 10)
    number_of_symbols = random.randint(5, 10)
    number_of_numbers = random.randint(5, 10)

    for i in range(number_of_letters):
        password_list.append(random.choice(letters))

    for i in range(number_of_symbols):
        password_list.append(random.choice(symbols))

    for i in range(number_of_numbers):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)

    password = "".join(password_list)
    print(password)

generate_password()
