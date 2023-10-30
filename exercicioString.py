# a) Leia uma frase qualquer
frase = (input("Digite uma frase: "))

# b) Escreva a frase lida na vertical
def fraseVertical(frase):

    novaFrase = ""

    for i in frase:
            novaFrase = novaFrase + i + "\n"

    return novaFrase

#fraseVertical(frase)


# c) Escreva a frase na diagonal
def fraseDiagonal(frase):
      
    espacos = ""
    novaFrase = ""

    for i in frase:

        novaFrase = novaFrase + espacos + i + "\n"
        espacos = espacos + " "
    
    return novaFrase
        
#fraseDiagonal(frase)
        

# d) Escreva a frase na diagonal invertida
def fraseDiagonalInvertida(frase):
      
    espacos = " "
    quatidadeEspacos = len(frase)
    novaFrase = ""

    for  i in frase:
        novaFrase = novaFrase + espacos * quatidadeEspacos + i + "\n"
        quatidadeEspacos = quatidadeEspacos - 1

    return novaFrase
#fraseDiagonalInvertida(frase)

              
# e) Escreva a frase na ordem contrária
def fraseInvertida(frase):

    fraseInvertida = ""

    for i in frase:
        fraseInvertida = i + fraseInvertida

    print(fraseInvertida)
    return fraseInvertida

#fraseInvertida(frase)


# f) Escreva a frase sem espaço em branco
def fraseSemEspacoBranco(frase):
    fraseSemEspaco = ""
    for i in frase:
        if i != " ":
            fraseSemEspaco = fraseSemEspaco + i

    print(fraseSemEspaco)

#fraseSemEspacoBranco(frase)


# g) Escreva a frase sem vogais
def fraseSemVogais(frase):
    fraseSemVogais = ""
    for i in frase:
        if i != "a" and i != "e" and i != "i" and i != "o" and i != "u":
            fraseSemVogais = fraseSemVogais + i

    print(fraseSemVogais)

#fraseSemVogais(frase)


# h) Escreva a frase substituindo as vogais por *
def fraseSubstituindoVogais(frase):
    fraseSubstituindoVogais = ""
    for i in frase:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            fraseSubstituindoVogais = fraseSubstituindoVogais + "*"
        else:
            fraseSubstituindoVogais = fraseSubstituindoVogais + i

    print(fraseSubstituindoVogais)

#fraseSubstituindoVogais(frase)


# i) Informe quantas palavras existem na frase
def quantidadePalavras(frase):
    quantidadePalavras = 1
    for i in frase:
        if i == " ":
            quantidadePalavras = quantidadePalavras + 1

    print("A frase possui", quantidadePalavras, "palavras")

#quantidadePalavras(frase)


# j) Informe a maior palavra existem na frase
def maiorPalavraFrase(frase):
    maiorPalavra = ""
    palavra = ""

    for i in frase:
        if i != " ":
            palavra = palavra + i

        else:
            if len(palavra) > len(maiorPalavra):
                maiorPalavra = palavra
            palavra = "" 

    if palavra > maiorPalavra:
        maiorPalavra = palavra
        
    print("A maior palavra da frase é:", maiorPalavra)

# maiorPalavraFrase(frase)


# k) Leia duas palavras; verifique se a primeira palavra estar presente na frase lida;
#caso esteja substitua pela segunda palavra

def verificarETrocarPalavraFrase(frase):

    palavra1 =  input("Digite a primeira palavra: ")
    palavra2 = input("Digite a segunda palavra: ")
    palavra = ""
    novaFrase = ""

    for i in  frase:

        if i != " ":
            palavra = palavra + i

        else:
            if palavra == palavra1:
                palavra = palavra2
            novaFrase = novaFrase + palavra + " "
            palavra = ""

    if palavra == palavra1: 
        palavra = palavra2 
    novaFrase = novaFrase + palavra + " "

    print(novaFrase)

#verificarETrocarPalavraFrase(frase)
  

# l) Inicie as palavras da frase com letra maiúscula
def tornaLetrasMaiusculas(termo):

    termoModificado = ""

    for i in termo:

        if i == "a":
            i = "A"

        elif i == "b":
            i = "B"
            
        elif i == "c":
            i = "C"

        elif i == "d":
            i = "D"

        elif i == "e":
            i = "E"
            
        elif i == "f":
            i = "F"

        elif i == "g":
                i = "G"

        elif i == "h":
            i = "H"

        elif i == "i":
            i = "I"

        elif i == "j":
            i = "J"

        elif i == "k":
            i = "K"

        elif i == "l":
                i = "L"

        elif i == "m":
            i = "M"

        elif i == "n":
                i = "N"

        elif i == "o":
            i = "O"

        elif i == "p":
            i = "P"

        elif i == "q":
            i = "Q"

        elif i == "r":
            i = "R"

        elif i == "s":
            i = "S"

        elif i == "t":
            i = "T"

        elif i == "u":
            i = "U" 

        elif i == "v":
            i = "V"

        elif i == "w":
            i = "W"

        elif i == "x":
            i = "X"

        elif i == "y":
            i = "Y"

        elif i == "z":
            i = "Z"

        termoModificado = termoModificado + i

    return termoModificado

