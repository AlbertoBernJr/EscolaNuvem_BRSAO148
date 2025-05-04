#Solitar nome do usuário

def nome_usuario():
    while True: #O programa seguirá perguntando o nome de usuário até que 
                #   um valor válido seja inserido
        try:
            nome=input("Digite o seu nome:")
            if not nome.strip(): 
                #[strip()]= remove os espaços em branco/vazios
                #[if not nome.strip()]= verifica se a string [nome] esta vazia 
                #   -> se for verdadeira, a condição do [ if ] é iniciada
                #   -> se estiver vazia, retorna [ False ]
                #   -> se estiver com algum valor, retorna [ True ]

                print("Nome não pode estar vazio! Tente novamente. ")
                continue #usado em loops [For e While] para pular a iteração atual e 
                            #iniciar a próxima iteração do loop
                        # -> se o usuário não entrar com um valor válido, o loop 
                        # voltará ao início, solicitando o nome

            print(f"Seja bem vindo {nome}!!")
            return nome

        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            exit() #encerra a execução do programa imediatamente
    
nome = nome_usuario()