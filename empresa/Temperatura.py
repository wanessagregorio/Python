# Importar a classe Flask e o objeto request:
from flask import Flask, request


# Criar o objeto Flask app:
app = Flask (__name__)

# Validador de nota de aluno
# http://127.0.0.1:5000/temperatura?temp=25
@app.route ('/temperatura', methods=['GET'])
def menu_inicial():
    temp = float(request.args.get('temp'))

    fah = (temp * 1.8) + 32
    
    return '''<h1>Temperatura correspondente
em Fahrenheit.: {}</h1>'''.format(fah)

if __name__ == '__main__':
    # Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug = True, port = 5000)