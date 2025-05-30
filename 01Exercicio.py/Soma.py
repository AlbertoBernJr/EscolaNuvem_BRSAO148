def somar_dois_numeros_com_while():
    """
    Solicita dois números ao usuário, utilizando 'while' para garantir
    entradas válidas, e calcula a soma deles.
    """
    num1 = None
    num2 = None

    # Loop para obter o primeiro número válido
    while num1 is None:
        try:
            entrada_num1 = input("Digite o primeiro número: ")
            num1 = float(entrada_num1)  # Tenta converter para float
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido para o primeiro valor.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    # Loop para obter o segundo número válido
    while num2 is None:
        try:
            entrada_num2 = input("Digite o segundo número: ")
            num2 = float(entrada_num2)  # Tenta converter para float
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido para o segundo valor.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    # Calcula a soma
    soma = num1 + num2

    # Mostra o resultado
    print(f"A soma de {num1} e {num2} é igual a {soma}.")

# Chama a função para iniciar o programa
somar_dois_numeros_com_while()