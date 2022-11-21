# Importar a classe Flask, objeto request e o objeto jsonify:
from flask import Flask, request, jsonify
# Criar o objeto Flask app:
app = Flask(__name__)
matriculas = [{'codigo': '1', 'nome': 'Ana', 'nota': 72.00},
            {'codigo': '2', 'nome': 'Bruna', 'nota': 71.50},
            {'codigo': '3', 'nome': 'Carlos', 'nota': 68.50},
            {'codigo': '4', 'nome': 'Diogo', 'nota': 70.00},
            {'codigo': '5', 'nome': 'Ester', 'nota': 69.00}]

# http://127.0.0.1:5000/matriculas
@app.route('/matriculas', methods=['GET'])
def retornar_todos_os_matriculas():
    return jsonify({'matriculas': matriculas})

# http://127.0.0.1:5000/matriculas/2
@app.route('/matriculas/<string:codigo>', methods=['GET'])
def retornar_dados_do_matricula_informado(codigo):
    resp = {'matricula': '', 'codigo': '', 'nome': '', 'nota': ''}
    for matricula in matriculas:
        if matricula['codigo'] == codigo:
            resp = matricula
    return jsonify(resp)

# http://127.0.0.1:5000/matriculas/6/Junior/75.25
@app.route('/matriculas/<int:codigo>/<string:nome>/<float:nota>', methods=['POST'])
def inserir_matricula(codigo, nome, nota):
    matriculas.append({'matricula': codigo,'nome': nome,'nota': nota})
    return jsonify({'matricula': codigo,'nome': nome, 'nota': nota})


# http://127.0.0.1:5000/matriculas/5/10.00
# http://127.0.0.1:5000/matriculas/5/-10.00
@app.route('/matriculas/<string:codigo>/<float(signed=True):nota>',
methods=['PATCH'])
def alterar_nota_do_matricula(codigo, nota):
    resp = {'matricula': '', 'nota': None}
    for matricula in matriculas:
        if matricula['codigo'] == codigo:
            matricula['nota'] += nota
            resp = matricula
    return jsonify(resp)

# http://127.0.0.1:5000/matriculas/5
@app.route('/matriculas/<string:codigo>', methods=['DELETE'])
def remover_matricula(codigo):
    for i, matricula in enumerate(matriculas):
        if matricula['codigo'] == codigo:
            del matriculas[i]
    return jsonify({'matriculas': matriculas})

if __name__ == '__main__':
    # Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug = True, port = 5000)