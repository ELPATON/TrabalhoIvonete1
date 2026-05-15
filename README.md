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

### 5. Rode o projeto
```bash
python app.py
```

Acesse no navegador: **http://127.0.0.1:5000**

## Como funciona
O sistema usa a arquitetura **MVC simplificada**:
- `app.py` contém todas as rotas e a lógica de comunicação com o banco
- A comunicação com o Supabase é feita via **API REST** usando a biblioteca `requests`
- Os templates HTML usam **Jinja2** para renderizar os dados dinamicamente

## Integrantes do grupo
- Integrante 1
- Integrante 2
- Integrante 3
- Integrante 4
- Integrante 5
  