def tornaLetrasMinusculas(termo):

    termoModificado = ""

    for i in termo:

        if i == "A":
            i = "a"

        elif i == "B":
            i = "b"
            
        elif i == "C":
            i = "c"

        elif i == "D":
            i = "d"

        elif i == "E":
            i = "e"
            
        elif i == "F":
            i = "f"

        elif i == "G":
                i = "g"

        elif i == "H":
            i = "h"

        elif i == "I":
            i = "i"

        elif i == "J":
            i = "j"

        elif i == "K":
            i = "k"

        elif i == "L":
                i = "l"

        elif i == "M":
            i = "m"

        elif i == "N":
                i = "n"

        elif i == "O":
            i = "o"

        elif i == "P":
            i = "p"

        elif i == "Q":
            i = "q"

        elif i == "R":
            i = "r"

        elif i == "S":
            i = "s"

        elif i == "T":
            i = "t"

        elif i == "U":
            i = "u"

        elif i == "V":
            i = "v"

        elif i == "W":
            i = "w"

        elif i == "X":
            i = "x"

        elif i == "Y":
            i = "y"

        elif i == "Z":
            i = "z"

        termoModificado = termoModificado + i

    return termoModificado

def tornarPrimeiraLetraMaiuscula(palavra):
    
    novaPalavra = ""
    contador = 0

    for i in palavra:

        if contador == 0:
            i = tornaLetrasMaiusculas(i)
            novaPalavra = novaPalavra + i
            contador = contador + 1

        else: 
            novaPalavra = novaPalavra + i

    return novaPalavra

def palavrasFraseComLetraMaiuscula(frase):

    fraseLetrasMinusculas = tornaLetrasMinusculas(frase)
    novaFrase = ""
    palavra = ""

    for i in fraseLetrasMinusculas:     

        if i != " ":
            palavra = palavra + i
          
        else: 
            palavra = tornarPrimeiraLetraMaiuscula(palavra)
            novaFrase = novaFrase + palavra + " "
            palavra = ""

    palavra = tornarPrimeiraLetraMaiuscula(palavra)
    novaFrase = novaFrase + palavra + " "

    print(novaFrase)

# palavrasFraseComLetraMaiuscula(frase)


# m) Escreva cada palavra da frase na vertical e a frase na diagonal

def fraseVerticalEDiagonal(frase):
    
    espacos = ""

    for i in frase:
        if i != " ":
            print(espacos + i)

        else:
            espacos = espacos + " "

#fraseVerticalEDiagonal(frase)
        

# n) Leia um caractere qualquer e informe quantas vezes esse caractere foi
#localizado na frase lida.

def quantidadeCaractere(frase):

    caractere = input("Digite um caractere: ")
    quantidadeCaractere = 0

    for i in frase:
        if i == caractere:
            quantidadeCaractere = quantidadeCaractere + 1

    print("O caractere", caractere, "aparece", quantidadeCaractere, "vezes na frase")

#quantidadeCaractere(frase)


# o) Escreva uma palavra da esquerda para direita e a próxima palavra da direita
# para esquerda alternando até o final da frase

def alternarOrdemPalavras(frase):

    contador = 1
    novaFrase = ""
    palavra = ""


    for i in frase:

        if i != " " and contador == 1:
            palavra = palavra + i


        elif i != " " and contador == 2:
            palavra = palavra + i

        else:

            if contador == 1:
                novaFrase = novaFrase + palavra + " "
                palavra = ""
                contador = contador + 1
            else: 
                palavra = fraseInvertida(palavra)
                novaFrase = novaFrase + palavra + " "
                palavra = ""
                contador = 1

    if contador == 1:
        novaFrase = novaFrase + palavra + " "
    else:
        palavra = fraseInvertida(palavra)
        novaFrase = novaFrase + palavra + " "

    print("A frase com as palavras alternadas é:", novaFrase)

#alternarOrdemPalavras(frase) 


# p) Escreva a frase apenas com as vogais em maiúsculo

def vogaisMaiusculo(frase):

    fraseMinuscula = tornaLetrasMinusculas(frase)
    novaFrase = ""

    for i in fraseMinuscula:

        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            i = tornaLetrasMaiusculas(i)

        novaFrase = novaFrase + i

    print(novaFrase)

#vogaisMaiusculo(frase)


# q) Separe as silabas da frase. PS: Considerar apenas palavra com sílabas de
# dois caracteres.

