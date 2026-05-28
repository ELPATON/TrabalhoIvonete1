import sys
import os
import requests
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Blueprint, render_template, request, redirect, session
from config import URL, KEY, HEADERS
from db import db_get, db_update, db_delete, db_insert, db_get_filtrado

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin')
def admin():
    if session.get('perfil') != 'admin':
        return redirect('/acesso_negado')
    usuarios = db_get('usuarios')
    alunos = db_get('alunos')
    return render_template('adim.html', usuarios=usuarios, alunos=alunos)

@admin_bp.route('/admin/criar', methods=['POST'])
def criar_usuario():
    if session.get('perfil') != 'admin':
        return redirect('/acesso_negado')
    email = request.form['email']
    senha = request.form['senha']
    perfil = request.form['perfil']
    aluno_id = request.form.get('aluno_id')

    r = requests.post(
        f'{URL}/auth/v1/signup',
        json={'email': email, 'password': senha},
        headers={'apikey': KEY, 'Content-Type': 'application/json'}
    )
    dados = r.json()
    print('CRIAR USUARIO:', dados)
    auth_id = dados.get('id') or (dados.get('user') or {}).get('id')

    if auth_id:
        db_insert('usuarios', {
            'email': email,
            'perfil': perfil,
            'auth_id': auth_id
        })
        if perfil == 'aluno' and aluno_id:
            db_update('alunos', int(aluno_id), {'auth_id': auth_id})

    return redirect('/admin')

@admin_bp.route('/admin/excluir/<int:id>')
def excluir_usuario(id):
    if session.get('perfil') != 'admin':
        return redirect('/acesso_negado')
    db_delete('usuarios', id)
    return redirect('/admin')

@admin_bp.route('/admin/perfil/<int:id>', methods=['POST'])
def alterar_perfil(id):
    if session.get('perfil') != 'admin':
        return redirect('/acesso_negado')
    db_update('usuarios', id, {'perfil': request.form['perfil']})
    return redirect('/admin')
