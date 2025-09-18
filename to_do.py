import json
import hashlib
import getpass
import os 

arquivos_dados = "dados_user.json"

def carregar_dados():
    if not os.path.exists