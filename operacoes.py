import os
import csv
from colorama import init, Fore, Back 
import pandas as pd
init(autoreset=True)

#Limpar a tela
def limpar_tela_ope():
    os.system('cls' if os.name == "nt" else 'clear')

#Define a variável do tipo de usuário conforme a opção do operador do sistema
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

#Visualizar todos os usuários
def visualizar_usuarios():
    df = pd.read_csv('lista_usuarios.csv')
    print(f"{Fore.BLUE}Usuários do sistema: {Fore.RESET}")
    print(df)

#Cadastra um usuário novo    
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


def apagar_usuario():
    df = pd.read_csv('lista_usuarios.csv')
    print(f"{Fore.GREEN}Usuários do sistema: {Fore.RESET}")
    print(df)
    excluir_item = int(input(f"{Fore.GREEN}Digite o número do usuário que deseja apagar: {Fore.RESET}"))
    nome_usuario = df.loc[excluir_item, 'Usuario']
    novo_df = df.copy()
    novo_df.drop([excluir_item], axis = 0, inplace = True)
    limpar_tela_ope()
    print(f"{Fore.GREEN}Usuário {nome_usuario} foi apagado! {Fore.RESET}")
    novo_df.to_csv('lista_usuarios.csv', index=False)

#Atualiza um usuário
def adicionar_usuarios_atualizar(nome_usuario, senha_usuario, tipo_usuario):
    with open("lista_usuarios.csv", "a", newline='') as arquivo_csv:
        add = csv.writer(arquivo_csv)
        add.writerow([nome_usuario, senha_usuario, tipo_usuario])

def editar_usuario():
    df = pd.read_csv('lista_usuarios.csv')
    print(f"{Fore.GREEN}Usuários do sistema: {Fore.RESET}")
    print(df)
    editar_usuario = int(input(f"{Fore.GREEN}Digite o número do usuário que deseja editar: {Fore.RESET}"))
    item_df = df.loc[editar_usuario]
    limpar_tela_ope()
    print(f"{Fore.GREEN}Você selecionou: {Fore.RESET}")
    print(item_df)
    nome_usuario = df.loc[editar_usuario, 'Usuario']
    senha_usuario = input(f"{Fore.MAGENTA}Qual a nova senha para {nome_usuario}? {Fore.RESET}")
    print(f"{Fore.MAGENTA}O usuário {nome_usuario} é 'admin' ou 'colaborador'? {Fore.RESET}")
    print("1 - Admin")
    print("2 - Colaborador")
    tipo_usuario = processa_tipo_usuario()
    novo_df = df.copy()
    novo_df.drop([editar_usuario], axis = 0, inplace = True)
    novo_df.to_csv('lista_usuarios.csv', index=False)
    adicionar_usuarios_atualizar(nome_usuario, senha_usuario, tipo_usuario)
    print(f"{Fore.GREEN}Usuário {nome_usuario} atualizado! {Fore.RESET}")

#Valida autenticação
'''def valida_autenticacao(login, senha):
    df_usuarios = pd.read_csv('lista_usuarios.csv')
    usuarios = set(df_usuarios['Usuario'])
    if login in usuarios:
        cadastro = df_usuarios.loc[df_usuarios['Usuario'] == login]
        senha_usuario = set(cadastro['Senha'])
        if senha == senha_usuario:
            return(True)
    else:
        return(False)'''
