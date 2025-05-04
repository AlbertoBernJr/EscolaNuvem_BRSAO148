def nome_usuario():
    """
    Solicita o nome do usuário com tratamento de erros e validação.
    Retorna o nome válido ou encerra o programa em caso de cancelamento.
    """
    while True:
        try:
            nome = input("Digite o seu nome: ").strip()
            if not nome:
                print("Erro: O nome não pode estar vazio. Tente novamente!")
                continue
            print(f"Bem-vindo, {nome}!!")
            return nome
        except KeyboardInterrupt:
            print("\nOperação cancelada pelo usuário.")
            exit()
        except Exception as e:
            print(f"Erro inesperado: {e}")
            exit()

# Chamada da função
nome = nome_usuario()
