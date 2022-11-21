# Importar a classe Flask, objeto request e o objeto jsonify:
from flask import Flask, request, jsonify
# Criar o objeto Flask app:
app = Flask(__name__)
produtos = [{'codigo': '1', 'nome': 'Camiseta P', 'preco': 10.00},
            {'codigo': '2', 'nome': 'Camiseta M', 'preco': 12.00},
            {'codigo': '3', 'nome': 'Camiseta G', 'preco': 15.00}]

# http://127.0.0.1:5000/fabrica
# Aceita requisições com o método POST.
# O corpo da requisição deve conter um objeto JSON
# como o apresentado abaixo:
# {
# "camisetap" : "5",
# "camisetam" : "4",
# "camisetag" : "2"
# }
@app.route('/fabrica', methods=['POST'])
def verifica_camiseta():
    objeto_json = request.get_json()

    # Verificar se o ojeto no formato JSON é NULL.
    if objeto_json is not None:
        if 'camisetap' in objeto_json:
            camisetap = float(objeto_json['camisetap'])

        if 'camisetam' in objeto_json:
            camisetam = float(objeto_json['camisetam'])

        if 'camisetag' in objeto_json:
            camisetag = float(objeto_json['camisetag'])
        
    valorp = camisetap * 10.00
    valorm = camisetam * 12.00
    valorg = camisetag * 15.00
    total  = valorp + valorm + valorg

    return '''
                Quantidade de camisetas P: {}
                Quantidade de camisetas M: {}
                Quantidade de camisetas G: {}
                Valor arrecadado de camisetas P: {}
                Valor arrecadado de camisetas M: {}
                Valor arrecadado de camisetas G: {}
                Valor arrecadado total: {}
           '''.format(camisetap, camisetam, camisetag, valorp, valorm, valorg, total)

if __name__ == '__main__':
    # Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug = True, port = 5000)