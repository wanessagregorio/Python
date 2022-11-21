# Importar a classe Flask e o objeto request:
from flask import Flask, request

# Criar o objeto Flask app:
app = Flask (__name__)

# Peso IMC
# http://127.0.0.1:5000/imc?peso=80&altura=1.90
@app.route ('/imc', methods=['GET'])

def menu_inicial():
    peso = float(request.args.get('peso'))
    altura = float(request.args.get('altura'))

    imc = peso / (altura * altura)

    resp = ''

    if (imc <=18,5):
        resp='Abaixo do peso'
    elif (imc >= 18,6) and (imc < 24,9):
        resp='Peso ideal! Parabens'
    elif (imc >= 25,0) and (imc <= 29,9):
        resp='Levemente acima do peso'
    elif (imc >= 30,0) and (imc <= 34,9):
        resp='Obesidade grau I'
    elif (imc >= 35,0) and (imc <= 39,9):
        resp='Obesidade grau II (Severa)'
    elif (imc >= 40):
        resp='Obesidade grau III (Morbida)'

    return '''<h1>IMC: {}</h1>
    <h1>Situação: {}</h1>'''.format(imc, resp)

if __name__ == '__main__':
# Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug = True, port = 5000)
