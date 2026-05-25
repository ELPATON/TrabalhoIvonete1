import sys
import os
import requests
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Blueprint, render_template, request, redirect, session
from config import URL, KEY, HEADERS
from db import db_insert, db_get_filtrado

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
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
        print('RESPOSTA LOGIN:', dados)
        if 'access_token' in dados:
            session['usuario'] = email
            session['token'] = dados['access_token']
            auth_id = dados['user']['id']
            usuarios = db_get_filtrado('usuarios', 'auth_id', auth_id)
            print('USUARIOS ENCONTRADOS:', usuarios)
            if usuarios:
                session['perfil'] = usuarios[0]['perfil']
                print('PERFIL SALVO:', session['perfil'])
            else:
                session['perfil'] = 'aluno'
                print('PERFIL PADRAO: aluno')
            return redirect('/alunos')
        else:
            erro = 'Email ou senha incorretos!'
    return render_template('login.html', erro=erro)

@auth_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    erro = None
    sucesso = None
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        perfil = request.form['perfil']
        r = requests.post(
            f'{URL}/auth/v1/signup',
            json={'email': email, 'password': senha},
            headers={'apikey': KEY, 'Content-Type': 'application/json'}
        )
        dados = r.json()
        print('RESPOSTA CADASTRO:', dados)
        if 'id' in dados:
            db_insert('usuarios', {
                'email': email,
                'perfil': perfil,
                'auth_id': dados['id']
            })
            sucesso = 'Cadastro realizado! Faça login.'
        else:
            erro = 'Erro ao cadastrar. Tente outro email.'
    return render_template('cadastro.html', erro=erro, sucesso=sucesso)

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

@auth_bp.route('/acesso_negado')
def acesso_negado():
    return render_template('acesso_negado.html')