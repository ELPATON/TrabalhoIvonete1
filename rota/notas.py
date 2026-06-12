from flask import Blueprint, render_template, request, redirect, session
from db import db_get, db_insert, db_delete, db_get_filtrado
from decorators import login_requerido, perfil_requerido

notas_bp = Blueprint('notas', __name__)

@notas_bp.route('/notas')
@login_requerido
def notas():
    if session.get('perfil') == 'aluno':
        aluno = db_get_filtrado('alunos', 'email', session['usuario'])
        if aluno and isinstance(aluno, list) and len(aluno) > 0:
            dados = db_get_filtrado('notas', 'aluno_id', aluno[0]['id'])
        else:
            dados = []
        alunos = []
    else:
        dados = db_get('notas')
        alunos = db_get('alunos')
    aluno_map = {a['id']: a['nome'] for a in alunos} if alunos else {}
    return render_template('notas.html', notas=dados, alunos=alunos, aluno_map=aluno_map)

@notas_bp.route('/notas/novo', methods=['POST'])
@login_requerido
@perfil_requerido('admin', 'professor')
def nova_nota():
    try:
        aluno_id = int(request.form['aluno_id'])
        valor = float(request.form['valor'])
    except (ValueError, KeyError):
        return redirect('/notas')
    db_insert('notas', {
        'aluno_id': aluno_id,
        'disciplina': request.form['disciplina'],
        'bimestre': request.form['bimestre'],
        'valor': valor
    })
    return redirect('/notas')

@notas_bp.route('/notas/excluir/<int:id>')
@login_requerido
@perfil_requerido('admin', 'professor')
def excluir_nota(id):
    db_delete('notas', id)
    return redirect('/notas')