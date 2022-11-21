# Importar a classe Flask e o objeto request:
from flask import Flask, request

# Criar o objeto Flask app:
app = Flask (__name__)

# Media tres numeros
# http://127.0.0.1:5000/mediatresnumeros?a=80&b=60&c=90
@app.route ('/mediatresnumeros', methods=['GET'])

def menu_inicial():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    c = float(request.args.get('c'))

    media = (a + b + c) / 3

    maior = a

    if (b > a) and (b > c):
        maior = b
    if (c > a) and (c > b):
        maior = c


    menor = a

    if (b < a) and (b < c):
        menor = b
    if (c < a) and (c < b):
        menor = c

    return '''<h1>Maior: {}</h1>
             <h1>Menor: {}</h1>
             <h1>Media: {}</h1>'''.format(maior,menor, media)

if __name__ == '__main__':
# Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug = True, port = 5000)
