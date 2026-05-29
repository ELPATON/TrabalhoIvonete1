import sys
import os
import requests
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Blueprint, render_template, request, redirect, session
from config import URL, KEY
from db import db_get, db_insert, db_delete
from decorators import login_requerido, perfil_requerido

professores_bp = Blueprint('professores', __name__)

@professores_bp.route('/professores')
@login_requerido
@perfil_requerido('admin')
def professores():
    erro = request.args.get('erro')
    dados = db_get('professores')
    return render_template('professores.html', professores=dados, erro=erro)

@professores_bp.route('/professores/novo', methods=['POST'])
@login_requerido
@perfil_requerido('admin')
def novo_professor():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    disciplina = request.form['disciplina']

    r = requests.post(
        f'{URL}/auth/v1/signup',
        json={'email': email, 'password': senha},
        headers={'apikey': KEY, 'Content-Type': 'application/json'}
    )
    dados = r.json()
    print('CRIAR CONTA PROFESSOR:', dados)
    auth_id = dados.get('id') or (dados.get('user') or {}).get('id')

    if not auth_id:
        return redirect('/professores?erro=Erro%20ao%20criar%20conta%20no%20Supabase')

    db_insert('professores', {
        'nome': nome,
        'email': email,
        'disciplina': disciplina
    })
    db_insert('usuarios', {
        'email': email,
        'perfil': 'professor',
        'auth_id': auth_id
    })
    return redirect('/professores')

@professores_bp.route('/professores/excluir/<int:id>')
@login_requerido
@perfil_requerido('admin')
def excluir_professor(id):
    db_delete('professores', id)
    return redirect('/professores')