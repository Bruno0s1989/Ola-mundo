import tkinter as tk

class CalculadoraChurrasco:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Churrasco")
        self.root.geometry("300x200")

        self.label_pessoas = tk.Label(self.root, text="Número de pessoas:", font=("Arial", 14))
        self.label_pessoas.pack(pady=10)
        
        self.entry_pessoas = tk.Entry(self.root, font=("Arial", 14))
        self.entry_pessoas.pack(pady=5)
        
        self.button_calcular = tk.Button(self.root, text="Calcular", font=("Arial", 14), command=self.calcular_carne)
        self.button_calcular.pack(pady=10)
        
        self.result_var = tk.StringVar()
        self.label_resultado = tk.Label(self.root, textvariable=self.result_var, font=("Arial", 14))
        self.label_resultado.pack(pady=10)

    def calcular_carne(self):
        try:
            num_pessoas = int(self.entry_pessoas.get())
            quantidade_carne = num_pessoas * 400  # 400 gramas por pessoa
            self.result_var.set(f"Quantidade de carne: {quantidade_carne} gramas")
        except ValueError:
            self.result_var.set("Por favor, insira um número válido.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraChurrasco(root)
    root.mainloop()
