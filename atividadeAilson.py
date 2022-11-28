from flask import Flask, jsonify, request

atividadeAilson = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'O senhor dos Anéis - A sociedade do Anel',
        'autor': 'J.R.R. Tolkien',
        'Preço': 'R$ 45,00'
    },
    {
        'id': 2,
        'título': 'O senhor dos Anéis - As duas torres',
        'autor': 'J.R.R. Tolkien',
        'Preço': 'R$ 45,00'
    },
    {
        'id': 3,
        'título': 'O senhor dos Anéis -  O retorno do rei',
        'autor': 'J.R.R. Tolkien',
        'Preço': 'R$ 45,00'
    },
    {
        'id': 4,
        'título': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K. Rowling',
        'Preço': 'R$ 45,00'
    },
    {
        'id': 5,
        'título': 'Harry Potter e a Câmara Secreta ',
        'autor': 'J.K. Rowling',
        'Preço': 'R$ 45,00'
    },
    {
        'id': 6,
        'título': 'Harry Potter e o Prisioneiro de Azkaban',
        'autor': 'J.K. Rowling',
        'Preço': 'R$ 45,00'
    },
    {
        'id': 7,
        'título': 'Harry Potter e o Cálice de Fogo',
        'autor': 'J.K. Rowling',
        'Preço': 'R$ 45,00'
    },
    {
        'id': 8,
        'título': 'Harry Potter e a Ordem da Fênix',
        'autor': 'J.K. Rowling',
        'Preço': 'R$ 45,00'
    },
    {
        'id': 9,
        'título': 'Harry Potter e o Enigma do Príncipe',
        'autor': 'J.K. Rowling',
        'Preço': 'R$ 45,00'
    },
    {
        'id': 10,
        'título': 'Harry Potter e as Relíquias da Morte',
        'autor': 'J.K. Rowling',
        'Preço': 'R$ 45,00'
    },
    {
        'id': 11,
        'título': 'Harry Potter e a Criança Amaldiçoada',
        'autor': 'J.K. Rowling',
        'Preço': 'R$ 45,00'
    }
]

# consultar(todos)
@atividadeAilson.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

# consultar(id)
@atividadeAilson.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
# editar
@atividadeAilson.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        livros[indice].update(livro_alterado)
        return jsonify(livros[indice])
# criar
@atividadeAilson.route('/livros',methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)
# excluir
@atividadeAilson.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)

atividadeAilson.run(port=5000,host='localhost',debug=True)