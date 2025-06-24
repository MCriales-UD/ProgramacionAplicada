import tkinter as tk

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("480x600")  # Aumentado tamaño de ventana
        self.root.resizable(False, False)

        self.expresion = ""

        self.entrada = tk.Entry(root, font=('Arial', 24), borderwidth=2, relief="ridge", justify='right')
        self.entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=15)  # Mayor altura

        botones = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'C', '+',
            '='
        ]

        fila = 1
        columna = 0
        for boton in botones:
            if boton == '=':
                btn = tk.Button(root, text=boton, width=10, height=1, font=('Arial', 14), command=self.calcular)
                btn.grid(row=fila, column=0, columnspan=4, padx=10, pady=5)
            else:
                btn = tk.Button(root, text=boton, width=8, height=3, font=('Arial', 14),
                                command=lambda b=boton: self.click(b))
                btn.grid(row=fila, column=columna, padx=5, pady=5)
                columna += 1
                if columna > 3:
                    columna = 0
                    fila += 1

    def click(self, boton):
        if boton == 'C':
            self.expresion = ""
            self.actualizar_pantalla()
        else:
            self.expresion += boton
            self.actualizar_pantalla()

    def actualizar_pantalla(self):
        self.entrada.delete(0, tk.END)
        self.entrada.insert(0, self.expresion)

    def calcular(self):
        try:
            resultado = eval(self.expresion)
            if resultado == int(resultado):
                resultado = int(resultado)
            self.expresion = str(resultado)
            self.actualizar_pantalla()
        except Exception:
            self.expresion = ""
            self.actualizar_pantalla()
            self.entrada.insert(0, "Error")

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculadora(root)
    root.mainloop()

