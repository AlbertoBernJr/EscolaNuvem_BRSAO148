def numero():
    while True:
        try:
            valor1=input("Entre com o 1° número inteiro: ")
            
            if not valor1.strip(): #verificar se a string [n1] esta vazio
            # -> se for verdadeira, a condição do [ if ] é iniciada
            # -> se estiver vazia, retorna [ False ]
            # -> se estiver com algum valor, retorna [ True ]
                print("Nome não pode estar vazio! Tente novamente. ")
                continue
            
            valor2=input("Entre com o 2° número inteiro: ")
            
            if not valor2.strip():
                print("Nome não pode estar vazio! Tente novamente. ")
                continue
            
            n1=int(valor1)
            n2=int(valor2)
            
            print(f"1° valor digitado foi: {n1}")
            print(f"2° valor digitado foi: {n2}")
            return n1, n2
            
            
            
        except ValueError:  # Captura apenas erros de conversão para int
            print("Erro: Digite um número inteiro válido!")
        
        except Exception as e: #outros erros genéricos
            print(f"Ocorreu um erro inesperado: {e}")
            #exit() #encerra a execução do programa imediatamente

def media(n1, n2):
    while True:
        try:
            media=(n1+n2)/2
            print(f"A média entre {n1} e {n2} = {media}")
            return media
        
        except Exception as e: #outros erros genéricos
            print(f"Ocorreu um erro inesperado: {e}")
            

        
n1, n2 = numero()
media(n1, n2)