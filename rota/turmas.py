from flask import Blueprint, render_template, request, redirect, session
from db import db_get, db_insert, db_delete, db_get_filtrado
from decorators import login_requerido, perfil_requerido

turmas_bp = Blueprint('turmas', __name__)

@turmas_bp.route('/turmas')
@login_requerido
def turmas():
    if session.get('perfil') == 'aluno':
        aluno = db_get_filtrado('alunos', 'email', session['usuario'])
        if aluno and isinstance(aluno, list) and len(aluno) > 0:
            dados = db_get_filtrado('turmas', 'nome', aluno[0]['turma'])
        else:
            dados = []
    else:
        dados = db_get('turmas')
    return render_template('turmas.html', turmas=dados)

@turmas_bp.route('/turmas/novo', methods=['POST'])
@login_requerido
@perfil_requerido('admin')
def nova_turma():
    db_insert('turmas', {
        'nome': request.form['nome'],
        'serie': request.form['serie'],
        'turno': request.form['turno']
    })
    return redirect('/turmas')

@turmas_bp.route('/turmas/excluir/<int:id>')
@login_requerido
@perfil_requerido('admin')
def excluir_turma(id):
    db_delete('turmas', id)
    return redirect('/turmas')