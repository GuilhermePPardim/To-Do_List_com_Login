Este projeto é uma aplicação de lista de tarefas (To-Do List) em Python, com sistema de cadastro e login de usuários.
Cada usuário tem sua própria lista de tarefas, que é salva em um arquivo JSON.

🚀 Funcionalidades

✅ Cadastro de usuários com senha criptografada (SHA-256)

✅ Login seguro (validação de senha)

✅ Adicionar novas tarefas

✅ Listar tarefas pendentes e concluídas

✅ Marcar tarefas como concluídas

✅ Remover tarefas

✅ Persistência de dados em arquivo JSON (dados_user.json)

📂 Estrutura do Projeto
To-Do_List_com_Login/
│── to_do.py           # Código principal
│── dados_user.json    # Base de dados em JSON (gerada automaticamente)
│── README.md          # Documentação do projeto

🛠️ Tecnologias Utilizadas

Python 3.11+

Módulos padrão:

json

hashlib

getpass

os

▶️ Como Executar

Clone este repositório:

git clone https://github.com/seu-usuario/to-do-list-login.git
cd to-do-list-login


Execute o programa:

python to_do.py


No terminal, você verá o menu inicial:

---BEM-VINDO À APLICAÇÃO---
1. LOGIN
2. Registrar
3. Sair

🧑‍💻 Exemplo de Uso

Registro de novo usuário:

___Cadastro de Novo Usuário___
Digite o nome de usuário desejado: igor
Digite a senha:
Confirme a senha:
Usuário 'igor' cadastrado com sucesso!


Adicionar tarefa:

***Menu de tarefas de igor***
1. Adicionar Tarefa
2. Listar Tarefa
3. Marcar Tarefa como Concluída
4. Remover Tarefa
5. Sair

Escolha uma opção: 1
Digite a descrição da nova tarefa: Estudar Flask
Tarefa adicionada com sucesso!

📌 Próximos Passos (Versão 1.2)

Migrar o sistema para aplicação web (Flask)

Criar interface com HTML, CSS e JavaScript

Melhorar a persistência de dados (SQLite ou PostgreSQL)

✍️ Autor: Guilherme Pereira pardim
📅 Versão: 1.1 (Terminal)
