import os
import csv
from colorama import init, Fore, Back 
import pandas as pd
init(autoreset=True)

#Limpar a tela
def limpar_tela_ope():
    os.system('cls' if os.name == "nt" else 'clear')

#Visualizar todos os eventos
def visualizar_usuarios():
    df = pd.read_csv('lista_usuarios.csv')
    print(f"{Fore.BLUE}Usuários do sistema: {Fore.RESET}")
    print(df)

#Cadastra um usuario novo
def processa_tipo_usuario():
    opcao_tipo_usuario = input(f"{Fore.GREEN}Digite a opção desejada: {Fore.RESET}")
    if opcao_tipo_usuario == "1":
        tipo_usuario = "Admin"
    elif opcao_tipo_usuario == "2":
        tipo_usuario = "Colaborador"
    else:
        print(f"{Fore.RED}Opção inválida! Tente novamente {Fore.RESET}")
        processa_tipo_usuario()
    return(tipo_usuario)
    
def criar_usuario():
    with open("lista_usuarios.csv", "a", newline='') as arquivo_csv:
        print(f"{Fore.GREEN}Criando usuário novo... Não use acentos! {Fore.RESET}")
        nome_usuario = input(f"{Fore.MAGENTA}Qual o nome do usuário? {Fore.RESET}")
        senha_usuario = input(f"{Fore.MAGENTA}Digite uma senha para {nome_usuario}: {Fore.RESET}")
        print(f"{Fore.MAGENTA}O usuário {nome_usuario} é 'admin' ou 'colaborador'? {Fore.RESET}")
        print("1 - Admin")
        print("2 - Colaborador")
        tipo_usuario = processa_tipo_usuario()
        add = csv.writer(arquivo_csv)
        add.writerow([nome_usuario, senha_usuario, tipo_usuario])
        print(f"{Fore.GREEN}Usuário {nome_usuario} foi adicionado! {Fore.RESET}")