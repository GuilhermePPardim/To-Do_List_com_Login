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
         print("ERRO: Nome de Usuário ja existe")
         return
     if not username:
         print("ERRO: Usuário não pode ser nulo")
         return
     
     senha = getpass.getpass("Digite a senha:")
     senha_confim= getpass.getpass ("Confirme a senha: ") 
     
     if not senha:
         print("ERRO: Senha nula")
         return
     if senha != senha_confim:
         print("ERRO: As senhas não coincidem")
         return
     
     dados[username] = {
         "senha": hash_senha(senha),
         "Tarefas": []}
         