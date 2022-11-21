# Importar a classe Flask e o objeto request:
from flask import Flask, request
# Criar o objeto Flask app:
app = Flask(__name__)
# http://127.0.0.1:5000/triangulo
# Aceita requisições com o método POST.
# O corpo da requisição deve conter um objeto JSON
# como o apresentado abaixo:
# {
# "valorx" : "5",
# "valory" : "2",
# "valorz" : "4"
# }
@app.route('/triangulo', methods=['POST'])
def verifica_triangulo():
    objeto_json = request.get_json()

    # Verificar se o ojeto no formato JSON é NULL.
    if objeto_json is not None:
        if 'valorx' in objeto_json:
            valorx = float(objeto_json['valorx'])

        if 'valory' in objeto_json:
            valory = float(objeto_json['valory'])

        if 'valorz' in objeto_json:
            valorz = float(objeto_json['valorz'])
        
    resp = 'Não podem ser comprimentos de um triângulo'

    if (valorx < valory + valorz) and (valory < valorx + valorz) and (valorz < valorx + valory):
        if (valorx > abs(valory - valorz)) and (valory > abs(valorx - valorz)) and (valorz > abs(valorx - valory)):
           resp = 'Podem ser comprimentos de um triângulo'

    return '''
                Valor X informado: {}
                Valor Y informado: {}
                Valor Z informado: {}
                Resposta: {}
           '''.format(valorx, valory, valorz, resp)

if __name__ == '__main__':
    # Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug = True, port = 5000)