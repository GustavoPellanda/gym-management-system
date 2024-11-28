"""
Classe responsável por gerenciar o banco de dados do sistema.
"""

class DatabaseManager:
    def __init__(self):
        self.clients = {}

    def SearchClient(self, cpf):
        """
        Busca um cliente no banco de dados pelo CPF.
        """
        return self.clients.get(cpf)

    def RegisterClient(self, cpf, info):
        """
        Registra um novo cliente no banco de dados.
        """
        if cpf in self.clients:
            raise ValueError("Cliente já registrado.")
        self.clients[cpf] = info

    def UpdateClientInfo(self, cpf, info):
        """
        Atualiza as informações de um cliente no banco de dados.
        """
        if cpf not in self.clients:
            raise ValueError("Cliente não encontrado.")
        self.clients[cpf] = info

    def SearchWorkout(self, cpf):
        """
        Busca o treino associado a um cliente pelo CPF.
        """
        client = self.SearchClient(cpf)
        if client:
            return client.get("workout")
        return None

    def RegisterWorkout(self, cpf, workout):
        """
        Associa um treino a um cliente no banco de dados.
        """
        client = self.SearchClient(cpf)
        if not client:
            raise ValueError("Cliente não encontrado.")
        client["workout"] = workout