def resposta(n):
    divisivel_3 = n % 3 == 0
    divisivel_5 = n % 5 == 0
    divisivel_3_5 = divisivel_3 and divisivel_5

    if divisivel_3_5:
        return "FizzBuzz"
    elif divisivel_3:
        return "Fizz"
    elif divisivel_5:
        return "Buzz"
    else:
        return n
