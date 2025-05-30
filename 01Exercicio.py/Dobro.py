def obter_dobro():
    """Função que pede um número ao usuário e retorna o seu dobro."""
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            return numero * 2
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números inteiros.")

# Exemplo de uso da função
dobro = obter_dobro()
print(f"O dobro do número é: {dobro}")