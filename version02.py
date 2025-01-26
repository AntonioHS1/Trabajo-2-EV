import tkinter as tk
from tkinter import simpledialog
import matplotlib.pyplot as plt
import numpy as np

# Cambiar a 'ggplot' para evitar dependencias externas
plt.style.use('ggplot')  
plt.rcParams.update({
    'axes.titlesize': 16,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial'],
    'lines.linewidth': 2,
    'lines.markersize': 8,
})

def center_window(window, width, height):
    """Centers a window on the screen."""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

def custom_simpledialog_float(title, prompt, parent=None):
    """Custom dialog to focus on the input field automatically."""
    result = None
    def on_ok(event=None):
        nonlocal result
        result = float(entry.get()) if entry.get().strip() else None
        dialog.destroy()

    dialog = tk.Toplevel(parent)
    dialog.title(title)
    center_window(dialog, 300, 150)

    tk.Label(dialog, text=prompt).pack(pady=10)
    entry = tk.Entry(dialog)
    entry.pack(pady=10)
    entry.focus_force()

    button_ok = tk.Button(dialog, text="OK", command=on_ok)
    button_ok.pack(pady=5)

    dialog.bind("<Return>", on_ok)

    parent.wait_window(dialog)
    return result

def custom_simpledialog_integer(title, prompt, parent=None):
    """Custom dialog to focus on the input field automatically."""
    result = None
    def on_ok(event=None):
        nonlocal result
        result = int(entry.get()) if entry.get().strip() else None
        dialog.destroy()

    dialog = tk.Toplevel(parent)
    dialog.title(title)
    center_window(dialog, 300, 150)

    tk.Label(dialog, text=prompt).pack(pady=10)
    entry = tk.Entry(dialog)
    entry.pack(pady=10)
    entry.focus_force()

    button_ok = tk.Button(dialog, text="OK", command=on_ok)
    button_ok.pack(pady=5)

    dialog.bind("<Return>", on_ok)

    parent.wait_window(dialog)
    return result

def graficar_ingresos_gastos():
    meses = []
    ingresos = []
    gastos = []

    num_meses = custom_simpledialog_integer("Meses", "¿Cuántos meses desea ingresar?", parent=ventana)
    if num_meses is None or num_meses <= 0:
        return

    nombres_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    for i in range(num_meses):
        mes = nombres_meses[i % 12]  # Usa nombres de meses cíclicamente si num_meses > 12
        ingreso = custom_simpledialog_float("Ingreso", f"Ingrese el ingreso para {mes} (€):", parent=ventana)
        gasto = custom_simpledialog_float("Gasto", f"Ingrese el gasto para {mes} (€):", parent=ventana)

        if ingreso is not None and gasto is not None:
            meses.append(mes)
            ingresos.append(ingreso)
            gastos.append(gasto)

    # Calcular beneficios totales
    ingresos_totales = sum(ingresos)
    gastos_totales = sum(gastos)
    beneficios_totales = ingresos_totales - gastos_totales

    # Graficar ingresos y gastos
    x = np.arange(len(meses))

    plt.figure(figsize=(12, 7))
    plt.plot(x, ingresos, marker='o', color='green', label='Ingresos')
    plt.plot(x, gastos, marker='o', color='red', label='Gastos')

    plt.xticks(x, meses, rotation=45, ha='right')
    plt.xlabel("Meses")
    plt.ylabel("Cantidad (€)")
    plt.title("Ingresos y Gastos por Mes", fontsize=18, weight='bold')
    plt.legend(fontsize=12)

    # Mostrar beneficios totales en la parte baja de la gráfica
    plt.text(-0.5, -max(ingresos + gastos) * 0.1,  # Coordenadas del texto
             f"Beneficios totales: ${beneficios_totales:.2f}", 
             fontsize=12, color='blue', weight='bold')

    # Personalizar ejes
    plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
    plt.tight_layout()

    plt.show()


ventana = tk.Tk()
ventana.title("Calculadora de Beneficios")
center_window(ventana, 960, 540)

controles = tk.Frame(ventana)
controles.pack(pady=20)

boton_grafico_ingresos_gastos = tk.Button(controles, text="Gráfica ingresos/gastos", command=graficar_ingresos_gastos)
boton_grafico_ingresos_gastos.grid(row=0, columnspan=2, pady=10)

ventana.mainloop()

