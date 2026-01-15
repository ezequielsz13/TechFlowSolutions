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

