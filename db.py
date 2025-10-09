import sqlite3

def get_conexao():
    return sqlite3.connect("banco.db")

def inicializar_banco():
    """Executa o script SQL se o banco ainda não existir."""
    conexao = get_conexao()
    cursor = conexao.cursor()
    try:
        with open("banco.sql", "r", encoding="utf-8") as f:
            script_sql = f.read()
        cursor.executescript(script_sql)
        conexao.commit()
        print("Banco inicializado com sucesso.")
    except Exception as e:
        print(f"Erro ao inicializar banco: {e}")
    finally:
        conexao.close()

def inserir_beneficiario(pessoa):
    conexao = get_conexao()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO beneficiarios
    (nome, filiacao1, filiacao2, cpf, data_nascimento, documento_identidade, nacionalidade, email)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        pessoa.nome,
        pessoa.filiacao1,
        pessoa.filiacao2,
        pessoa.cpf,
        pessoa.data_nasc,
        pessoa.doc_identidade,
        pessoa.nacionalidade,
        pessoa.email
    ))

    id_beneficiario = cursor.lastrowid

    # Simples: telefone armazenado em um campo único
    cursor.execute("""
    INSERT INTO telefone (codigo_pais, ddd, numero, descricao, fk_beneficiarios_id_beneficiario)
    VALUES (?, ?, ?, ?, ?)
    """, (55, 11, pessoa.telefone, "Residencial", id_beneficiario))

    conexao.commit()
    conexao.close()
    return id_beneficiario

def listar_beneficiarios():
    conexao = get_conexao()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT id_beneficiario, nome, cpf, data_nascimento 
        FROM beneficiarios
    """)
    resultados = cursor.fetchall()
    conexao.close()
    return resultados
