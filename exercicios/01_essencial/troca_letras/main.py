def resposta(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + s[1:-1] + s[0]
