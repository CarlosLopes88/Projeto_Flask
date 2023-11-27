from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def get_home():
    return render_template('home.html')

@app.route('/servicos')
def get_service():
    return render_template('services.html')

@app.route('/contato', methods=['GET', 'POST'])
def get_contact():
    if request.method == 'POST':
        nome_e_sobrenome = request.form['nome_e_sobrenome']
        email = request.form['email']
        telefone = request.form['telefone']
        mensagem = request.form['mensagem']
        contato = request.form['contato']
        receber_informacoes = 'receber_informacoes' in request.form

        data = {
            'nome_e_sobrenome': nome_e_sobrenome,
            'email': email,
            'telefone': telefone,
            'mensagem': mensagem,
            'contato': contato,
            'receber_informacoes': receber_informacoes
        }
        
        print(data)

        # Faça uma solicitação POST para a aplicação FastAPI
        url_fastapi = 'http://127.0.0.1:8000/salvar_dados'  # Substitua pelo endereço correto
        response = requests.post(url_fastapi, json=data)

        # Redirecionar para a página de contato com uma mensagem de sucesso
        return redirect(url_for('get_contact', success=True))

    success = request.args.get('success')
    return render_template('contact.html', success=success)

if __name__ == '__main__':
    app.run(debug=True)
