import facil
import medio
import dificil

dificuldade = 0
int(dificuldade)


def dificuldades(dificuldade):
    if (dificuldade == 1):
        facil.dificuldade_easy()
    elif (dificuldade == 2):
        medio.___dificuldademedio___()
    elif (dificuldade == 3):
        dificil.___dificuldadedificil___()
    else:
        print("\n*************--AVISO--*****************")
        print("Por gentileza, selecione de 1 a 3")
        print("\n***********--AVISO--*****************\n")
        menu()


def menu():
    print("************************************")
    print("BEM VINDO AO JOGO DE ADVINHAÇÃO")
    print("Escolha o Nível de dificuldade")
    print("(1) FÁCIL    (2) MÉDIO   (3) DIFÍCIL")
    print("************************************")
    dificuldade = int(input("OPÇÃO: "))
    dificuldades(dificuldade)


menu()
