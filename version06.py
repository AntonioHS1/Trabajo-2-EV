import tkinter as tk
from tkinter import simpledialog, messagebox
import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image
import pickle 

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
    """Centra una ventana en la pantalla."""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

def custom_simpledialog_string(title, prompt, parent=None):
    """Cuadro de diálogo personalizado para obtener una cadena de texto."""
    result = None
    def on_ok(event=None):
        nonlocal result
        result = entry.get().strip() if entry.get().strip() else None
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
    """Cuadro de diálogo personalizado para obtener un número entero."""
    result = None
    def on_ok(event=None):
        nonlocal result
        try:
            result = int(entry.get()) if entry.get().strip() else None
        except ValueError:
            result = None  # En caso de que no se ingrese un número válido
            messagebox.showerror("Error", "Revise los valores escritos. El teléfono debe ser un número entero.")
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

def custom_simpledialog_float(title, prompt, parent=None):
    """Cuadro de diálogo personalizado para obtener un número flotante."""
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

def graficar_ingresos_gastos():
    # Pedir los datos personales
    nombre_completo = custom_simpledialog_string("Nombre completo", "Ingrese su nombre completo:", parent=ventana)
    telefono = None
    while telefono is None:
        telefono = custom_simpledialog_integer("Teléfono de contacto", "Ingrese su teléfono de contacto (solo números):", parent=ventana)

    dni = custom_simpledialog_string("DNI", "Ingrese su DNI:", parent=ventana)

    if not (nombre_completo and telefono and dni):
        return  # Si falta algún dato, salir

    # Mostrar los datos ingresados 
    print(f"Nombre completo: {nombre_completo}")
    print(f"Teléfono: {telefono}")
    print(f"DNI: {dni}")

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

    # Pedir nombre para la gráfica
    nombre_grafica = custom_simpledialog_string("Nombre de la Gráfica", "¿Qué nombre desea para la gráfica?", parent=ventana)
    if not nombre_grafica:
        nombre_grafica = "Ingresos y Gastos por Mes"  # Nombre por defecto si no se ingresa uno

    # Calcular beneficios totales
    ingresos_totales = sum(ingresos)
    gastos_totales = sum(gastos)
    beneficios_totales = ingresos_totales - gastos_totales

    # Grafica ingresos y gastos
    x = np.arange(len(meses))

    fig, ax = plt.subplots(figsize=(12, 7))
    ax.plot(x, ingresos, marker='o', color='green', label='Ingresos')
    ax.plot(x, gastos, marker='o', color='red', label='Gastos')

    ax.set_xticks(x)
    ax.set_xticklabels(meses, rotation=45, ha='right')
    ax.set_xlabel("Meses")
    ax.set_ylabel("Cantidad (€)")
    ax.set_title(nombre_grafica, fontsize=18, weight='bold') 
    ax.legend(fontsize=12)

    # Mostrar beneficios totales en la parte baja de la gráfica
    ax.text(-0.5, -max(ingresos + gastos) * 0.1,  # Coordenadas del texto
             f"Beneficios totales: ${beneficios_totales:.2f}", 
             fontsize=12, color='blue', weight='bold')

    # Personalizar ejes
    ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
    plt.tight_layout()

    # Guardar la gráfica en un archivo cuando se haga clic en el botón de guardar
    def guardar_grafica():
        nombre_archivo = f"{nombre_grafica}.png"
        fig.savefig(nombre_archivo)
        messagebox.showinfo("Guardado", f"Gráfica guardada como {nombre_archivo}")
        plt.close(fig)

        # Guardar los datos de la gráfica junto con la gráfica
        agregar_boton(nombre_grafica, nombre_completo, telefono, dni)

        boton_guardar.pack_forget()  # Eliminar el botón "Guardar gráfica" después de guardarla

    # Crear botón para guardar la gráfica
    global boton_guardar  # Hacer el botón global para poder ocultarlo después
    boton_guardar = tk.Button(ventana, text=f"Guardar gráfica {nombre_grafica}", command=guardar_grafica)
    boton_guardar.pack(pady=20)

    # Mostrar la gráfica
    plt.show()

