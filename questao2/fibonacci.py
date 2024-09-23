def fibonacci(n):
    vetor= [0,1]

    while vetor[-1] < n:
        proximo_valor = vetor[-1] + vetor[-2]
        vetor.append(proximo_valor)

    if n in vetor:
        return "o valor informado está contido na sequencia de fibonacci"
    else:
        return "o valor informado nao esta contido na sequencia de fibonacci"

valor = int(input("Digite um numero "))
resultado = fibonacci(valor)
print(resultado)
input()
