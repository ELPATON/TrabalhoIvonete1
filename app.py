import os
import requests
from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

URL = os.getenv('SUPABASE_URL')
KEY = os.getenv('SUPABASE_KEY')

HEADERS = {
    'apikey': KEY,
    'Authorization': f'Bearer {KEY}',
    'Content-Type': 'application/json'
}

def db_get(tabela):
    r = requests.get(f'{URL}/rest/v1/{tabela}?select=*', headers=HEADERS)
    return r.json()

def db_insert(tabela, dados):
    requests.post(f'{URL}/rest/v1/{tabela}', json=dados, headers=HEADERS)

def db_update(tabela, id, dados):
    requests.patch(f'{URL}/rest/v1/{tabela}?id=eq.{id}', json=dados, headers=HEADERS)

def db_delete(tabela, id):
    requests.delete(f'{URL}/rest/v1/{tabela}?id=eq.{id}', headers=HEADERS)

# ========== ALUNOS ==========

@app.route('/')
def index():
    return redirect('/alunos')

@app.route('/alunos')
def alunos():
    dados = db_get('alunos')
    print('DADOS:', dados)
    return render_template('alunos.html', alunos=dados)

@app.route('/alunos/novo', methods=['POST'])
def novo_aluno():
    db_insert('alunos', {
        'nome': request.form['nome'],
        'matricula': request.form['matricula'],
        'turma': request.form['turma'],
        'status': request.form['status']
    })
    return redirect('/alunos')

@app.route('/alunos/editar/<int:id>', methods=['POST'])
def editar_aluno(id):
    db_update('alunos', id, {
        'nome': request.form['nome'],
        'matricula': request.form['matricula'],
        'turma': request.form['turma'],
        'status': request.form['status']
    })
    return redirect('/alunos')

@app.route('/alunos/excluir/<int:id>')
def excluir_aluno(id):
    db_delete('alunos', id)
    return redirect('/alunos')

# ========== PROFESSORES ==========

@app.route('/professores')
def professores():
    dados = db_get('professores')
    return render_template('professores.html', professores=dados)

@app.route('/professores/novo', methods=['POST'])
def novo_professor():
    db_insert('professores', {
        'nome': request.form['nome'],
        'email': request.form['email'],
        'disciplina': request.form['disciplina']
    })
    return redirect('/professores')

@app.route('/professores/excluir/<int:id>')
def excluir_professor(id):
    db_delete('professores', id)
    return redirect('/professores')

# ========== TURMAS ==========

@app.route('/turmas')
def turmas():
    dados = db_get('turmas')
    return render_template('turmas.html', turmas=dados)

@app.route('/turmas/novo', methods=['POST'])
def nova_turma():
    db_insert('turmas', {
        'nome': request.form['nome'],
        'serie': request.form['serie'],
        'turno': request.form['turno']
    })
    return redirect('/turmas')

@app.route('/turmas/excluir/<int:id>')
def excluir_turma(id):
    db_delete('turmas', id)
    return redirect('/turmas')

# ========== NOTAS ==========

@app.route('/notas')
def notas():
    dados = db_get('notas')
    alunos = db_get('alunos')
    return render_template('notas.html', notas=dados, alunos=alunos)

@app.route('/notas/novo', methods=['POST'])
def nova_nota():
    db_insert('notas', {
        'aluno_id': int(request.form['aluno_id']),
        'disciplina': request.form['disciplina'],
        'bimestre': request.form['bimestre'],
        'valor': float(request.form['valor'])
    })
    return redirect('/notas')

@app.route('/notas/excluir/<int:id>')
def excluir_nota(id):
    db_delete('notas', id)
    return redirect('/notas')

if __name__ == '__main__':
    app.run(debug=True)