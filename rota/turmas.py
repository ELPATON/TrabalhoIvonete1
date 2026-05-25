import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Blueprint, render_template, request, redirect
from db import db_get, db_insert, db_delete
from decorators import login_requerido, perfil_requerido

turmas_bp = Blueprint('turmas', __name__)

@turmas_bp.route('/turmas')
@login_requerido
def turmas():
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