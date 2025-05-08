def numero():
    while True:
        try:
            valor=input("Entre com o número que iniciará a sequencia: ")
            
            if not valor.strip(): #verificar se a string [n1] esta vazio
            # -> se for verdadeira, a condição do [ if ] é iniciada
            # -> se estiver vazia, retorna [ False ]
            # -> se estiver com algum valor, retorna [ True ]
                print("Nome não pode estar vazio! Tente novamente. ")
                continue

            n1=int(valor)

            print(f"1° valor digitado foi: {n1}")
            return n1
   
        except ValueError:  # Captura apenas erros de conversão para int
            print("Erro: Digite um número inteiro válido!")
        
        except Exception as e: #outros erros genéricos
            print(f"Ocorreu um erro inesperado: {e}")
            #exit() #encerra a execução do programa imediatamente

def seq(n1):
    n1=i
    for i in range(0, i):
        print(i)

n1 = numero()
seq(n1)
