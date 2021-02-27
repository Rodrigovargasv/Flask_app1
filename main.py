from flask import Flask, render_template, request, redirect, url_for
from app.models.database import Database

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        email = request.form.get('email')
        #recebe o email e passa para o init de Database
        gerenciadoDb = Database(email)
        #insere os dados recebido na base de dados
        gerenciadoDb.gravaDadosTabela()
        #cria a tabela de dados caso não tenha 
        gerenciadoDb.dbContato()
        
        return redirect(url_for('bemvindo'))
    return render_template('login.html')

@app.route('/bemvindo', methods=['GET', 'POST'])
def bemvindo():
    if request.method == 'GET':
        return render_template('index.html')
app.run(debug=True)