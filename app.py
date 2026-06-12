import os
from flask import Flask, redirect, session
from config import SECRET_KEY

template_dir = os.path.abspath('templates')
static_dir = os.path.abspath('static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.secret_key = SECRET_KEY

from rota.auth import auth_bp
from rota.adim import admin_bp
from rota.aluno import alunos_bp
from rota.professor import professores_bp
from rota.turmas import turmas_bp
from rota.notas import notas_bp

app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(alunos_bp)
app.register_blueprint(professores_bp)
app.register_blueprint(turmas_bp)
app.register_blueprint(notas_bp)

@app.route('/')
def index():
    if 'usuario' not in session:
        return redirect('/login')
    perfil = session.get('perfil', 'aluno')
    if perfil == 'admin':
        return redirect('/admin')
    elif perfil == 'professor':
        return redirect('/alunos')
    else:
        return redirect('/turmas')

if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', 'false').lower() == 'true')
