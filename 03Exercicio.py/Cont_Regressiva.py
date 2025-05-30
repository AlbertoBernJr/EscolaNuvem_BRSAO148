def contagem_regressiva():
    print("Bem-vindo à contagem regressiva!")
    
    while True:
        try:
            numero = int(input("Digite um número inteiro positivo para iniciar a contagem: "))
            if numero < 0:
                print("Por favor, digite um número inteiro positivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida! Por favor, insira apenas números.")

    while numero >= 0:
        print(numero)
        numero -= 1

    print("FIM!")

if __name__ == "__main__":
    contagem_regressiva()