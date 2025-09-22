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

def salvar_dados (dados):
    
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
         "Tarefas": []
}
    salvar_dados(dados)
    print(f"Usuário '{username}' cadastro com sucesso!")    
     
def fazer_login(dados):
    
    print("___Login___")
    username = input("Usuário: ")
    senha = getpass.getpass("Senha: ")
    
    if username not in dados:
        print("ERRO: Usuário não encotrado")
        return None
    
    if dados[username]["senha"] == hash_senha(senha) :
        print(f"login bem-sucedido! Bem vindo(a), {username}")
        return username
    else
        print("ERRO: Senha incorreta.")
        return None

def menu_tarefas (username, dados):
    
    while True:
        print(f"***Menu de terefas de {username}***")
        print("1. Adicionar Tarefas")
        print("2. Listar Tarefa")
        print("3 Marcar Tarefa como Concluida")
        print("4. Remover Tarefa")
        print("5. SAIR")
        
        escolha = input ("Escolha uma opção")
        
        if escolha == '1' :
            adicionar_tarefa(username, dados)
        elif escolha == '2' :
            listar_tarefa(username, dados)
        elif escolha == '3' :
            marcar_tarefa_concluida(username, dados)
        elif escolha == '4'
            remover_tarefa(username, dados)      
        elif escolha == '5'
            print("SAINDO")
            break
        else:
            print("INVÁLIDO.")
                   
        
        salvar_dados(dados)
                   
def adicionar_tarefa(username, dados):
    
    descricao = input ("Digite a descrição da nova tarefa: ")
    if descricao:
        tarefa = {"descricao": descricao, "concluida": False}
        dados[username]["tarefas"].append(tarefa)
        print("Tarefa adicionada com sucesso! ")
    else:
        print("A descrição da tarefa não pode ser NULA. ")
       
def listar_tarefas(username, dados):
    
    print("***Sua Lista de Tarefas*** ")
    tarefas = dados[username]["tarefas"]
    if not tarefas:
        print("Sem tarefas.")
        return
    
    for i, tarefa in enumerate(tarefas):
        status = "✓" if tarefa["concluida"] else " "
        print(f"{i + 1}. [{status}] {tarefa[descricao]}")
        
def marcar_tarefa_concluida(username, dados):
    
    listar_tarefas(username, dados)
    tarefa = dados [username]["tarefas"]
    if not tarefas:
        return

    try:
        num_tarefa = int(input("Digite o número da tarefa para marcar como concluida: "))
        if 1 <= num_tarefa <= len(tarefas):
            tarefas[num_tarefa - 1]["concluida"] = True
            print("Tarefa marcado como conluída! ")
        else: print ("Número de tarefa inválido.")
    except ValueError:
        print("ENtrada inválida. Por favor , digite um número.")

def remover_tarefa(username, dados): 
    
    listar_tarefas(username, dados)
    tarefas = dados[username]["tarefas"]
    if not tarefas:
        return
    
    try:
        num_tarefa = int(input("Digite o número da tarefa para remover"))
        if 1 <= num_tarefa <= len(tarefas):
            tarefa_removida = tarefas.pop(num_tarefa - 1)
            print(f"Tarefa '{tarefa_removida['descricao']}'removida com sucesso")
        else: 
            print("Número de tarefa inválido. ")
    except ValueError:
        print("Entrada inválida. por favor, digite um número. ")
        
def main():
    dados = carregar_dados
    
    while True:
        print("---BEM-VINDO À APLICAÇÂO---")
        print("1. LOGIN")
        print("2, Registrar")
        print("3. Sair")
        
        escolha_inicial = input("Escolha uma opção: ")
        
        if escolha_inicial == '1':
            usuario_logado = fazer_login(dados)
            if usuario_logado:
                menu_tarefas(usuario_logado, dados)
        elif escolha_inicial == '2':
            registrar_usuario(dados)
        elif escolha_inicial == '3':
            print("Obrigado por usar a aplicação. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()