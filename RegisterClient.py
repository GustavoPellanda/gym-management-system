"""
Classe responsável por registrar clientes no sistema.
"""

class RegisterClient:
    def __init__(self, database_manager):
        self.database_manager = database_manager

    def SetClientInfo(self, cpf, info):
        """
        Define as informações do cliente e registra ou atualiza conforme necessário.
        """
        if not cpf or not info:
            raise ValueError("CPF e informações são obrigatórios.")
        
        # Se o cliente não existir, cria um novo
        if self.database_manager.SearchClient(cpf) is None:
            self.database_manager.RegisterClient(cpf, info)
        else:
            self.database_manager.UpdateClientInfo(cpf, info)