from flask import Flask, render_template, request, redirect, session
from functools import wraps
from dotenv import load_dotenv
import requests
import os

load_dotenv()

app = Flask(__name__)
app.static_folder = 'static'
app.secret_key = 'eduflow2026'

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

def login_requerido(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'usuario' not in session:
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated

# ========== AUTH ==========

@app.route('/login', methods=['GET', 'POST'])
def login():
    erro = None
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        r = requests.post(
            f'{URL}/auth/v1/token?grant_type=password',
            json={'email': email, 'password': senha},
            headers={'apikey': KEY, 'Content-Type': 'application/json'}
        )
        dados = r.json()
        if 'access_token' in dados:
            session['usuario'] = email
            session['token'] = dados['access_token']
            return redirect('/alunos')
        else:
            erro = 'Email ou senha incorretos!'
    return render_template('login.html', erro=erro)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    erro = None
    sucesso = None
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        r = requests.post(
            f'{URL}/auth/v1/signup',
            json={'email': email, 'password': senha},
            headers={'apikey': KEY, 'Content-Type': 'application/json'}
        )
        dados = r.json()
        if 'id' in dados:
            sucesso = 'Cadastro realizado! Faça login.'
        else:
            erro = 'Erro ao cadastrar. Tente outro email.'
    return render_template('cadastro.html', erro=erro, sucesso=sucesso)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

# ========== ALUNOS ==========

@app.route('/')
def index():
    return redirect('/alunos')

@app.route('/alunos')
@login_requerido
def alunos():
    dados = db_get('alunos')
    return render_template('alunos.html', alunos=dados)

@app.route('/alunos/novo', methods=['POST'])
@login_requerido
def novo_aluno():
    db_insert('alunos', {
        'nome': request.form['nome'],
        'matricula': request.form['matricula'],
        'turma': request.form['turma'],
        'status': request.form['status']
    })
    return redirect('/alunos')

@app.route('/alunos/editar/<int:id>', methods=['POST'])
@login_requerido
def editar_aluno(id):
    db_update('alunos', id, {
        'nome': request.form['nome'],
        'matricula': request.form['matricula'],
        'turma': request.form['turma'],
        'status': request.form['status']
    })
    return redirect('/alunos')

@app.route('/alunos/excluir/<int:id>')
@login_requerido
def excluir_aluno(id):
    db_delete('alunos', id)
    return redirect('/alunos')

# ========== PROFESSORES ==========

@app.route('/professores')
@login_requerido
def professores():
    dados = db_get('professores')
    return render_template('professores.html', professores=dados)

@app.route('/professores/novo', methods=['POST'])
@login_requerido
def novo_professor():
    db_insert('professores', {
        'nome': request.form['nome'],
        'email': request.form['email'],
        'disciplina': request.form['disciplina']
    })
    return redirect('/professores')

@app.route('/professores/excluir/<int:id>')
@login_requerido
def excluir_professor(id):
    db_delete('professores', id)
    return redirect('/professores')

# ========== TURMAS ==========

@app.route('/turmas')
@login_requerido
def turmas():
    dados = db_get('turmas')
    return render_template('turmas.html', turmas=dados)

@app.route('/turmas/novo', methods=['POST'])
@login_requerido
def nova_turma():
    db_insert('turmas', {
        'nome': request.form['nome'],
        'serie': request.form['serie'],
        'turno': request.form['turno']
    })
    return redirect('/turmas')

@app.route('/turmas/excluir/<int:id>')
@login_requerido
def excluir_turma(id):
    db_delete('turmas', id)
    return redirect('/turmas')

# ========== NOTAS ==========

@app.route('/notas')
@login_requerido
def notas():
    dados = db_get('notas')
    alunos = db_get('alunos')
    return render_template('notas.html', notas=dados, alunos=alunos)

@app.route('/notas/novo', methods=['POST'])
@login_requerido
def nova_nota():
    db_insert('notas', {
        'aluno_id': int(request.form['aluno_id']),
        'disciplina': request.form['disciplina'],
        'bimestre': request.form['bimestre'],
        'valor': float(request.form['valor'])
    })
    return redirect('/notas')

@app.route('/notas/excluir/<int:id>')
@login_requerido
def excluir_nota(id):
    db_delete('notas', id)
    return redirect('/notas')

if __name__ == '__main__':
    app.run(debug=True)

   dados = r.json()
print('RESPOSTA CADASTRO:', dados)  # adiciona essa linha
if 'id' in dados: