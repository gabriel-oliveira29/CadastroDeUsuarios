# 1. Cadastro de Novos Usuários:
#  O programa deve permitir que o usuário insira dados como nome, e-mail e idade,
# e armazene esses dados no banco de dados(tudo pelo terminal).
# 2. Visualização de Usuários Cadastrados:
#  O usuário pode visualizar a lista de todos os usuários cadastrados, incluindo
# suas informações.
# 3. Atualização de Usuários:
#  O programa deve permitir que o usuário atualize as informações de um cadastro
# existente no banco de dados.
# 4. Remoção de Usuários:
#  O programa deve permitir que o usuário remova cadastros do banco de dados.
# 5. Persistência dos Dados:
#  Os dados devem ser salvos em um banco de dados PostgresSQL para que o sistema
# possa ser reutilizado em diferentes sessões

import psycopg2

conexao = psycopg2.connect (
    dbname = 'localhost',
    host = 'localhost',
    user = 'postgres',
    password = 'admin',
    port = '5432'
)

# criando tabela
cursor = conexao.cursor()
cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS Usuários (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        idade INTEGER NOT NULL,
        email VARCHAR(255) NOT NULL
    );
''')

def cadastro_usuarios():
    nome = input('digite o nome: ')
    idade = int(input('digite a idade: '))
    email = input('digite o email: ')
    
    cursor.execute("INSERT INTO Usuários (nome, idade, email) VALUES (%s, %s, %s)",(nome, idade, email))
    conexao.commit()

def atualizar_usuarios():
    id = input('informe o ID do usuario: ')
    idade = int(input('informe a idade atualizada: '))
    email  = input('informe o email atualizado: ')

    cursor.execute("UPDATE Usuários SET idade = %s, email = %s WHERE id = %s", (idade, email, id))
    conexao.commit()

def remover_usuarios():
    id = input('informe o ID do usuario: ')
   
    cursor.execute("DELETE FROM Usuários WHERE id = %s",(id,))
    conexao.commit()

def vizualizar_usuarios():
    cursor.execute("SELECT * FROM Usuários")
    usuarios = cursor.fetchall()
    print(usuarios)



while True:
    print('1- Cadastrar usuario')
    print('2- atualizar usuario')
    print('3- remover usuario')
    print('4- vizualizar usuario')
    print('0- sair')

    escolha = input('')

    if escolha == '1':
        cadastro_usuarios()
    elif escolha == '2':
        atualizar_usuarios()
    elif escolha == '3':
        remover_usuarios()
    elif escolha == '4':
        vizualizar_usuarios()
    elif escolha > '4':
        print('numero invalido !!')
    elif escolha == '0':
        break
