import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456789',
    database='testebd',
)

cursor = conexao.cursor()

# CRIANDO O CRUD
###################

# dica: Se o comando que for executado editar no banco de dados, será utilizado o "conexao.commit()";
# caso seja visualização, usará "valores = cursor.fetchall()"


# CREATE

nome= 'toddynho'
valor= 5
cursor.execute(f'''
               INSERT INTO vendas(nome_produto, valor)
               VALUES("{nome}",{valor})
               ''')
conexao.commit()

# READ

cursor.execute('''
               SELECT * FROM vendas               
               ''')
valores = cursor.fetchall()
print(valores)


# UPDATE

nome_produto = 'toddynho'
valor = 10
cursor.execute(f'''UPDATE vendas 
                SET valor={valor} 
                WHERE nome_produto="{nome_produto}"''')
conexao.commit()

# DELETE

nome = 'toddynho'
cursor.execute(f'''
               DELETE FROM vendas
               WHERE nome_produto="{nome}"
               ''')
conexao.commit()


cursor.close()
conexao.close()