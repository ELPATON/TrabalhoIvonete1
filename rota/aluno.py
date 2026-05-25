import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Blueprint, render_template, request, redirect
from db import db_get, db_insert, db_update, db_delete
from decorators import login_requerido, perfil_requerido

alunos_bp = Blueprint('alunos', __name__)

@alunos_bp.route('/alunos')
@login_requerido
def alunos():
    dados = db_get('alunos')
    return render_template('alunos.html', alunos=dados)

@alunos_bp.route('/alunos/novo', methods=['POST'])
@login_requerido
@perfil_requerido('admin')
def novo_aluno():
    db_insert('alunos', {
        'nome': request.form['nome'],
        'matricula': request.form['matricula'],
        'turma': request.form['turma'],
        'status': request.form['status']
    })
    return redirect('/alunos')

@alunos_bp.route('/alunos/editar/<int:id>', methods=['POST'])
@login_requerido
@perfil_requerido('admin')
def editar_aluno(id):
    db_update('alunos', id, {
        'nome': request.form['nome'],
        'matricula': request.form['matricula'],
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