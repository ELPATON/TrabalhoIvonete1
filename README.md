# EduFlow — Documentação Técnica

## Estrutura do Projeto
TrabalhoIvonete1/
├── app.py
├── config.py
├── db.py
├── decorators.py
├── .env
├── .gitignore
├── rota/
│   ├── init.py
│   ├── auth.py
│   ├── adim.py
│   ├── aluno.py
│   ├── professor.py
│   ├── turmas.py
│   └── notas.py
├── static/
│   └── estilo.css
└── templates/
├── base.html
├── login.html
├── cadastro.html
├── acesso_negado.html
├── adim.html
├── alunos.html
├── professores.html
├── turmas.html
└── notas.html

---

## Arquivos Python

### `app.py`
É o ponto de entrada do sistema. Inicializa o Flask, define a chave secreta da sessão e registra todos os Blueprints (módulos de rotas). É o primeiro arquivo que o Python executa quando você roda `python app.py`.

### `config.py`
Responsável pelas configurações globais do sistema. Lê as variáveis do arquivo `.env` (URL e chave do Supabase) e monta o cabeçalho HTTP usado em todas as requisições à API do Supabase.

### `db.py`
Contém todas as funções de comunicação com o banco de dados Supabase via API REST. É a camada de acesso a dados do sistema. Funções disponíveis:
- `db_get(tabela)` → busca todos os registros
- `db_insert(tabela, dados)` → insere um novo registro
- `db_update(tabela, id, dados)` → atualiza um registro
- `db_delete(tabela, id)` → remove um registro
- `db_get_filtrado(tabela, campo, valor)` → busca com filtro

### `decorators.py`
Contém os decorators de proteção de rotas. Decorators são funções que "envolvem" outras funções adicionando comportamento extra. Dois decorators disponíveis:
- `@login_requerido` → bloqueia acesso de usuários não logados
- `@perfil_requerido('admin', 'professor')` → bloqueia acesso por perfil

---

## Pasta `rota/`

### `rota/__init__.py`
Arquivo vazio obrigatório. Indica ao Python que a pasta `rota` é um módulo e pode ser importada.

### `rota/auth.py`
Gerencia toda a autenticação do sistema. Contém as rotas:
- `GET/POST /login` → tela e lógica de login
- `GET/POST /cadastro` → tela e lógica de cadastro
- `GET /logout` → encerra a sessão
- `GET /acesso_negado` → tela de acesso negado

### `rota/adim.py`
Painel exclusivo do administrador. Contém as rotas:
- `GET /admin` → lista todos os usuários
- `GET /admin/excluir/<id>` → exclui um usuário
- `POST /admin/perfil/<id>` → altera o perfil de um usuário

### `rota/aluno.py`
CRUD completo de alunos. Contém as rotas:
- `GET /alunos` → lista todos os alunos (todos os perfis)
- `POST /alunos/novo` → cadastra aluno (só admin)
- `POST /alunos/editar/<id>` → edita aluno (só admin)
- `GET /alunos/excluir/<id>` → exclui aluno (só admin)

### `rota/professor.py`
CRUD de professores. Contém as rotas:
- `GET /professores` → lista todos os professores (todos os perfis)
- `POST /professores/novo` → cadastra professor (só admin)
- `GET /professores/excluir/<id>` → exclui professor (só admin)

### `rota/turmas.py`
CRUD de turmas. Contém as rotas:
- `GET /turmas` → lista todas as turmas (todos os perfis)
- `POST /turmas/novo` → cadastra turma (só admin)
- `GET /turmas/excluir/<id>` → exclui turma (só admin)

### `rota/notas.py`
CRUD de notas. Contém as rotas:
- `GET /notas` → lista todas as notas (todos os perfis)
- `POST /notas/novo` → lança nota (admin e professor)
- `GET /notas/excluir/<id>` → exclui nota (admin e professor)

---

## Arquivos de Configuração

### `.env`
Armazena as credenciais sensíveis do projeto. **Nunca sobe para o GitHub.** Contém:
- `SUPABASE_URL` → endereço do banco de dados
- `SUPABASE_KEY` → chave de acesso à API

### `.gitignore`
Lista de arquivos que o Git ignora e não envia ao GitHub. Inclui o `.env`, arquivos de cache do Python (`__pycache__`) e arquivos compilados (`.pyc`).

---

## Pasta `templates/`

Arquivos HTML renderizados pelo Flask usando o motor de templates **Jinja2**.

| Arquivo | Descrição |
|---------|-----------|
| `base.html` | Layout base com menu de navegação. Todos os outros herdam dele via `{% extends %}` |
| `login.html` | Tela de login |
| `cadastro.html` | Tela de cadastro com seleção de perfil |
| `acesso_negado.html` | Tela exibida quando o perfil não tem permissão |
| `adim.html` | Painel admin com lista de usuários e controle de perfis |
| `alunos.html` | Listagem e formulário de alunos |
| `professores.html` | Listagem e formulário de professores |
| `turmas.html` | Listagem e formulário de turmas |
| `notas.html` | Listagem e formulário de notas |

---

## Pasta `static/`

### `estilo.css`
Arquivo de estilos CSS responsável pelo visual do sistema. Define cores, fontes, layout do menu, tabelas e formulários.

---

## Tecnologias Utilizadas

| Tecnologia | Função |
|-----------|--------|
| Python 3.14 | Linguagem principal |
| Flask | Framework web |
| Supabase | Banco de dados (PostgreSQL) + Autenticação |
| Jinja2 | Motor de templates HTML |
| Requests | Chamadas HTTP para API REST |
| python-dotenv | Leitura do arquivo `.env` |
| HTML + CSS | Interface do usuário |
