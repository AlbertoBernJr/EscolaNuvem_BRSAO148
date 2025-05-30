def verificar_par_impar():
    """
    Solicita um número ao usuário e verifica se é par ou ímpar.
    """
    try:
        numero = int(input("Digite um número inteiro: "))
        if numero % 2 == 0:
            print(f"O número {numero} é PAR. 👍")
        else:
            print(f"O número {numero} é ÍMPAR. 👎")
    except ValueError:
        print("Erro: Por favor, insira um número inteiro válido. 😬")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e} 🤯")

# Chama a função para iniciar o programa
verificar_par_impar()