"""
Classe responsável por registrar clientes no sistema.
"""

class RegisterClient:
    def __init__(self, database_manager):
        self.database_manager = database_manager

    def SetClientName(self, cpf, name):
        """
        Define o nome do cliente e registra no sistema.
        """
        if not cpf or not name:
            raise ValueError("CPF e Nome são obrigatórios.")
        self.database_manager.RegisterClient(cpf, {"name": name, "workout": None})

    def SetClientInfo(self, cpf, info):
        """
        Define informações adicionais para o cliente.
        Registra o cliente se ele não existir.
        """
        if not cpf or not info:
            raise ValueError("CPF e informações são obrigatórios.")
        # Verifica se o cliente já existe, caso contrário, registra-o
        if self.database_manager.SearchClient(cpf) is None:
            self.database_manager.RegisterClient(cpf, info)
        else:
            self.database_manager.UpdateClientInfo(cpf, info)