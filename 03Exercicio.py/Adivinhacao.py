import random

def main():
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número escolhido pelo computador (entre 1 e 5). Você tem 3 tentativas.")

    # O computador escolhe um número aleatório entre 1 e 5
    numero_secreto = random.randint(1, 5)

    for tentativa in range(1, 4):
        try:
            palpite = int(input(f"Tentativa {tentativa}: Digite seu palpite: "))
            if palpite < 1 or palpite > 5:
                print("Por favor, digite um número entre 1 e 5.")
                continue

            if palpite == numero_secreto:
                print(f"Parabéns! Você acertou na {tentativa}ª tentativa.")
                break
            elif palpite < numero_secreto:
                print("O número secreto é maior.")
            else:
                print("O número secreto é menor.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro.")

    else:
        # Se o loop terminar sem break, significa que o usuário não acertou
        print(f"Você esgotou suas 3 tentativas. O número secreto era {numero_secreto}.")

if __name__ == "__main__":
    main()