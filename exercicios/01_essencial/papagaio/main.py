def resposta(falando, hora):
    if falando == True and hora <= 7:
        return True
    elif falando == True and hora >= 20:
        return True
    else:
        return False
