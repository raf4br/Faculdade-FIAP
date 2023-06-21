def jogar():
    print("**************************")
    print("BEM VINDO AO JOGO DA FORCA")
    print("**************************")

    print("FIM DE JOGO")

    #variaveis
    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    #enquanto não enforcou e não acertou
    while (not enforcou and not acertou):
        chute = input("Qual a letra ?")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {} da palavra secreta".
                      format(letra, index))
            index = index + 1


if (__name__ == "__main__"):
    jogar()