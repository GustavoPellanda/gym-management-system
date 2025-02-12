import datetime

class DatabaseManager:
    def __init__(self):
        self.clients = {}  
        self.employees = {}  

    def register_client(self, cpf, info):
        if cpf in self.clients:
            raise ValueError("Cliente já registrado.")
        info['access_records'] = []
        self.clients[cpf] = info

    def validate_access_and_register_entry(self, cpf):
        if cpf not in self.clients:
            raise ValueError("Cliente não encontrado.")
        
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.clients[cpf]['access_records'].append(current_time)
        return f"Acesso permitido para {self.clients[cpf]['name']} às {current_time}."

    def get_access_records(self, cpf):
        if cpf not in self.clients:
            raise ValueError("Cliente não encontrado.")
        return self.clients[cpf]['access_records']

    def SearchWorkout(self, cpf):
        if cpf not in self.clients:
            raise ValueError("Cliente não encontrado.")
        return self.clients[cpf].get('workout', 'Nenhum treino atribuído.')

    def SearchClient(self, cpf):
        return self.clients.get(cpf)

    def update_client_info(self, cpf, info):
        if cpf not in self.clients:
            raise ValueError("Cliente não encontrado.")
        for key, value in info.items():
            self.clients[cpf][key] = value

    def register_employee(self, employee_id, name):
        if employee_id in self.employees:
            raise ValueError("Funcionário já registrado.")
        self.employees[employee_id] = {
            'name': name,
            'records': []  
        }
        return f"Funcionário {name} registrado com sucesso."

    def check_in(self, employee_id):
        if employee_id not in self.employees:
            raise ValueError("Funcionário não encontrado.")
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.employees[employee_id]['records'].append({'check_in': current_time, 'check_out': None})
        return f"Entrada registrada para {self.employees[employee_id]['name']} às {current_time}."

    def check_out(self, employee_id):
        if employee_id not in self.employees:
            raise ValueError("Funcionário não encontrado.")
        
        if not self.employees[employee_id]['records'] or self.employees[employee_id]['records'][-1]['check_out'] is not None:
            raise ValueError("Hora de entrada não registrada ou já finalizada.")

        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.employees[employee_id]['records'][-1]['check_out'] = current_time
        return f"Saída registrada para {self.employees[employee_id]['name']} às {current_time}."

    def get_employee_data(self, employee_id):
        if employee_id not in self.employees:
            raise ValueError("Funcionário não encontrado.")
        return self.employees[employee_id]
