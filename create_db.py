import sqlite3

# Função para criar o banco de dados e a tabela
def criar_banco_de_dados():
    conn = sqlite3.connect("dados_site.db")
    cursor = conn.cursor()

    # Criar a tabela "dados" se ela não existir
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS dados_site (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT,
            telefone TEXT,
            mensagem TEXT,
            contato TEXT,
            receber_informacoes INTEGER
        )
    """)

    # Commit e fechar a conexão com o banco de dados
    conn.commit()
    conn.close()

if __name__ == '__main__':
    criar_banco_de_dados()
    print("Banco de dados criado com sucesso.")