def separarSilabasFrase(frase):

    contador = 1
    novaFrase = ""
    silaba = ""


    for i in frase:

        if i != " ":

            if contador == 1:
                silaba = silaba + i
                contador = contador + 1


            else: 
                silaba = silaba + i
                novaFrase = novaFrase + silaba + "-"
                silaba = ""
                contador = 1

        else:
            novaFrase = novaFrase + silaba + " "
            silaba = ""
            contador = 1

    novaFrase = novaFrase + silaba 

    print("A frase com as silabas separadas é:", novaFrase)

#separarSilabasFrase(frase)


# r) Informe a última posição que existe uma vogal

def ultimaPosicaoVogal(frase):

    contador = 0

    for i in frase:

        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            contador = contador + 1
            ultimaPosicao = contador

        else:
            contador = contador + 1

    print("A última posição que existe uma vogal é:", ultimaPosicao)    

#ultimaPosicaoVogal(frase)
    

# s) Some os índices de todos os caracteres não vogais.

def somaIndicesVogais(frase):

    contador = 0
    somaIndices = 0

    for i in frase:

        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            contador = contador + 1

        else:
            contador = contador + 1
            somaIndices = somaIndices + contador


    print("A soma dos índices de todos os caracteres não vogais é:", somaIndices)

#somaIndicesVogais(frase)


# t) Informe a palavra central em frases com quantidade de palavras impares

# def palavraCentralFraseImpar(frase):



# u) Escreva a primeira e última palavra na diagonal

def primeiraEUltimaFraseDiagonal(frase):

    contador = 1
    palavra = ""
    novaFrase = ""

    for i in frase:

        if i != " ":
            palavra = palavra + i
        
        else:
            if contador == 1:
                novaFrase = novaFrase + fraseDiagonal(palavra) + " "
                palavra = ""
                contador = 0

            else:
                novaFrase = novaFrase + palavra + " "
                palavra = ""

    novaFrase = novaFrase + "\n" + fraseDiagonal(palavra)

    print(novaFrase)
        
#primeiraEUltimaFraseDiagonal(frase)


# v) Criptografe a frase lida

def fraseCriptografada(frase):

    novaFrase = ""

    for i in frase:

        if i == 'a':
            i = '*'
            novaFrase = novaFrase + i

        elif i == 'e':
            i = '&'
            novaFrase = novaFrase + i

        
        elif i == 'i':
            i = '%'
            novaFrase = novaFrase + i

        
        elif i == 'o':
            i = '$'
            novaFrase = novaFrase + i

        
        elif i == 'u':
            i = '#'
            novaFrase = novaFrase + i

        else:
            novaFrase = novaFrase + i

    print(novaFrase)

#fraseCriptografada(frase)


# w) Descriptografe a frase lida

def fraseDescriptografada(frase):

    print("Frase criptografada:",frase)
    novaFrase = ""

    for i in frase:

        if i == '*':
            i = 'a'
            novaFrase = novaFrase + i

        elif i == '&':
            i = 'e'
            novaFrase = novaFrase + i

        
        elif i == '%':
            i = 'i'
            novaFrase = novaFrase + i

        
        elif i == '$':
            i = 'o'
            novaFrase = novaFrase + i

        
        elif i == '#':
            i = 'u'
            novaFrase = novaFrase + i

        else:
            novaFrase = novaFrase + i

    print("Frase descriptografada: ", novaFrase)

#fraseDescriptografada(frase)


# x) Escreva a primeira palavra e a última na vertical

def primeiraEUltimaFraseVertical(frase):

    contador = 1
    palavra = ""
    novaFrase = ""

    for i in frase:

        if i != " ":
            palavra = palavra + i
        
        else:
            if contador == 1:
                novaFrase = novaFrase + fraseVertical(palavra) + " "
                palavra = ""
                contador = 0

            else:
                novaFrase = novaFrase + palavra + " "
                palavra = ""

    novaFrase = novaFrase + "\n" + fraseVertical(palavra)

    print(novaFrase)

#primeiraEUltimaFraseVertical(frase)


# y) Escreva a primeira palavra na diagonal e a última na diagonal invertida

def primeiraDiagonalUltimaDiagonalInvertida(frase):

    contador = 1
    palavra = ""
    novaFrase = ""

    for i in frase:

        if i != " ":
            palavra = palavra + i
        
        else:
            if contador == 1:
                novaFrase = novaFrase + fraseDiagonal(palavra) + " "
                palavra = ""
                contador = 0

            else:
                novaFrase = novaFrase + palavra + " "
                palavra = ""

    novaFrase = novaFrase + "\n" + fraseDiagonalInvertida(palavra)

    print(novaFrase)

#primeiraDiagonalUltimaDiagonalInvertida(frase)


# z) Crie uma questão particular usando manipulação de string.
# z) Trocar todas as letras i por #

def trocarLetraI(frase):

    novaFrase = ""

    for i in frase:
        
        if i == "i":
            i = "#"
            novaFrase = novaFrase + i

        else:
            novaFrase = novaFrase + i

    print(novaFrase)

#trocarLetraI(frase)
