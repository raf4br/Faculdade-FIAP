print("""seja bem vindo ao curso de python
      aqui vamos falar sobre a interação do python na sociedade.
      
      Por gentileza, nos informe seu nome e a sua idade!""")

sleep: 5

nome = str(input("Digite eu nome: "))
idade = int(input("Nos informe sua idade: "))

print(
    """ Olá {nome1}, seja bem vindo. constatamos que você possui {idade1} anos. """
    .format(nome1=nome, idade1=idade))
