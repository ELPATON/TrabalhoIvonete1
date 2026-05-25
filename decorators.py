from functools import wraps
from flask import session, redirect

def login_requerido(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'usuario' not in session:
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated

def perfil_requerido(*perfis_permitidos):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if session.get('perfil') not in perfis_permitidos:
                return redirect('/acesso_negado')
            return f(*args, **kwargs)
        return decorated
    return decorator
