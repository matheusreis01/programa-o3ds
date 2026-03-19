import random

# Configurações iniciais
numero_secreto = random.randint(1, 10)
tentativas_restantes = 5
ganhou = False

print("--- Bem-vindo ao Jogo de Adivinhação! ---")
print("Tente adivinhar o número entre 1 e 10.")

# Usamos o while porque o número de tentativas pode mudar dinamicamente
while tentativas_restantes > 0:
    print(f"\nVocê tem {tentativas_restantes} tentativa(s).")
    
    try:
        chute = int(input("Digite seu palpite: "))
    except ValueError:
        print("Por favor, digite apenas números inteiros.")
        continue

    if chute == numero_secreto:
        print(f"Parabéns! Você acertou o número {numero_secreto}!")
        ganhou = True
        break # Sai do loop imediatamente se acertar
    
    else:
        # Lógica do Bônus: verifica se a diferença é de apenas 1 unidade
        # Usamos abs() para pegar o valor absoluto da diferença
        if abs(chute - numero_secreto) == 1:
            print("Quase lá! Você chegou muito perto e ganhou +1 tentativa de bônus!")
            # O bônus anula a perda da tentativa atual
        else:
            print("Errou!")
            tentativas_restantes -= 1 # Só diminui a tentativa se não ganhar bônus

if not ganhou:
    print(f"\nGame Over! O número era {numero_secreto}.")
