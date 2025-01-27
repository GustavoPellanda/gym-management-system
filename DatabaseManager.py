import sqlite3

class DatabaseManager:
    def __init__(self, db_name="smartfyt.db"):
        """
        Conecta-se ao banco de dados SQLite. Se o banco não existir, ele será criado.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Cria as tabelas necessárias no banco de dados, caso não existam.
        """
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                cpf TEXT PRIMARY KEY,
                name TEXT,
                birth_date TEXT,
                email TEXT,
                workout TEXT
            )
        """)
        self.conn.commit()

    def SearchClient(self, cpf):
        """
        Busca um cliente no banco de dados pelo CPF.
        """
        self.cursor.execute("SELECT * FROM clients WHERE cpf=?", (cpf,))
        result = self.cursor.fetchone()
        if result:
            return {
                "cpf": result[0],
                "name": result[1],
                "birth_date": result[2],
                "email": result[3],
                "workout": result[4]
            }
        return None

    def RegisterClient(self, cpf, info):
        """
        Registra um novo cliente no banco de dados.
        """
        if self.SearchClient(cpf):
            raise ValueError("Cliente já registrado.")
        
        self.cursor.execute("""
            INSERT INTO clients (cpf, name, birth_date, email, workout)
            VALUES (?, ?, ?, ?, ?)
        """, (cpf, info['name'], info['birth_date'], info['email'], info.get('workout', None)))
        self.conn.commit()

    def UpdateClientInfo(self, cpf, info):
        """
        Atualiza as informações de um cliente no banco de dados.
        """
        self.cursor.execute("""
            UPDATE clients
            SET name=?, birth_date=?, email=?, workout=?
            WHERE cpf=?
        """, (info['name'], info['birth_date'], info['email'], info.get('workout', None), cpf))
        self.conn.commit()

    def close(self):
        """
        Fecha a conexão com o banco de dados.
        """
        self.conn.close()
