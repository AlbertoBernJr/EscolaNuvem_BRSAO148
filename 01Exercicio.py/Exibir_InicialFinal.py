def main():
    print("Bem-vindo ao gerador de sequências numéricas!")

    while True:
        try:
            # Solicita ao usuário o número inicial
            inicio = int(input("Digite o número inicial: "))
            
            # Solicita ao usuário o número final
            fim = int(input("Digite o número final: "))

            # Verifica se o número inicial é menor ou igual ao final
            if inicio > fim:
                print("O número inicial deve ser menor ou igual ao número final. Tente novamente.")
                continue  # Reinicia o loop para tentar novamente

            # Exibe a sequência
            print(f"Sequência do número {inicio} até {fim}:")
            numero = inicio
            while numero <= fim:
                print(numero)
                numero += 1

            break  # Sai do loop após a sequência ser exibida

        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números inteiros.")

if __name__ == "__main__":
    main()