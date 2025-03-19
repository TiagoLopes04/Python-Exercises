from re import sub

def camel_case(s):
    # Uso de expressoes reguralres para subtituir - e _ por espaços
    # .title() para colocar em maiusculas a 1ª letra de cada palavra
    #.relace(" ", "") para eliminar os espaços
    s = sub(r"(_|-)+", " ", s).title().replace(" ", "")

    # altera a primeira letra para minuscula e mantem o resto inalterado
    return ''.join([s[0].lower(), s[1:]])


frase=input("Qual a string a converter para camel case?")
print(camel_case(frase))