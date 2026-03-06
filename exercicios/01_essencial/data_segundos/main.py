def resposta(dias, horas, minutos, segundos):
    return (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos

print(resposta(10, 13, 1, 15))
