from datetime import datetime

def calcular_idade_em_dias(ano_nascimento):
    """Função que calcula a idade de uma pessoa em dias."""
    ano_atual = datetime.now().year
    if ano_nascimento > ano_atual:
        return "O ano de nascimento não pode ser maior que o ano atual."
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365  # Aproximação simplificada (sem considerar anos bissextos)
    return idade_dias

def main():
    print("Bem-vindo ao calculador de idade em dias!")
    
    while True:
        try:
            ano_nascimento = int(input("Digite o ano de nascimento da pessoa: "))
            resultado = calcular_idade_em_dias(ano_nascimento)
            
            if isinstance(resultado, str):
                print(resultado)
            else:
                print(f"A idade da pessoa é aproximadamente {resultado} dias.")
            break
        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro.")

if __name__ == "__main__":
    main()