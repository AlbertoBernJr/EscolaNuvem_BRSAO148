def calcular_media(notas):
    """Função que calcula a média das notas."""
    return sum(notas) / len(notas)

def main():
    print("Bem-vindo ao sistema de cálculo de médias!")
    
    # Solicita o nome do aluno
    nome = input("Digite o nome do aluno: ").strip()
    
    # Solicita as três notas
    notas = []
    for i in range(3):
        while True:
            try:
                nota = float(input(f"Digite a {i + 1}ª nota: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Nota inválida! Digite um valor entre 0 e 10.")
            except ValueError:
                print("Entrada inválida! Por favor, insira um número.")

    # Calcula a média
    media = calcular_media(notas)
    
    # Exibe a média com duas casas decimais
    print(f"A média do aluno {nome} é: {media:.2f}")

if __name__ == "__main__":
    main()