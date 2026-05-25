import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Blueprint, render_template, request, redirect
from db import db_get, db_insert, db_delete
from decorators import login_requerido, perfil_requerido

notas_bp = Blueprint('notas', __name__)

@notas_bp.route('/notas')
@login_requerido
def notas():
    dados = db_get('notas')
    alunos = db_get('alunos')
    return render_template('notas.html', notas=dados, alunos=alunos)

@notas_bp.route('/notas/novo', methods=['POST'])
@login_requerido
@perfil_requerido('admin', 'professor')
def nova_nota():
    db_insert('notas', {
        'aluno_id': int(request.form['aluno_id']),
        'disciplina': request.form['disciplina'],
        'bimestre': request.form['bimestre'],
        'valor': float(request.form['valor'])
    })
    return redirect('/notas')

@notas_bp.route('/notas/excluir/<int:id>')
@login_requerido
@perfil_requerido('admin', 'professor')
def excluir_nota(id):
    db_delete('notas', id)
    return redirect('/notas')