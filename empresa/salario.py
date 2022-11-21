# Importar a classe Flask, objeto request e o objeto jsonify:
from flask import Flask, request, jsonify
# Criar o objeto Flask app:
app = Flask(__name__)
# http://127.0.0.1:5000/salario
# Aceita requisições com o método POST.
# O corpo da requisição deve conter um objeto JSON
# como o apresentado abaixo:
# {
# "hora" : "10",
# "horaextra" : "2"
# }
@app.route('/salario', methods=['POST'])
def verifica_salario():
    objeto_json = request.get_json()

    # Verificar se o ojeto no formato JSON é NULL.
    if objeto_json is not None:
        if 'hora' in objeto_json:
            hora = float(objeto_json['hora'])

        if 'horaextra' in objeto_json:
            horaextra = float(objeto_json['horaextra'])

    hora = hora * 40.00
    horaextra = horaextra * 50.00
    salariob = hora + horaextra
    salariol = salariob - (salariob * 0.1)

    return '''
                Valor total das horas trabalhadas: {}
                Valor total das horas extras trabalhadas: {}
                Salário Bruto: {}
                Salário Líquido: {}
           '''.format(hora, horaextra, salariob, salariol)

if __name__ == '__main__':
    # Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug = True, port = 5000)