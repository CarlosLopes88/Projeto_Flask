from fastapi import FastAPI
import sqlite3

app = FastAPI()

# Função para inserir dados no banco
def inserir_dados(nome, email, telefone, mensagem, contato, receber_informacoes):
    conn = sqlite3.connect("dados_site.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO dados_site (nome, email, telefone, mensagem, contato, receber_informacoes)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (nome, email, telefone, mensagem, contato, receber_informacoes))

    # Commit e fechar a conexão com o banco de dados
    conn.commit()
    conn.close()

@app.post('/salvar_dados')
async def salvar_dados(data: dict):
    # Imprima os dados recebidos no console
    print("Dados recebidos:")
    print(data)

    # Extrair os dados recebidos
    nome = data.get('nome_e_sobrenome')
    email = data.get('email')
    telefone = data.get('telefone')
    mensagem = data.get('mensagem')
    contato = data.get('contato')
    receber_informacoes = data.get('receber_informacoes', False)

    # Mensagem de depuração para verificar os dados extraídos
    print("Dados extraídos:")
    print(nome, email, telefone, mensagem, contato, receber_informacoes)

    # Chamar a função para inserir dados no banco
    inserir_dados(nome, email, telefone, mensagem, contato, receber_informacoes)

    # Mensagem de depuração após a inserção
    print("Dados inseridos no banco")

    # Retorne uma resposta de sucesso (você pode personalizá-la conforme necessário)
    return {'message': 'Dados salvos com sucesso'}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)