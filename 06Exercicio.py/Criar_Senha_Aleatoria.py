import random
import string

def gerar_senha(tamanho):
    """Função que gera uma senha aleatória com o tamanho especificado."""
    # Definindo os conjuntos de caracteres
    letras_minusculas = string.ascii_lowercase
    letras_maiusculas = string.ascii_uppercase
    digitos = string.digits
    caracteres_especiais = string.punctuation

    # Combinando todos os caracteres
    todos_caracteres = letras_minusculas + letras_maiusculas + digitos + caracteres_especiais

    # Gerando a senha aleatória
    senha = ''.join(random.choice(todos_caracteres) for _ in range(tamanho))
    return senha

def main():
    print("Bem-vindo ao gerador de senhas aleatórias!")
    
    while True:
        try:
            tamanho = int(input("Digite o número de caracteres para a senha (mínimo 8): "))
            if tamanho < 8:
                print("A senha deve ter no mínimo 8 caracteres. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida! Por favor, insira apenas números.")

    senha = gerar_senha(tamanho)
    print(f"Sua senha aleatória é: {senha}")

if __name__ == "__main__":
    main()