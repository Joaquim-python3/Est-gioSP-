#funcao de inverter uma string

def inverterString(str):
    str_invertida =""
    for char in str:
        str_invertida = char + str_invertida
    return str_invertida

value = input("Digite a palavra: ")
print(inverterString(value))
