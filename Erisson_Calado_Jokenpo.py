print("Digite o nome do 1° jogador:")
nome1 = input()
print("Bem-vindo, ", nome1)

print("Digite o nome do 2° jogador:")
nome2 = input()
print("Bem-vindo, ", nome2)

lista = ("Pedra", "Papel", "Tesoura")

pontos1 = 0
pontos2 = 0
count = 1

while count > 0:
    count = count+1
    if (pontos1 == 2) or (pontos2 == 2):
        break
    jogador1 = int(input('''Escolha uma opcao para se jogar:\n[0] Pedra\n[1] Papel\n[2] Tesoura\n
Digite sua escolha: '''))

    jogador2 = int(input('''Escolha uma opcao para se jogar:\n[0] Pedra\n[1] Papel\n[2] Tesoura\n
Digite sua escolha: '''))

    if jogador1 == 0:
        if jogador2 == 0:
            print("Empate!",)
        elif jogador2 == 1:
            print(nome2, "venceu a rodada")
            pontos2 = pontos2+1
        elif jogador2 == 2:
            print(nome1, "venceu a rodada")
            pontos1 = pontos1+1
        else:
            print("Operação inválida")

    if jogador1 == 1:
        if jogador2 == 1:
            print("Empate!")
        elif jogador2 == 0:
            print(nome1, "venceu a rodada")
            pontos1 = pontos1+1
        elif jogador2 == 2:
            print(nome2, "venceu a rodada")
            pontos2 = pontos2+1
        else:
            print("Operação inválida")

    if jogador1 == 2:
        if jogador2 == 2:
            print("Empate!")
        elif jogador2 == 0:
            print(nome2, "venceu a rodada")
            pontos2 = pontos2+1
        elif jogador2 == 1:
            print(nome1, "venceu a rodada")
            pontos1 = pontos1+1
        else:
            print("Operação inválida")

if pontos2 == 2:
    print(nome2, "venceu por ", pontos2, "a", pontos1, "de", nome1)
if pontos1 == 2:
    print(nome1, "venceu por ", pontos1, "a", pontos2, "de", nome2)
