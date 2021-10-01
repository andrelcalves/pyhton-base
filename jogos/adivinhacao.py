print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

# função input é usada para obter um valor externo com interação no console, o input sempre devolve uma string
# por isso será necessário converter com a função int para compara inteiro

palpite = int(input("Digite o seu número: "))
print("Você digitou", palpite)

if(palpite == numero_secreto):
    print("Você acertou")
else:
    print("Você erro o número")