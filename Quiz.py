# Jogo de perguntas e respostas
print("Bem vindo ao meu quiz de jogos! Use somente letras minúsculas, por favor.")
quer_jogar = input("Você quer jogar? ")

if quer_jogar != "sim":
    print("Então vá se catar.")
    quit()
else:
    print("Ok, vamos lá. Capitalize suas respostas!")

resposta = input("Como se chama a franquia Resident Evil no Japão? ")

if resposta == "biohazard":
    print("Acertou! Vamos para a próxima.")
else:
    print("Que pena. você errou.")
    quit()

resposta_2 = input("Qual é o jogo mais vendido do mundo? ")

if resposta_2 == "tetris":
    print("Parabéns, certo de novo. ")
else:
    print("É uma pena que tenha errado. Tente de novo!")
    quit()

resposta_3 = (input("Última pergunta: qual jogo originou a expressão 'sus''? "))

if resposta_3 == "amogus":
    print("Você zerou o jogo! Mas ainda vou fechar ele na sua cara.")
    quit()
else:
    print("Você errou. Verifique a ortografia de sua resposta! ;)")
    quit()
