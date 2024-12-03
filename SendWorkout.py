"""
Classe responsável por enviar treinos para clientes.
"""

class SendWorkout:
    def __init__(self, database_manager):
        self.database_manager = database_manager

    def GetClient(self, cpf):
        """
        Busca um cliente no sistema.
        """
        client = self.database_manager.SearchClient(cpf)
        if not client:
            raise ValueError("Cliente não encontrado.")
        return client

    def WriteWorkout(self, cpf, workout):
        """
        Registra o treino para o cliente.
        """
        if not workout:
            raise ValueError("Treino não pode ser vazio.")
        client = self.GetClient(cpf)
        client["workout"] = workout
        self.database_manager.UpdateClientInfo(cpf, client)

    def SendWorkout(self, cpf, workout):
        """
        Método principal para associar o treino ao cliente.
        """
        self.WriteWorkout(cpf, workout)
