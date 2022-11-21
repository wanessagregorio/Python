# Importar a classe Flask, objeto request e o objeto jsonify:
from flask import Flask, request, jsonify
# Criar o objeto Flask app:
app = Flask(__name__)
produtos = [{'codigo': '1', 'nome': 'sapato', 'preco': 99.99},
            {'codigo': '2', 'nome': 'bolsa', 'preco': 103.89},
            {'codigo': '3', 'nome': 'camisa', 'preco': 49.98},
            {'codigo': '4', 'nome': 'calça', 'preco': 89.72},
            {'codigo': '5', 'nome': 'blusa', 'preco': 97.35}]


# http://127.0.0.1:5000/produtos/1
@app.route('/produtos/<string:codigo>', methods=['GET'])
def retornar_dados_do_produto_informado(codigo):
    resp = {'produto': '', 'preco': '', 'codigo': '', 'nome':''}
    for produto in produtos:
        if produto['codigo'] == codigo:
            resp = produto
    return jsonify(resp)



if __name__ == '__main__':
    # Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug = True, port = 5000)