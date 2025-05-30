def verificar_senha_forte(senha):
    """Verifica se a senha é forte (pelo menos 8 caracteres e contém pelo menos um número)."""
    if len(senha) < 8:
        return False, "A senha deve ter pelo menos 8 caracteres."
    if not any(char.isdigit() for char in senha):
        return False, "A senha deve conter pelo menos um número."
    return True, "Senha forte!"

def main():
    print("Bem-vindo ao verificador de senha forte!")
    print("Digite 'sair' para encerrar o programa.")

    while True:
        senha = input("Digite uma senha: ").strip()

        if senha.lower() == 'sair':
            print("Programa encerrado.")
            break

        eh_forte, mensagem = verificar_senha_forte(senha)
        if eh_forte:
            print(mensagem)
            break
        else:
            print(mensagem)

if __name__ == "__main__":
    main()