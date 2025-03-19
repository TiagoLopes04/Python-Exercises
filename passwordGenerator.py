import random
import string

def generate_password():
    #criar os possiveis caracteres para a password
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    #unificar todos em apenas uma variavel
    chars = letters + numbers + symbols

    password=""

    #criar o tamanho da password
    number_of_chars = random.randint(12, 30)

    #criar a password, escolhe um cacter em chars e adiciona a password number_of_chars vezes
    for i in range(number_of_chars):
        password+=random.choice(chars)


    return password

print(generate_password())
