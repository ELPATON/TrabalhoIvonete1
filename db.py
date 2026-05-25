import requests
from config import URL, HEADERS

def db_get(tabela):
    r = requests.get(f'{URL}/rest/v1/{tabela}?select=*', headers=HEADERS)
    return r.json()

def db_insert(tabela, dados):
    requests.post(f'{URL}/rest/v1/{tabela}', json=dados, headers=HEADERS)

def db_update(tabela, id, dados):
    requests.patch(f'{URL}/rest/v1/{tabela}?id=eq.{id}', json=dados, headers=HEADERS)

def db_delete(tabela, id):
    requests.delete(f'{URL}/rest/v1/{tabela}?id=eq.{id}', headers=HEADERS)

def db_get_filtrado(tabela, campo, valor):
    r = requests.get(f'{URL}/rest/v1/{tabela}?{campo}=eq.{valor}&select=*', headers=HEADERS)
    return r.json()
