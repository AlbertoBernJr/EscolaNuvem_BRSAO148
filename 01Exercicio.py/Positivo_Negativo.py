def verificar_positivo_negativo():
    """Função que verifica se um número é positivo ou negativo."""
    while True:
        try:
            numero = float(input("Digite um número: "))
            if numero > 0:
                print("O número é positivo.")
            elif numero < 0:
                print("O número é negativo.")
            else:
                print("O número é zero.")
            break
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")

# Executa a função
verificar_positivo_negativo()