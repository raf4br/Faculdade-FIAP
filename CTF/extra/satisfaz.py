import random


# Retirado do código original com as condições para satisfazer o if.
def checkserial(d1, d2, d3, d4, d5, d6, d7, d8):
    if d1 + d3 + d5 + d7 == 12 and d2 + d4 + d6 + d8 == 11 and d2 * d3 * d7 == 24 and d1 * d2 * d3 * d5 == 60 and d7 - d2 + d3 - d4 == 0 and d6 + d1 + d8 == 10 and d8 > 3:
        flag = f"fiap{{{d1}{d2}{d3}{d4}{d5}{d6}{d7}{d8}}}"
        return flag
    else:
        return False

# aqui fica o gerador de numeros, onde ele faz o bruteforce,
# quando ele satisfaz o if, retorna a flag printada na tela


def gerador_de_numeros():
    while True:
        d1, d2, d3, d4, d5, d6, d7, d8 = random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1, 6)
        flag = checkserial(d1, d2, d3, d4, d5, d6, d7, d8)
        if flag:
            print(f"A flag é {flag}")
            print(d1,d2,d3,d4,d5,d6,d7,d8)
            break


gerador_de_numeros()
