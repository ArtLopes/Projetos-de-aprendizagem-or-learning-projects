import random
wins_usuario = 0
wins_computador = 0
options = ['Pedra', 'Papel', 'Tesoura']
# while True significa enquanto o jogo estiver sendo jogado

while True:
    input_usuario = input('Digite Pedra/Papel/Tesoura ou Q para sair: ').lower()
    if input_usuario == "q":
        break  # Poderia ser utilizado quit() aqui, mas 'break' encurta o código.
    elif input_usuario in options:  # Asking IF Pedra, Papel or Tesoura exists in input_usuario
        continue
# Choosing a random number

    rng = random.randint(0, 2)
    pc_escolha = options[rng]  # O computador escolhe um indice aleatório na variável options, onde 0 = Pedra...
    print('O computador escolheu', pc_escolha + '.')

# Define as condições de vitória ('win conditions')

    if input_usuario == "pedra" and pc_escolha == "Tesoura":
        print("Você venceu!")
        wins_usuario += 1
    elif input_usuario == "papel" and pc_escolha == "Pedra":
        print("Você venceu!")
        wins_usuario += 1
    elif input_usuario == "tesoura" and pc_escolha == "Papel":
        print("Você venceu!")
        wins_usuario += 1
    else:
        print('Você perdeu!')
        wins_computador += 1

print(f"Você venceu {wins_usuario} vezes, o computador venceu {wins_computador} vezes.")
print("Tchau!")
