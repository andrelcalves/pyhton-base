print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
numero_rodada  = 1
numero_tentativas = 3

# função input é usada para obter um valor externo com interação no console, o input sempre devolve uma string
# por isso será necessário converter com a função int para compara inteiro

while(numero_rodada <= numero_tentativas):
    print("------------------------------------")
    print("Você está na rodada", numero_rodada, "de", numero_tentativas)
    palpite = int(input("Digite o seu número: "))
    print("Você digitou", palpite)

    acertou         = palpite == numero_secreto
    palpite_maior   = palpite > numero_secreto
    palpite_menor   = palpite < numero_secreto

    if(acertou):
        print("Você acertou")
    else:
        if(palpite_maior):
            print("Você erro o número, seu palpite foi maior que o número secreto")
        elif(palpite):
            print("Vocë erro o número, seu palpite foi menor que o número secreto")
    numero_rodada = numero_rodada + 1

print("Fim do jogo!")

#     Merge dictionaries in a single readable line
#     This is available as of Python 3.9:
first_dictionary  = {'primeiro_nome': 'Joao', 'localizacao': 'Munich'}
second_dictionary = {'primeiro_nome': 'Joao', 'segundo_nome': 'Morina','localizacao': 'Bavaria, Munich'}
result = first_dictionary | second_dictionary
print(result)