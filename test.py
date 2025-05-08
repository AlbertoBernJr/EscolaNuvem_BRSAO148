def numero():
    while True:
        try:
            valor1 = input("Entre com o 1° número inteiro: ").strip()
            if not valor1:
                print("Número não pode estar vazio! Tente novamente.")
                continue

            valor2 = input("Entre com o 2° número inteiro: ").strip()
            if not valor2:
                print("Número não pode estar vazio! Tente novamente.")
                continue

            n1 = int(valor1)
            n2 = int(valor2)

            print(f"1° valor digitado foi: {n1}")
            print(f"2° valor digitado foi: {n2}")
            return n1, n2

        except ValueError:
            print("Erro: Digite um número inteiro válido!")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

def calcula(n1, n2):
    while True:
        try:
            print("\nOperações disponíveis:")
            print("Adição [1], Subtração [2] e Multiplicação [3]")
            escolha = input("Escolha uma opção de cálculo (ou 's' para sair): ").strip().lower()

            if escolha == "1":
                resultado = n1 + n2
                print(f"\nO resultado da adição é: {resultado}")
                break

            elif escolha == "2":
                resultado = n1 - n2
                print(f"\nO resultado da subtração é: {resultado}")
                break

            elif escolha == "3":
                resultado = n1 * n2
                print(f"\nO resultado da multiplicação é: {resultado}")
                break

            elif escolha == 's':
                print("Saindo...")
                break

            else:
                print("Opção inválida! Escolha entre as opções 1, 2, 3 ou 's' para sair.")

        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

# Chamando as funções
if __name__ == "__main__":
    n1, n2 = numero()
    calcula(n1, n2)
