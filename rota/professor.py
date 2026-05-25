import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Blueprint, render_template, request, redirect
from db import db_get, db_insert, db_delete
from decorators import login_requerido, perfil_requerido

professores_bp = Blueprint('professores', __name__)

@professores_bp.route('/professores')
@login_requerido
def professores():
    dados = db_get('professores')
    return render_template('professores.html', professores=dados)

@professores_bp.route('/professores/novo', methods=['POST'])
@login_requerido
@perfil_requerido('admin')
def novo_professor():
    db_insert('professores', {
        'nome': request.form['nome'],
        'email': request.form['email'],
        'disciplina': request.form['disciplina']
    })
    return redirect('/professores')

@professores_bp.route('/professores/excluir/<int:id>')
@login_requerido
@perfil_requerido('admin')
def excluir_professor(id):
    db_delete('professores', id)
    return redirect('/professores')