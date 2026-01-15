import os
from operacoes import visualizar_usuarios, criar_usuario, apagar_usuario, editar_usuario
from colorama import init, Fore, Back 
init(autoreset=True)

def limpar_tela():
    os.system('cls' if os.name == "nt" else 'clear')

def pausar():
    input(f"{Fore.YELLOW}Pressione ENTER para continuar...{Fore.RESET}")

#Menu principal
def menu_principal():
    print(f"{Fore.BLUE}Olá novamente! {Fore.RESET}")
    print(f"{Fore.BLUE}O que você deseja fazer? (Digite o número da opção e tecle ENTER) {Fore.RESET}")
    print(f"1 - Visualizar a lista de usuários")
    print(f"2 - Editar um usuário")
    print(f"3 - Criar um usuário novo")
    print(f"4 - Apagar um usuário")
    print(f"0 - Sair do sistema")

def processar_opcao(opcao):
    if opcao == "1":
        visualizar_usuarios()
    if opcao == "2":
        editar_usuario()
    if opcao == "3":
        criar_usuario()
    if opcao == "4":
        apagar_usuario()
    if opcao == "0":
        exit()

def sistema_usuarios():
    limpar_tela()
    menu_principal()
    opcao = input(f"{Fore.BLUE}Digite o número da opção desejada e tecle ENTER: {Fore.RESET}")
    limpar_tela()
    processar_opcao(opcao)
    pausar()
    sistema_usuarios()


sistema_usuarios()