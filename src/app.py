from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        if email == 'exemplo@fatec.sp.gov.br' and senha == 'exemplo1':
            return redirect(url_for('index'))
        else:
            return render_template('login.html')

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/arquivos')
def arquivos():
    return render_template('arquivos.html')

@app.route('/enviar')
def enviar():
    return render_template('enviar.html')

@app.route('/configuraçoes')
def configuraçoes():
    return render_template('config.html')

@app.route('/registrar')
def regristrar():
    return render_template('registrar.html')

if __name__ == '__main__':
    app.run(port='8000', debug=True)
