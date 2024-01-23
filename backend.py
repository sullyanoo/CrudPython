import sqlite3 as sql

class TransactionObject():
    ## Declaracao dos dados para se conectar ao banco de dados.
    database = "clientes.db"
    conn = None
    cur = None
    connected = False

    ## Funcao onde sera realizado a conexao.
    def connect(self):
        self.conn = sql.connect(self.database) ## Trecho que que realiza a conexao.
        self.cur = self.conn.cursor() ## Trecho que define o cursor para usarmos comandos SQL.
        self.connected = True ## Altera o status de conexao.

    ## Funcao de desconexao.
    def disconnect(self):
        self.conn.close() ## Fecha a sessao de conexao com o banco de dados.
        self.connected = False ## Altera o status de conexao.

    ## Funcao onde iremos mandar nossos comandos SQL. (self - Instacia da classe Transactiontobject, sql - Comandos SQL, parms - Parametros Opcionais SQL)
    def execute(self, sql, parms=None):
        if self.connected:
            if parms is None:
                self.cur.execute(sql)
            else:
                self.cur.execute(sql, parms)
            return True
        else:
            return False

    ## Este comando retorna todas as linhas resultantes da última consulta executada no cursor (self.cur). O método fetchall é geralmente usado após a execução de uma consulta SELECT para recuperar todas as linhas do conjunto de resultados.
    def fetchall(self):
        return self.cur.fetchall()

    ## Funcao que ira pesistir os dados enviados para o banco.
    def persist(self):
        if self.connected:
            self.conn.commit()
            return True
        else:
            return False

    ## Funcao inicia o banco e verifica se a tabela ja existe.
    def initDB(self):
        self.connect() ## Trecho que inicia o banco.
        self.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)") ## Trecho que verifica se a tabela no banco existe, se nao existir o trecho em SQL vai criar.
        self.persist() ## Persiste os dados se a tabela nao existir.
        self.disconnect() ## Desconecta a sessao.

    def insert(self, nome, sobrenome, email, cpf):
        self.connect()
        self.execute("INSERT INTO clientes VALUES(NULL, ?,?,?,?)", (nome, sobrenome, email, cpf)) ## Inclue um cadastro novo.
        self.persist()
        self.disconnect()

    def view(self):
        self.connect()
        self.execute("SELECT * FROM clientes") ## Busca todos os cadastros tabela.
        rows = self.fetchall()
        self.disconnect()
        return rows

    def search(self, nome="", sobrenome="", email="", cpf=""):
        self.connect()
        self.execute("SELECT * FROM clientes WHERE nome = ? or sobrenome = ? or email = ? or cpf = ?", (nome, sobrenome, email, cpf)) ## Busca um cadastro especifico.
        rows = self.fetchall()
        self.disconnect()
        return rows ## Retorna os dados buscados com o (fetchall)

    def delete(self, id):
        self.connect()
        self.execute("DELETE FROM clientes WHERE id = ?", (id,)) ## Deleta um cadastro.
        self.persist()
        self.disconnect()

    def update(self, id, nome, sobrenome, email, cpf):
        self.connect()
        self.execute("UPDATE clientes SET nome = ?, sobrenome = ?, email = ?, cpf = ? WHERE id = ?", (nome, sobrenome, email, cpf, id)) ## Atualiza um cadastro.
        self.persist()
        self.disconnect()
