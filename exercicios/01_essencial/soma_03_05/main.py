
def resposta(n):
    soma = 0

    for i in range(n):
        divisivel_3 = i % 3 == 0
        divisivel_5 = i % 5 == 0

        if divisivel_3 or divisivel_5:
            soma += i

    return soma
