def resposta(palavra, index):
    return palavra[:index] + palavra[index+1:]

print(resposta('kitten', 4))
