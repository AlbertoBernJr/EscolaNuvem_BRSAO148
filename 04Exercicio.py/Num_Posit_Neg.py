def main():
    print("Digite números inteiros (digite 0 para encerrar):")
    
    positivos = []
    negativos = []

    while True:
        try:
            numero = int(input("Digite um número: "))
            if numero == 0:
                break
            elif numero > 0:
                positivos.append(numero)
            else:
                negativos.append(numero)
        except ValueError:
            print("Valor inválido! Por favor, insira apenas números inteiros.")

    print(f"\nQuantidade de números positivos: {len(positivos)}")
    print(f"Quantidade de números negativos: {len(negativos)}")

if __name__ == "__main__":
    main()