# Importar a classe Flask e o objeto request:
from flask import Flask, request


# Criar o objeto Flask app:
app = Flask (__name__)

# Validador de nota de aluno
# http://127.0.0.1:5000/notas?nota1=5&nota2=9&nota3=2
@app.route ('/notas', methods=['GET'])
def menu_inicial():
    nota1 = float(request.args.get('nota1'))
    nota2 = float(request.args.get('nota2'))
    nota3 = float(request.args.get('nota3'))

    media = (nota1 + nota2 + nota3) / 3
    
    resp = ''

    if (media >= 0) and (media <3):
        resp='Reprovado'
    elif (media >= 3) and (media < 7):
        resp='Exame'
    elif (media >= 7) and (media <= 10):
        resp='Aprovado'
    
    return '''<h1>Média: {}</h1>
              <h1>Situação: {}</h1>'''.format(media, resp)

if __name__ == '__main__':
    # Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug = True, port = 5000)