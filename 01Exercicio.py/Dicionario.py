def main():
    print("Bem-vindo ao sistema de cadastro de países e capitais!")

    # Pergunta ao usuário quantos países ele deseja cadastrar
    while True:
        try:
            quantidade_paises = int(input("Quantos países você deseja cadastrar? "))
            if quantidade_paises <= 0:
                print("Por favor, insira um número maior que zero.")
                continue
            break
        except ValueError:
            print("Entrada inválida! Por favor, insira apenas números.")

    # Inicializa o dicionário para armazenar os países e suas capitais
    paises_capitais = {}

    # Loop para coletar os dados dos países
    for i in range(quantidade_paises):
        print(f"\nCadastro do país {i + 1}:")
        pais = input("Digite o nome do país: ").strip()
        capital = input("Digite a capital do país: ").strip()

        # Verifica se o país já foi cadastrado
        if pais in paises_capitais:
            print("Esse país já foi cadastrado. Tente novamente.")
            continue

        paises_capitais[pais] = capital

    # Opção para consultar a capital de um país
    while True:
        print("\nDeseja consultar a capital de algum país?")
        opcao = input("Digite 's' para sim ou 'n' para não: ").strip().lower()

        if opcao == 's':
            pais_consultado = input("Digite o nome do país: ").strip()
            if pais_consultado in paises_capitais:
                print(f"A capital de {pais_consultado} é {paises_capitais[pais_consultado]}.")
            else:
                print("País não encontrado no cadastro.")
        elif opcao == 'n':
            print("Obrigado por usar o sistema!")
            break
        else:
            print("Opção inválida. Digite 's' para sim ou 'n' para não.")

if __name__ == "__main__":
    main()