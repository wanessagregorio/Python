# Importar a classe Flask, objeto request e o objeto jsonify:
from flask import Flask, request, jsonify
# Criar o objeto Flask app:
app = Flask(__name__)
produtos = [{'codigo': '1', 'nome': 'Cachorro quente', 'preco': 12.00},
            {'codigo': '2', 'nome': 'Sanduíche', 'preco': 23.89},
            {'codigo': '3', 'nome': 'Pastel', 'preco': 3.98},
            {'codigo': '4', 'nome': 'Refrigerante', 'preco': 5.72},
            {'codigo': '5', 'nome': 'Suco', 'preco': 4.35}]

# http://127.0.0.1:5000/produtos
@app.route('/produtos', methods=['GET'])
def retornar_todos_os_produtos():
    return jsonify({'produtos': produtos})

# http://127.0.0.1:5000/produtos/2
@app.route('/produtos/<string:codigo>', methods=['GET'])
def retornar_dados_do_produto_informado(codigo):
    resp = {'produto': '', 'codigo': '', 'nome': '', 'preco': ''}
    for produto in produtos:
        if produto['codigo'] == codigo:
            resp = produto
    return jsonify(resp)

# http://127.0.0.1:5000/produtos/6/pizza/53.49
@app.route('/produtos/<int:codigo>/<string:nome>/<float:preco>', methods=['POST'])
def inserir_produto(codigo, nome, preco):
    produtos.append({'produto': codigo,'nome': nome,'preco': preco})
    return jsonify({'produto': codigo,'nome': nome, 'preco': preco})


# http://127.0.0.1:5000/produtos/5/10.00
# http://127.0.0.1:5000/produtos/5/-10.00
@app.route('/produtos/<string:codigo>/<float(signed=True):preco>',
methods=['PATCH'])
def alterar_preco_do_produto(codigo, preco):
    resp = {'produto': '', 'preco': None}
    for produto in produtos:
        if produto['codigo'] == codigo:
            produto['preco'] += preco
            resp = produto
    return jsonify(resp)

# http://127.0.0.1:5000/produtos/5
@app.route('/produtos/<string:codigo>', methods=['DELETE'])
def remover_produto(codigo):
    for i, produto in enumerate(produtos):
        if produto['codigo'] == codigo:
            del produtos[i]
    return jsonify({'produtos': produtos})

if __name__ == '__main__':
    # Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug = True, port = 5000)