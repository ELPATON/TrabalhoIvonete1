import requests
from config import URL, HEADERS

def db_get(tabela):
    try:
        r = requests.get(f'{URL}/rest/v1/{tabela}?select=*', headers=HEADERS, timeout=10)
        return r.json() if r.ok else []
    except Exception:
        return []

def db_insert(tabela, dados):
    try:
        requests.post(f'{URL}/rest/v1/{tabela}', json=dados, headers=HEADERS, timeout=10)
    except Exception:
        pass

def db_update(tabela, id, dados):
    try:
        requests.patch(f'{URL}/rest/v1/{tabela}?id=eq.{id}', json=dados, headers=HEADERS, timeout=10)
    except Exception:
        pass

def db_delete(tabela, id):
    try:
        requests.delete(f'{URL}/rest/v1/{tabela}?id=eq.{id}', headers=HEADERS, timeout=10)
    except Exception:
        pass

def db_get_filtrado(tabela, campo, valor):
    try:
        r = requests.get(f'{URL}/rest/v1/{tabela}?{campo}=eq.{valor}&select=*', headers=HEADERS, timeout=10)
        return r.json() if r.ok else []
    except Exception:
        return []