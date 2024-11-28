"""
Classe responsável por criar a interface do sistema.
Ela possui botões e campos de texto que o usuário 
utiliza para acessar as funcionalidades do sistema.
"""

import tkinter as tk
from tkinter import messagebox

class Interface:
    def __init__(self):
        # Inicializar a janela principal
        self.window = tk.Tk()
        self.window.title("Sistema de Gestão de Treinos")
        self.window.geometry("400x300")
        
        # Adicionar os botões para cada funcionalidade
        self.create_buttons()
        
        # Executar o loop da interface
        self.window.mainloop()

    def create_buttons(self):
        # Botões para acessar as funcionalidades
        buttons = [
            ("Validar Acesso", self.SelectValidateAccess),
            ("Registrar Cliente", self.SelectRegisterClient),
            ("Enviar Treino", self.SelectSendWorkout),
            ("Procurar Cliente", self.SelectFindClient),
            ("Checar Treino", self.SelectCheckWorkout),
        ]
        
        for i, (label, command) in enumerate(buttons):
            button = tk.Button(self.window, text=label, command=command, width=25, height=2)
            button.pack(pady=10)

    def SelectValidateAccess(self):
        messagebox.showinfo("Ação", "Validação de acesso selecionada.")

    def SelectRegisterClient(self):
        messagebox.showinfo("Ação", "Registro de cliente selecionado.")

    def SelectSendWorkout(self):
        messagebox.showinfo("Ação", "Envio de treino selecionado.")

    def SelectFindClient(self):
        messagebox.showinfo("Ação", "Busca de cliente selecionada.")

    def SelectCheckWorkout(self):
        messagebox.showinfo("Ação", "Checagem de treino selecionada.")

# Criar e executar a interface
if __name__ == "__main__":
    Interface()
