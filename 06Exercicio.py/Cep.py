import requests

def consultar_cep(cep):
    """Função que consulta a API ViaCEP e retorna os dados do endereço."""
    url = f"https://viacep.com.br/ws/{cep}/json/" 
    response = requests.get(url)
    
    if response.status_code == 200:
        dados = response.json()
        return dados
    else:
        return None

def main():
    print("Bem-vindo ao consultor de CEP!")
    
    while True:
        cep = input("Digite o CEP (apenas números): ").strip()
        
        # Validação do CEP: deve conter 8 dígitos
        if len(cep) != 8 or not cep.isdigit():
            print("CEP inválido! Digite apenas 8 números.")
            continue
        
        # Consulta a API ViaCEP
        endereco = consultar_cep(cep)
        
        if endereco:
            print("\nEndereço encontrado:")
            print(f"Logradouro: {endereco.get('logradouro', 'Não informado')}")
            print(f"Bairro: {endereco.get('bairro', 'Não informado')}")
            print(f"Cidade: {endereco.get('localidade', 'Não informado')}")
            print(f"Estado: {endereco.get('uf', 'Não informado')}")
        else:
            print("CEP não encontrado. Tente novamente.")
        
        # Pergunta se deseja realizar outra consulta
        opcao = input("\nDeseja consultar outro CEP? (s/n): ").strip().lower()
        if opcao != 's':
            print("Programa encerrado.")
            break

if __name__ == "__main__":
    main()