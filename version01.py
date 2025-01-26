import tkinter as tk

def boton_presionado():
    print("El botón fue presionado")

ventana = tk.Tk()
ventana.title("Calculadora de Beneficios")

controles = tk.Frame(ventana)
controles.pack(pady=20)

tk.Label(controles, text="Ingreso Total del Mes ($):").grid(row=0, column=0, padx=10, pady=5)
ingreso = tk.Entry(controles)
ingreso.grid(row=0, column=1, padx=10, pady=5)

tk.Label(controles, text="Gasto Total del Mes ($):").grid(row=1, column=0, padx=10, pady=5)
gasto = tk.Entry(controles)
gasto.grid(row=1, column=1, padx=10, pady=5)

boton_grafico_beneficios = tk.Button(controles, text="Gráfico Beneficios", command=boton_presionado)
boton_grafico_beneficios.grid(row=2, columnspan=2, pady=10)

ventana.mainloop()
