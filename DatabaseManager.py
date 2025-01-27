"""
Classe responsável por gerenciar o banco de dados do sistema.
"""

import sqlite3

class DatabaseManager:
    def __init__(self, database_file="clients.db"):
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()
        self._create_clients_table()

    def _create_clients_table(self):
        """
        Cria a tabela de clientes no banco de dados, caso não exista.
        """
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS clients (
            cpf TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            birth_date TEXT NOT NULL,
            email TEXT NOT NULL
        )
        """)
        self.connection.commit()

    def SearchClient(self, cpf):
        """
        Busca um cliente no banco de dados pelo CPF.
        """
        self.cursor.execute("SELECT * FROM clients WHERE cpf = ?", (cpf,))
        return self.cursor.fetchone()

    def RegisterClient(self, cpf, info):
        """
        Registra um novo cliente no banco de dados.
        """
        try:
            self.cursor.execute(
                "INSERT INTO clients (cpf, name, birth_date, email) VALUES (?, ?, ?, ?)",
                (cpf, info["name"], info["birth_date"], info["email"])
            )
            self.connection.commit()
        except sqlite3.IntegrityError:
            raise ValueError("Cliente já registrado.")

    def UpdateClientInfo(self, cpf, info):
        """
        Atualiza as informações de um cliente no banco de dados.
        """
        if self.SearchClient(cpf) is None:
            raise ValueError("Cliente não encontrado.")

        self.cursor.execute(
            "UPDATE clients SET name = ?, birth_date = ?, email = ? WHERE cpf = ?",
            (info["name"], info["birth_date"], info["email"], cpf)
        )
        self.connection.commit()

    def __del__(self):
        """
        Fecha a conexão com o banco de dados ao destruir o objeto.
        """
        self.connection.close()
