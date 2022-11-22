from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

PRODUTOS = [{'id': 1, 'nome': 'Ana', 'nota': 72.00},
            {'id': 2, 'nome': 'Bruna', 'nota': 71.50},
            {'id': 3, 'nome': 'Carlos', 'nota': 68.50},
            {'id': 4, 'nome': 'Diogo', 'nota': 70.00},
            {'id': 5, 'nome': 'Ester', 'nota': 69.00}]

def aborta_se_o_produto_nao_existe(id):
    encontrei = False

    for produto in PRODUTOS:

        if produto['id'] == int(id):
            encontrei = True
    
    if encontrei == False:
        abort(404, mensagem="O produto com id = {} não existe".format(id)) #404:Not Found

# Parse dos dados enviados na requisição no formato JSON:
parser = reqparse.RequestParser()
parser.add_argument('id', type=int, help='identificador do produto')
parser.add_argument('nome', type=str, help='nome do produto')
parser.add_argument('nota', type=float, help='preço do produto')

# Produto:
# 1) Apresenta um único produto.
# 2) Remove um único produto.
# 3) Atualiza (substitui) um produto.
class Produto(Resource):
    def get(self, id):
        aborta_se_o_produto_nao_existe(id)
        return PRODUTOS[int(id)]

    def delete(self, id):
        aborta_se_o_produto_nao_existe(id)
        del PRODUTOS[int(id)]
        return '', 204, #204: No Content

    def put(self, id):
        aborta_se_o_produto_nao_existe(id)
        args = parser.parse_args()
        for produto in PRODUTOS:
            if produto['id'] == int(id):
                produto['id'] = args['id']
                produto['nome'] = args['nome']
                produto['nota'] = args['nota']
                break
        return produto, 200, #200: OK

# ListaProduto:
# 1) Apresenta a lista de produtos.
# 2) Insere um novo produto.
class ListaProduto(Resource):
    def get(self):
        return PRODUTOS

    def post(self):
        args = parser.parse_args()
        id = -1

        for produto in PRODUTOS:
            if int(produto['id']) > id:
                id = int(produto['id'])
        id = id + 1
        produto = {'id': id, 'nome': args['nome'], 'nota': args['nota']}
        PRODUTOS.append(produto)
        return produto, 201, #201: Created

##
## Roteamento de recursos:
##
api.add_resource(Produto, '/produtos/<id>')
api.add_resource(ListaProduto, '/produtos')

if __name__ == '__main__':
    app.run(debug=True)