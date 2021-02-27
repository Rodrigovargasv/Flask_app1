import sqlite3


class Database:
    #inicia um conxeção com banco de dados
    def __init__(self, email):
        self.connection = sqlite3.connect('database.db')
        self.email = email   
    try:
        #está função insere dados no banco dados.
        def gravaDadosTabela(self):
            #separar o dominio do email
            cur = self.connection.cursor()
            verifica = self.email
            a = verifica.split('@')
            b = a[1:]
            c = ''.join(b)
            dominio = '@' + c
            try:
                #grava o email e dominio no banco de dados
                cur.execute("INSERT INTO email (emailUser, dominio) VALUES (?,?)" ,
                            (self.email, dominio)
                            )
              
                self.connection.commit()
            except:
                print('eu ao tenta inserir o dados no banco de dado')            
    except :
        ('erro')
    #cria a tabela
    def dbContato(self):
        cur = self.connection.cursor()
        cur.execute('''
                    CREATE TABLE IF NOT EXISTS email(
                        id integer primary key,
                        emailUser text,
                        dominio text
                        
                        );
                    ''')

        # fecha conexão
        self.connection.close()
   
        