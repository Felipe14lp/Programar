while True:
    resposta = input("Você é o usuário? (Sim/Não): ").strip().lower()
    if resposta == "sim":
        print("Confirmado você é um usuário!")
        break
    elif resposta == "não" or resposta == "nao":
        print("Confirmado você não é o usuário.")
        break
    else:
        print("Digite apenas Sim ou Não.")