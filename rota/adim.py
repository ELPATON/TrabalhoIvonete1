import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Blueprint, render_template, request, redirect
from db import db_get, db_update, db_delete
from decorators import login_requerido, perfil_requerido

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin')
@login_requerido
@perfil_requerido('admin')
def admin():
    usuarios = db_get('usuarios')
    return render_template('adim.html', usuarios=usuarios)

@admin_bp.route('/admin/excluir/<int:id>')
@login_requerido
@perfil_requerido('admin')
def excluir_usuario(id):
    db_delete('usuarios', id)
    return redirect('/admin')

@admin_bp.route('/admin/perfil/<int:id>', methods=['POST'])
@login_requerido
@perfil_requerido('admin')
def alterar_perfil(id):
    db_update('usuarios', id, {'perfil': request.form['perfil']})
    return redirect('/admin')