# Importar a classe Flask e o objeto request:
from flask import Flask, request

# Criar o objeto Flask app:
app = Flask (__name__)

# Distância
# http://127.0.0.1:5000/distancia?x1=80&x2=60&y1=90&y2=30
@app.route ('/distancia', methods=['GET'])

def menu_inicial():
    x1 = float(request.args.get('x1'))
    x2 = float(request.args.get('x2'))
    y1 = float(request.args.get('y1'))
    y2 = float(request.args.get('y2'))

    d = pow(((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1)))

    return '''<h1>A distância entre eles é: {}</h1>
           '''.format(d)

if __name__ == '__main__':
# Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug = True, port = 5000)
