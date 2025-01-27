"""
Classe responsável por criar a interface do sistema.
Ela possui botões e campos de texto que o usuário 
utiliza para acessar as funcionalidades do sistema.
"""

import tkinter as tk
from tkinter import messagebox, Menu
from tkinter.simpledialog import askstring
from RegisterClient import RegisterClient
from SendWorkout import SendWorkout
from DatabaseManager import DatabaseManager


class Interface:
    def __init__(self):
        self.database_manager = DatabaseManager()
        self.register_client = RegisterClient(self.database_manager)
        self.send_workout = SendWorkout(self.database_manager)
        self.window = tk.Tk()
        self.window.title("Smart Fyt Sistema")
        self.window.geometry("1024x768")
        self.create_menu_bar()
        self.create_toolbar()
        self.create_logo()
        self.window.mainloop()

    def create_menu_bar(self):
        menu_bar = Menu(self.window)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Sair", command=self.window.quit)
        menu_bar.add_cascade(label="Arquivo", menu=file_menu)

        register_menu = Menu(menu_bar, tearoff=0)
        register_menu.add_command(label="Registrar Cliente", command=self.SelectRegisterClient)
        menu_bar.add_cascade(label="Cadastros", menu=register_menu)

        access_menu = Menu(menu_bar, tearoff=0)
        access_menu.add_command(label="Validar Acesso", command=self.SelectValidateAccess)
        menu_bar.add_cascade(label="Acesso", menu=access_menu)

        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Sobre", command=self.show_about)
        menu_bar.add_cascade(label="Ajuda", menu=help_menu)
        
        self.window.config(menu=menu_bar)

    def create_toolbar(self):
        toolbar = tk.Frame(self.window, bd=1, relief=tk.RAISED)

        register_icon = tk.Button(toolbar, text="Registrar Cliente", command=self.SelectRegisterClient, width=15)
        register_icon.pack(side=tk.LEFT, padx=2, pady=2)

        send_workout_icon = tk.Button(toolbar, text="Enviar Treino", command=self.SelectSendWorkout, width=15)
        send_workout_icon.pack(side=tk.LEFT, padx=2, pady=2)

        find_client_icon = tk.Button(toolbar, text="Procurar Cliente", command=self.SelectFindClient, width=15)
        find_client_icon.pack(side=tk.LEFT, padx=2, pady=2)

        check_workout_icon = tk.Button(toolbar, text="Checar Treino", command=self.SelectCheckWorkout, width=15)
        check_workout_icon.pack(side=tk.LEFT, padx=2, pady=2)

        validate_access_icon = tk.Button(toolbar, text="Validar Acesso", command=self.SelectValidateAccess, width=15)
        validate_access_icon.pack(side=tk.LEFT, padx=2, pady=2)

        toolbar.pack(side=tk.TOP, fill=tk.X)

    def create_logo(self):
        logo_frame = tk.Frame(self.window)
        logo_frame.pack(expand=True)

        tk.Label(logo_frame, text="Smart Fyt", font=("Helvetica", 48, "bold"), fg="blue").pack()
        tk.Label(logo_frame, text="Saude", font=("Helvetica", 24), fg="gray").pack()

    def show_about(self):
        messagebox.showinfo(
            "Sobre",
            "Smart Fyt Sistema\nVersão 1.0\n\n FitTech Solutions"
        )

    def SelectValidateAccess(self):
        access_window = tk.Toplevel(self.window)
        access_window.title("Validar Acesso")
        access_window.geometry("400x200")

        tk.Label(access_window, text="CPF:", anchor="w").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        entry_cpf = tk.Entry(access_window, width=30)
        entry_cpf.grid(row=0, column=1, padx=10, pady=10)

        def validate_access():
            cpf = entry_cpf.get()
            if not cpf:
                return
            client = self.database_manager.SearchClient(cpf)
            if client:
                messagebox.showinfo("Acesso Permitido", f"Acesso permitido para o cliente {client['name']}.")
            else:
                messagebox.showerror("Acesso Negado", "CPF não encontrado.")
            access_window.destroy()

        tk.Button(access_window, text="Validar", command=validate_access).grid(row=1, column=1, pady=10)


    def SelectRegisterClient(self):
        register_window = tk.Toplevel(self.window)
        register_window.title("Registrar Cliente")
        register_window.geometry("600x400")

        tk.Label(register_window, text="Nome Completo *").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        entry_name = tk.Entry(register_window, width=40)
        entry_name.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(register_window, text="CPF *").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        entry_cpf = tk.Entry(register_window, width=40)
        entry_cpf.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(register_window, text="Data de Nascimento *").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        entry_birth_date = tk.Entry(register_window, width=40)
        entry_birth_date.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(register_window, text="E-mail *").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        entry_email = tk.Entry(register_window, width=40)
        entry_email.grid(row=3, column=1, padx=10, pady=10)

        tk.Button(register_window, text="Salvar", command=lambda: [
            self.register_client.SetClientInfo(
                entry_cpf.get(),
                {
                    "name": entry_name.get(),
                    "birth_date": entry_birth_date.get(),
                    "email": entry_email.get()
                }
            ),
            messagebox.showinfo("Sucesso", "Cliente registrado com sucesso."),
            register_window.destroy()
        ]).grid(row=4, column=1, padx=10, pady=20)


    def SelectSendWorkout(self):
        send_window = tk.Toplevel(self.window)
        send_window.title("Enviar Treino")
        send_window.geometry("400x200")  

        tk.Label(send_window, text="CPF:", anchor="w").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        entry_cpf = tk.Entry(send_window, width=30)
        entry_cpf.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(send_window, text="Treino:", anchor="w").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        entry_workout = tk.Entry(send_window, width=30)
        entry_workout.grid(row=1, column=1, padx=10, pady=10)

        def submit_workout():
            cpf = entry_cpf.get()
            workout = entry_workout.get()
            if not cpf or not workout:
                messagebox.showerror("Erro", "CPF e Treino são obrigatórios.")
                return
            try:
                self.send_workout.SendWorkout(cpf, workout)
                messagebox.showinfo("Sucesso", "Treino enviado com sucesso.")
                send_window.destroy()
            except ValueError as e:
                messagebox.showerror("Erro", str(e))

        tk.Button(send_window, text="Enviar", command=submit_workout).grid(row=2, column=1, pady=10)


    def SelectFindClient(self):
        find_window = tk.Toplevel(self.window)
        find_window.title("Procurar Cliente")
        find_window.geometry("400x200")

        tk.Label(find_window, text="CPF:", anchor="w").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        entry_cpf = tk.Entry(find_window, width=30)
        entry_cpf.grid(row=0, column=1, padx=10, pady=10)

        def find_client():
            cpf = entry_cpf.get()
            if not cpf:
                return
            client = self.database_manager.SearchClient(cpf)
            if client:
                workout = client.get("workout", "Nenhum treino atribuído.")
                messagebox.showinfo(
                    "Cliente Encontrado",
                    f"Nome: {client['name']}\n"
                    f"Data de Nascimento: {client.get('birth_date', 'Não informado')}\n"
                )
            else:
                messagebox.showerror("Erro", "Cliente não encontrado.")
            find_window.destroy()

        tk.Button(find_window, text="Procurar", command=find_client).grid(row=1, column=1, pady=10)



    def SelectCheckWorkout(self):
        check_window = tk.Toplevel(self.window)
        check_window.title("Checar Treino")
        check_window.geometry("400x200")

        tk.Label(check_window, text="CPF:", anchor="w").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        entry_cpf = tk.Entry(check_window, width=30)
        entry_cpf.grid(row=0, column=1, padx=10, pady=10)

        def check_workout():
            cpf = entry_cpf.get()
            if not cpf:
                return
            workout = self.database_manager.SearchWorkout(cpf)
            if workout:
                messagebox.showinfo("Treino", f"Treino: {workout}")
            else:
                messagebox.showwarning("Aviso", "Nenhum treino atribuído para este cliente.")
            check_window.destroy()

        tk.Button(check_window, text="Checar", command=check_workout).grid(row=1, column=1, pady=10)

    

if __name__ == "__main__":
    Interface()
