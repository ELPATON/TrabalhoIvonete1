import requests

from flask import Blueprint, render_template, request, redirect, session
from config import URL, KEY
from db import db_get, db_insert, db_update, db_delete, db_get_filtrado
from decorators import login_requerido, perfil_requerido

alunos_bp = Blueprint('alunos', __name__)

@alunos_bp.route('/alunos')
@login_requerido
@perfil_requerido('admin', 'professor')
def alunos():
    erro = request.args.get('erro')
    dados = db_get('alunos')
    return render_template('alunos.html', alunos=dados, erro=erro)

@alunos_bp.route('/alunos/novo', methods=['POST'])
@login_requerido
@perfil_requerido('admin')
def novo_aluno():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    matricula = request.form['matricula']
    turma = request.form['turma']
    status = request.form['status']

    if db_get_filtrado('alunos', 'matricula', matricula):
        return redirect('/alunos?erro=Matr%C3%ADcula%20j%C3%A1%20existe')
    if db_get_filtrado('alunos', 'email', email):
        return redirect('/alunos?erro=Email%20j%C3%A1%20cadastrado')

    r = requests.post(
        f'{URL}/auth/v1/signup',
        json={'email': email, 'password': senha},
        headers={'apikey': KEY, 'Content-Type': 'application/json'}
    )
    dados = r.json()
    auth_id = dados.get('id') or (dados.get('user') or {}).get('id')

    if not auth_id:
        return redirect('/alunos?erro=Erro%20ao%20criar%20conta%20no%20Supabase')

    db_insert('alunos', {
        'nome': nome,
        'email': email,
        'matricula': matricula,
        'turma': turma,
        'status': status
    })
    db_insert('usuarios', {
        'email': email,
        'perfil': 'aluno',
        'auth_id': auth_id
    })
    return redirect('/alunos')

@alunos_bp.route('/alunos/editar/<int:id>', methods=['POST'])
@login_requerido
@perfil_requerido('admin')
def editar_aluno(id):
    matricula = request.form['matricula']
    email = request.form['email']
    if db_get_filtrado('alunos', 'matricula', matricula) and db_get_filtrado('alunos', 'matricula', matricula)[0]['id'] != id:
        return redirect('/alunos?erro=Matr%C3%ADcula%20j%C3%A1%20existe')
    if db_get_filtrado('alunos', 'email', email) and db_get_filtrado('alunos', 'email', email)[0]['id'] != id:
        return redirect('/alunos?erro=Email%20j%C3%A1%20cadastrado')
    db_update('alunos', id, {
        'nome': request.form['nome'],
        'email': email,
        'matricula': matricula,
        'turma': request.form['turma'],
        'status': request.form['status']
    })
    return redirect('/alunos')

@alunos_bp.route('/alunos/excluir/<int:id>')
@login_requerido
@perfil_requerido('admin')
def excluir_aluno(id):
    db_delete('alunos', id)
    return redirect('/alunos')