def classificar_idade(idade):
    """Função que classifica a idade em uma das categorias."""
    if 0 <= idade <= 12:
        return "Criança"
    elif 13 <= idade <= 17:
        return "Adolescente"
    elif 18 <= idade <= 59:
        return "Adulto"
    elif idade >= 60:
        return "Idoso"
    else:
        return "Idade inválida"

def main():
    print("Bem-vindo ao sistema de classificação etária!")
    
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if idade < 0:
                print("Idade não pode ser negativa. Tente novamente.")
                continue
            categoria = classificar_idade(idade)
            print(f"Você é classificado como: {categoria}")
            break
        except ValueError:
            print("Entrada inválida! Por favor, insira apenas números.")

if __name__ == "__main__":
    main()