import random
import main


def ___dificuldadedificil___():

    print("************************************")
    print("BEM VINDO AO JOGO DE ADVINHAÇÃO")
    print("\tNIVEL DIFICIL\t")
    print("************************************")
    inicio()


def inicio():

    chute = 0
    tentativas = 3
    numero = 0
    int(numero)
    int(tentativas)

    # randomizando os numeros com 20 ranges de 1 a 20 numeros
    for i in range(20):
        numero = random.randint(1, 20)

    # comparando os valores para enserir dentro do laço
    comparando = chute != numero
    int(comparando)

    # iniciando o laço de repetição
    while comparando:
        if (tentativas == 0):
            print("************************************")
            print("\tSuas chances acabaram !\t")
            print("************************************")
            main.menu()
            continue

        # menu de tentativas
        print("\n**********************************")
        print("numeros de tentativas restantes: {}".format(tentativas))
        print("numero secreto: {}".format(numero))
        chute = int(input("Por favor, digite um numero:"))
        print("**********************************\n")
        maior = chute > numero
        menor = chute < numero
        acertou = chute == numero

        int(maior)
        int(menor)
        int(acertou)

        if (chute > 20 or chute < 1):
            print(
                "Seu numero foi {} digite apenas numeros entre 1 a 20!".format(
                    chute))
            continue

        # condições
        if (acertou):
            print("você digitou o numero:{} e você Acertou !!\n".format(chute))
            main.menu()
        else:
            if (maior):
                print(
                    "você digitou o numero:{} e você errou .... tente colocar um numero menor!!\n"
                    .format(chute))
            elif (menor):
                print(
                    "você digitou o numero:{} e você errou .... tente colocar um numero maior!!\n"
                    .format(chute))
        tentativas = tentativas - 1
