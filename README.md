# EduFlow — Sistema de Gestão Escolar

Projeto Integrador — Linguagem de Programação

## Descrição
Sistema web de gerenciamento escolar com cadastro completo de alunos, professores, turmas e notas. Desenvolvido com Python + Flask no backend e Supabase como banco de dados em nuvem.

## Tecnologias utilizadas
- Python 3.14
- Flask 3.1
- Supabase (PostgreSQL)
- HTML + CSS
- Jinja2 (templates)
- Requests (chamadas HTTP para a API do Supabase)

## Funcionalidades
- Cadastro, listagem e exclusão de alunos
- Cadastro, listagem e exclusão de professores
- Cadastro, listagem e exclusão de turmas
- Cadastro, listagem e exclusão de notas por bimestre

## Estrutura do projeto
TrabalhoIvonete1/
├── app.py
├── .env
├── .gitignore
├── static/
│   └── estilo.css
└── templates/
├── base.html
├── login.html
├── cadastro.html
├── alunos.html
├── professores.html
├── turmas.html
└── notas.html

## Como rodar o projeto

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/TrabalhoIvonete1.git
cd TrabalhoIvonete1
```
### 2. Instale as dependências
```bash
pip install flask python-dotenv requests
```

### 3. Configure as variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto:
SUPABASE_URL=https://dfeputmnswipzmgzqlrx.supabase.co
SUPABASE_KEY=
### 4. Configure o banco de dados
No Supabase, crie as seguintes tabelas:

**alunos:** id, nome, matricula, turma, status

**professores:** id, nome, email, disciplina

**turmas:** id, nome, serie, turno

**notas:** id, aluno_id, disciplina, bimestre, valor

Desative o RLS executando no SQL Editor do Supabase:
```sql
ALTER TABLE alunos DISABLE ROW LEVEL SECURITY;
ALTER TABLE professores DISABLE ROW LEVEL SECURITY;
ALTER TABLE turmas DISABLE ROW LEVEL SECURITY;
ALTER TABLE notas DISABLE ROW LEVEL SECURITY;
```

Desative a confirmação de email em:
**Authentication → Providers → Email → desmarque "Confirm email"**

### 5. Rode o projeto
```bash
python app.py
```

Acesse no navegador: **http://127.0.0.1:5000**

## Como funciona
O sistema usa a arquitetura **MVC simplificada**:
- `app.py` contém todas as rotas, lógica de autenticação e comunicação com o banco
- A autenticação é feita via **Supabase Auth** usando a API REST
- A comunicação com o banco é feita via **API REST** usando a biblioteca `requests`
- As sessões de usuário são gerenciadas pelo Flask com `secret_key`
- Os templates HTML usam **Jinja2** para renderizar os dados dinamicamente

  ## Fluxo de autenticação
1. Usuário acessa o sistema e é redirecionado para `/login`
2. Faz cadastro em `/cadastro` com email e senha
3. Supabase valida e retorna um token de acesso
4. Flask salva o token na sessão do navegador
5. Usuário é redirecionado para o sistema
6. Ao sair, a sessão é encerrada via `/logout`

## Integrantes do grupo
- Matheus Alcantara Silva 
- Guilherme Souza da Silva Fernandes dos Santos
- Daniel Cerqueira Nonato
- Vinicius Almeida Santos Ferreira
- Cassio Gabriel da Silva Oliveira
  
