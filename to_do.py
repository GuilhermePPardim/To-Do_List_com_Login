import json
import hashlib
import getpass
import os 

arquivos_dados = "dados_user.json"

def carregar_dados():
    if not os.path.exists(arquivos_dados):
        return {}
    try:
        with open(arquivos_dados, 'r') as f:
            return json.load(f)
    
    except (json.jsondecodeerror, FileNotFoundError):
        return{}

def save_data (dados):
    
    with open (arquivos_dados, 'w') as f:
        json.dump(dados, f indent = 4)
        
def hash_senha (senha) :
    return hashlib.sha256(senha.encode()) . hexdigest()

def registrar_usuario (dados)

     print("___Cadastros de Novo Usuário___")
     username = input("Digite o nome de usuário desejado: ")
     if username in dados:
         print("ERRO:Nome de Usuário ja existe")
         return
     if not username:
         print("ERRO: usuário não pode ser nulo")
         return    