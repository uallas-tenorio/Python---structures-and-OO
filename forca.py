import random

def jogar():

    texto_indroducao_jogo()

    palavra_secreta = seleciona_palavra_secreta()

    letras_acertadas = monta_items_forca(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(str(letras_acertadas).replace("'","").replace("[","").replace("]","").replace(",",""))
    while(not acertou and not enforcou):
        print("Jogando...")

        chute = solicita_chute()

        posicao_letra = 0

        for letra in palavra_secreta:
            posicao_letra += 1
            if letra == chute:
                letras_acertadas[posicao_letra-1] = chute

            if (str(letras_acertadas).replace("'","").replace("[","").replace("]","").replace(",","").replace(" ","") == palavra_secreta):
                print("Você acertou!")
                acertou = True

        print(str(letras_acertadas).replace("'","").replace("[","").replace("]","").replace(",","").replace(" ",""))

        erros += 1

        print("Faltam {} tentativas!".format(len(palavra_secreta) - erros))

        enforcou = (erros == len(palavra_secreta))

    if (enforcou):
        print("Você não acertou!")
    else:
        print("Você acertou!")

    print("Fim do jogo")

def texto_indroducao_jogo():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def seleciona_palavra_secreta():
    with open("Palavras_Forca.txt", "r") as arquivo:
        lista_palavras = []
        for linha in arquivo:
            linha = linha.strip()
            lista_palavras.append(linha)

    #arquivo.close()  replaced by the 'with' command

    num_aleatorio = random.randrange(0,len(lista_palavras))

    palavra_secreta = lista_palavras[num_aleatorio].upper()

    return palavra_secreta

def monta_items_forca(palavra):
    return ["_" for letra in palavra]

def solicita_chute():
    return input("Qual a letra?").upper().strip()

if(__name__ == "__main__"):
    jogar()