def agregar_boton(nombre_grafica, nombre_completo, telefono, dni):
    """Agregar un botón para mostrar la gráfica guardada en la ventana principal."""
    # Verificar si el botón con el nombre de la gráfica ya existe
    for boton in botones_frame.winfo_children():
        if boton.cget("text") == nombre_grafica:
            return  # Si ya existe, no agregarlo de nuevo

    def mostrar_grafica():
        # Mostrar la imagen guardada
        if os.path.exists(f"{nombre_grafica}.png"):
            img = Image.open(f"{nombre_grafica}.png")
            img.show()
        else:
            messagebox.showerror("Error", "No se encontró la imagen guardada de la gráfica.")

    # Crear botón para la gráfica
    boton = tk.Button(botones_frame, text=nombre_grafica, command=mostrar_grafica)
    boton.pack(pady=5)

    # Crear botón para mostrar los datos asociados
    def mostrar_datos():
        messagebox.showinfo("Datos de la persona", 
                            f"Datos de la persona que ingresó {nombre_grafica}:\n\n"
                            f"Nombre completo: {nombre_completo}\nTeléfono de contacto: {telefono}\nDNI: {dni}")

    boton_datos = tk.Button(botones_frame, text="Ver Datos", command=mostrar_datos)
    boton_datos.pack(pady=5)

    # Guardar botones en un archivo
    try:
        with open("botones_guardados.pkl", "rb") as f:
            botones_guardados = pickle.load(f)
    except (FileNotFoundError, EOFError):
        botones_guardados = []

    # Guardar también la información de la gráfica
    try:
        with open("datos_graficas.pkl", "rb") as f:
            datos_graficas = pickle.load(f)
    except (FileNotFoundError, EOFError):
        datos_graficas = []

    # Guardar datos de la gráfica
    datos_graficas.append({"nombre": nombre_grafica, "nombre_completo": nombre_completo, 
                           "telefono": telefono, "dni": dni})

    with open("datos_graficas.pkl", "wb") as f:
        pickle.dump(datos_graficas, f)

    botones_guardados.append(nombre_grafica)

    with open("botones_guardados.pkl", "wb") as f:
        pickle.dump(botones_guardados, f)

def cargar_botones_guardados():
    """Cargar los botones guardados al iniciar el programa."""
    try:
        with open("botones_guardados.pkl", "rb") as f:
            botones_guardados = pickle.load(f)
    except (FileNotFoundError, EOFError):
        botones_guardados = []

    try:
        with open("datos_graficas.pkl", "rb") as f:
            datos_graficas = pickle.load(f)
    except (FileNotFoundError, EOFError):
        datos_graficas = []

    for i, nombre_grafica in enumerate(botones_guardados):
        agregar_boton(nombre_grafica, 
                      datos_graficas[i]["nombre_completo"], 
                      datos_graficas[i]["telefono"], 
                      datos_graficas[i]["dni"])

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Gráficas")

# Crear el frame para los botones de las gráficas
botones_frame = tk.Frame(ventana)
botones_frame.pack(padx=10, pady=10, anchor='w')

# Llamar a cargar los botones guardados al inicio
cargar_botones_guardados()

# Llamar a la función para graficar ingresos/gastos
boton_grafica_ingresos_gastos = tk.Button(ventana, text="Gráficas Ingresos/Gastos", command=graficar_ingresos_gastos)
boton_grafica_ingresos_gastos.pack(pady=20)

# Eliminar botones 
def eliminar_botones_guardados():
    try:
        with open("botones_guardados.pkl", "wb") as f:
            pickle.dump([], f)  # Guardar lista vacía para eliminar los botones
    except Exception as e:
        print(f"Error al eliminar botones guardados: {e}")
    
    for boton in botones_frame.winfo_children():
        boton.destroy()  # Eliminar botones

# Crear el botón de eliminar
boton_eliminar = tk.Button(ventana, text="Eliminar Botones", command=eliminar_botones_guardados)
boton_eliminar.pack(pady=20)

# Mostrar la ventana
ventana.mainloop()
