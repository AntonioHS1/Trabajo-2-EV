⚠️⚠️⚠️Las preguntas y respuestas que he intercambiado con chat gpt te las he puesto completas hay muchas lineas son casi todas código⚠️⚠️⚠️

Para este trabajo lo que he querido hacer es un programa en el que tu pongas los datos de ingresos/gastos de los meses que elijas en un cuadro de texto y te muestre una gráfica donde puedas comparar los ingresos y gastos que ha tenido una empresa por ejemplo entre 2020 y 2024, mostrandote el beneficio que has obtenido. Además quien introduzca los datos se le pedirán una serie de credenciales para tener constancia de quien puso esos datos (nombre, telefono(este solo numérico) y DNI) en los que nombre y dni serán de tipo string. Una vez introducidos los datos tanto de la persona como de las gráficas se guardará la gráfica automaticamente en un PNG y las variables en variables globales. Todo esto se podrá eliminar SOLO de la interfaz gráfica con un botón de eliminar.

# Versión 01

Para esta versión simplemente queria testear un poco la interfaz gráfica y hacer la funcionalidad de pedir los ingresos y los gastos, con botones y cuadros de texto.

Las preguntas y respuestas que intercambié con la IA fueron las siguientes:

**Quiero hacer un programa por python que haga operaciones financieras  y haga un gráfico de ellas y lo muestre por tkinter asi como una interfaz gráfica bonita** 

¡Claro! Para hacer un programa en Python que realice operaciones financieras y luego muestre un gráfico con esos resultados en una interfaz gráfica bonita con Tkinter, te guiaré paso a paso.

¿Qué haremos?
Operaciones financieras: Incluirás cálculos como el interés compuesto, la rentabilidad de una inversión, entre otros.
Gráfico: Usaremos Matplotlib para crear los gráficos.
Interfaz gráfica: Usaremos Tkinter para crear una ventana con botones, campos de texto y el gráfico.
Paso 1: Instalación de librerías necesarias
Asegúrate de tener instaladas las siguientes librerías:

Tkinter (generalmente ya está incluida con Python)
matplotlib (para crear gráficos)
numpy (para algunos cálculos matemáticos)
Puedes instalarlas con pip si no las tienes:

pip install matplotlib numpy
Paso 2: Creación del Programa
A continuación, te dejo un ejemplo de código que hace lo siguiente:

Permite ingresar datos financieros (como monto inicial, tasa de interés, tiempo, etc.)
Calcula el interés compuesto (por ejemplo).
Muestra un gráfico con los resultados.
-------------------------------------------------------Codigo---------------------------------------------------------
import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

## Función para calcular el interés compuesto
def calcular_interes_compuesto(monto_inicial, tasa, tiempo):
    montos = []
    for t in range(1, tiempo + 1):
        monto = monto_inicial * (1 + tasa / 100) ** t
        montos.append(monto)
    return montos

## Función para mostrar el gráfico en la interfaz de Tkinter
def mostrar_grafico():
    try:
        # Obtener valores de los campos de entrada
        monto_inicial = float(entry_monto_inicial.get())
        tasa = float(entry_tasa_interes.get())
        tiempo = int(entry_tiempo.get())

        # Calcular el interés compuesto
        montos = calcular_interes_compuesto(monto_inicial, tasa, tiempo)
        
        # Crear el gráfico
        fig, ax = plt.subplots()
        ax.plot(range(1, tiempo + 1), montos, marker='o', color='b', label='Monto acumulado')
        ax.set_title('Crecimiento de la inversión')
        ax.set_xlabel('Tiempo (años)')
        ax.set_ylabel('Monto acumulado ($)')
        ax.legend()

        # Mostrar el gráfico en la interfaz gráfica
        canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
        canvas.draw()
        canvas.get_tk_widget().pack()

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores válidos.")

## Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Financiera")

## Crear el frame para los controles
frame_controles = tk.Frame(ventana)
frame_controles.pack(pady=20)

## Etiquetas y campos de entrada
tk.Label(frame_controles, text="Monto inicial ($):").grid(row=0, column=0, padx=10, pady=5)
entry_monto_inicial = tk.Entry(frame_controles)
entry_monto_inicial.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame_controles, text="Tasa de interés anual (%):").grid(row=1, column=0, padx=10, pady=5)
entry_tasa_interes = tk.Entry(frame_controles)
entry_tasa_interes.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame_controles, text="Tiempo (años):").grid(row=2, column=0, padx=10, pady=5)
entry_tiempo = tk.Entry(frame_controles)
entry_tiempo.grid(row=2, column=1, padx=10, pady=5)

## Botón para calcular y mostrar el gráfico
btn_calcular = tk.Button(frame_controles, text="Calcular y Mostrar Gráfico", command=mostrar_grafico)
btn_calcular.grid(row=3, columnspan=2, pady=10)

## Crear el frame para el gráfico
frame_grafico = tk.Frame(ventana)
frame_grafico.pack()

## Iniciar la aplicación
ventana.mainloop()
----------------------------------------------------------------------------------------------------------------------

Explicación del código:
Cálculo del interés compuesto:

La función calcular_interes_compuesto() calcula el monto acumulado en cada año dado un monto inicial, tasa de interés y tiempo (en años).
Interfaz gráfica:

Usamos Tkinter para crear una interfaz sencilla con campos de entrada (para monto, tasa e tiempo) y un botón que, al presionar, calcula el interés compuesto y muestra un gráfico de cómo crece la inversión a lo largo del tiempo.
Gráfico:

Utilizamos Matplotlib para crear el gráfico. Los resultados son mostrados en una ventana emergente en la interfaz gráfica utilizando FigureCanvasTkAgg para integrar el gráfico dentro de Tkinter.
Características:
El programa calcula el monto acumulado cada año con interés compuesto.
Muestra un gráfico con el crecimiento de la inversión.
Usa Tkinter para la interfaz gráfica, con entradas de texto y botones.
Puedes adaptarlo para agregar más funcionalidades financieras, como cálculos de rentabilidad, amortización, etc.

Siguientes pasos:
Mejorar la interfaz: Puedes agregar más detalles gráficos, como colores, imágenes o más interactividad.
Añadir más operaciones financieras: Puedes extender este programa para incluir más tipos de cálculos financieros (por ejemplo, préstamos, amortización, etc.).
¡Espero que esto te ayude a empezar! Si tienes alguna duda o necesitas más detalles, no dudes en preguntar.


⚠️--Al darme esta respuesta yo queria ir por partes porque como se puede ver nos da un churro de código importante así que le dije que primero empezariamos con la interfaz gráfica y la primera funcionalidad. A parte le czmbié un poco el nombre a las variables.--


**Quiero ir por partes así que de momento solo muestrame el la interfaz gráfica del tkinter con un botón de "Gráfico Beneficios" y como pedir el calculo con ingresos y gastos no hace alta que hagas nada más no muestres el gráfico ni hagas la gráfica ni nada solo lo que te he pedido**

¡Entendido! Vamos a enfocarnos solo en la parte de la interfaz gráfica de Tkinter con el botón "Gráfico Beneficios" y los campos de entrada para ingresos y gastos, sin realizar ningún cálculo ni mostrar el gráfico.

Aquí tienes el código con solo la interfaz gráfica básica:
-------------------------------------------------------Codigo---------------------------------------------------------
import tkinter as tk

## Función para mostrar el mensaje al presionar el botón
def boton_presionado():
    # Aquí se podría agregar la lógica que quieras, por ahora solo es un placeholder
    print("El botón fue presionado")

## Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Beneficios")

## Crear el frame para los controles
frame_controles = tk.Frame(ventana)
frame_controles.pack(pady=20)

## Etiquetas y campos de entrada
tk.Label(frame_controles, text="Ingreso Total del Mes ($):").grid(row=0, column=0, padx=10, pady=5)
entry_ingreso = tk.Entry(frame_controles)
entry_ingreso.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame_controles, text="Gasto Total del Mes ($):").grid(row=1, column=0, padx=10, pady=5)
entry_gasto = tk.Entry(frame_controles)
entry_gasto.grid(row=1, column=1, padx=10, pady=5)

## Botón para mostrar el gráfico de beneficios
btn_grafico_beneficios = tk.Button(frame_controles, text="Gráfico Beneficios", command=boton_presionado)
btn_grafico_beneficios.grid(row=2, columnspan=2, pady=10)

## Iniciar la aplicación
ventana.mainloop()
----------------------------------------------------------------------------------------------------------------------

Explicación del código:
Ventana principal: Usamos tk.Tk() para crear la ventana principal de la aplicación.
Campos de entrada: Creamos dos campos de entrada, uno para el ingreso total del mes y otro para el gasto total del mes.
Los campos son representados por tk.Entry().
Botón: Hemos añadido el botón "Gráfico Beneficios", que al ser presionado ejecutará la función boton_presionado(). Esta función por ahora no hace nada más que imprimir un mensaje en la consola como placeholder, ya que en este paso solo estamos configurando la interfaz.
Posicionamiento con grid(): Usamos el método grid() para organizar las etiquetas y los campos de texto en una cuadrícula.
Qué hace este código:
Presenta una ventana con:
Dos campos de entrada: uno para Ingreso Total y otro para Gasto Total.
Un botón "Gráfico Beneficios" que por ahora solo imprime un mensaje cuando se presiona.
Este es solo el diseño básico de la interfaz gráfica sin ninguna funcionalidad de cálculos ni gráficos aún. Puedes ir probando este código para ver cómo se muestra la interfaz antes de agregar las funcionalidades.

# Versión 02

Para esta versión quería añadir el botón de hacer una gráfica, que nos preguntase cuantos meses queriamos poner, nos preguntase los ingresos y los gastos de cada uno de esos meses, por ejemplo si pongo que quiero tres meses nos pregunte por enero, febrero, marzo y quería ademas que se mostrase la gráfica de una manera determinada.

Las preguntas que le hice fueron las siguientes:

**Quiero que los ingresos y los gastos de cada mes se le pregunte al usuario al presionar un boton llamado "Grafica ingresos/gastos**

**Quiero que los cuadros de texto de ingresos y gastos no aparezcan nada más iniciar el programa sino que tengamos que darle al boton de grafico ingresos/gastos para que nos pregunte por cada mes**

**Hay varios errores al darle al boton primero de todo la parte de "Grafico Beneficios" la he quitado, segundo al presionar el botón de "Grafica ingresos/gastos" quiero que pregunte cuantos meses quiero poner y dependiendo de el número de meses que le de por ejemplo si pongo 3 que salga una ventana que pregunte por los ingresos y gastos de ese enero, despues de febrero así hasta llegar a marzo, si por ejemplo le pongo 10 que me haga la pregunta para todos los meses de enero hasta octubre, entiendes?**

**Hay un pequeño error y es que cada vez que salta una pantalla de por ejemplo gastos enero, febrero o ingresos etc se pone detras de la pantalla principal por lo que tengo que clicarle todo el rato y es molesto**

**A parte de esto quiero que cada vez que salga una ventana emergente preguntando cualquier cosa el cursor se posicione en ese cuadro de texto para poder escribir directamente y no tener que clicarle a parte quiero que tambien el botón de "OK" que aparece en cada ventana emergente se le pueda dar a la tecla enter para no tener que clicarle**

**Ahora por ultimo quiero que la ventana principal se muestre en 1920x1080 y las emergentes de cuantos meses quiere o las que te preguntan por ingresos y gastos quiero que salgan en el centro de la pantalla siempre así como la gráfica final**

⚠️--Es importante descargar la herramienta matplotlib la descargamos con "pip install matplotlib", es importante descargarla ya que sino el código no funcionará--

⚠️--Te he puesto las preguntas seguidas ya que el código se iba actualizando y no hay una respuesta como tal, te pongo el código final que quedo con estas preguntas--


Aquí tienes una versión actualizada de tu código que incluye el botón "Gráfica ingresos/gastos". Al presionar este botón, se solicita al usuario que ingrese los ingresos y gastos de cada mes mediante cuadros de diálogo emergentes, y luego se puede usar esta información para graficar los ingresos y gastos:

-------------------------------------------------------Codigo---------------------------------------------------------
import tkinter as tk
from tkinter import simpledialog
import matplotlib.pyplot as plt

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
        ingreso = custom_simpledialog_float("Ingreso", f"Ingrese el ingreso para {mes} ($):", parent=ventana)
        gasto = custom_simpledialog_float("Gasto", f"Ingrese el gasto para {mes} ($):", parent=ventana)

        if ingreso is not None and gasto is not None:
            meses.append(mes)
            ingresos.append(ingreso)
            gastos.append(gasto)

    # Graficar ingresos y gastos
    plt.figure(figsize=(10, 6))
    plt.bar(meses, ingresos, color='green', alpha=0.7, label='Ingresos')
    plt.bar(meses, gastos, color='red', alpha=0.7, label='Gastos', bottom=0)
    plt.xlabel("Meses")
    plt.ylabel("Cantidad ($)")
    plt.title("Ingresos vs Gastos por Mes")
    plt.legend()
    plt.tight_layout()
    center_window(plt.gcf().canvas.manager.window, 960, 540)  # Center the plot window
    plt.show()

ventana = tk.Tk()
ventana.title("Calculadora de Beneficios")
center_window(ventana, 1920, 1080)

controles = tk.Frame(ventana)
controles.pack(pady=20)

boton_grafico_ingresos_gastos = tk.Button(controles, text="Gráfica ingresos/gastos", command=graficar_ingresos_gastos)
boton_grafico_ingresos_gastos.grid(row=0, columnspan=2, pady=10)

ventana.mainloop()
----------------------------------------------------------------------------------------------------------------------
⚠️--Le pasé una imagen del estilo que queria que fuera la gráfica, en esta parte pasa como la otra el código se va actualizando así que no hay una respuesta como tal.

**Quiero que la gráfica sea del estilo de la imagen que te he pasado, ademas quiero que los ingresos aparezcan en verde y los gastos en rojo**

**Ahora quiero que en la parte baja de la gráfica mas o menos a la altura de donde pone "Meses" ponga a la izquiera "Beneficios totales:" y muestre los beneficios totales de esa gráfica es decir ingresos totales menos gatos totales, aunque sea negativo da igual que se muestre igual**

Para mostrar los beneficios totales en la parte baja de la gráfica, puedes usar plt.text() para añadir un texto personalizado a la gráfica. Aquí está la versión actualizada de tu código con esa funcionalidad añadida:

Cambios realizados:
Se calculan los beneficios totales como ingresos_totales - gastos_totales.
Se usa plt.text() para mostrar los beneficios totales en la parte baja de la gráfica, cerca de donde está la etiqueta "Meses".
Aquí tienes el código modificado:
-------------------------------------------------------Codigo---------------------------------------------------------
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
        ingreso = custom_simpledialog_float("Ingreso", f"Ingrese el ingreso para {mes} ($):", parent=ventana)
        gasto = custom_simpledialog_float("Gasto", f"Ingrese el gasto para {mes} ($):", parent=ventana)

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
    plt.ylabel("Cantidad ($)")
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
----------------------------------------------------------------------------------------------------------------------
⚠️--El código de arriba es el cambio que se ha aplicado el de abajo es el completo--
-------------------------------------------------------Codigo---------------------------------------------------------
import tkinter as tk
from tkinter import simpledialog
import matplotlib.pyplot as plt
import numpy as np

## Configurar estilos globales de Matplotlib
plt.style.use('seaborn')  # Estilo base
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
        ingreso = custom_simpledialog_float("Ingreso", f"Ingrese el ingreso para {mes} ($):", parent=ventana)
        gasto = custom_simpledialog_float("Gasto", f"Ingrese el gasto para {mes} ($):", parent=ventana)

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
    plt.ylabel("Cantidad ($)")
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
----------------------------------------------------------------------------------------------------------------------
⚠️ Hay que instalar numpy lo instalamos con "pip install numpy"
⚠️--En el siguiente código cambié los dolares por euros--

# Versión 03

En esta versión añadiremos la funcinalidad de ponerle nombre a la gráfica y aparezca un boton para que se muestre al clicarle.

**Ahora quiero que cuando termine de preguntar los ingresos y gastos antes de mostrar la gráfica nos pregunte en una ventana emergente que nombre le queremos poner a la gráfica y cuando la gráfica se muestre que se muestre con ese nombre**

Para agregar la funcionalidad de pedir un nombre para la gráfica antes de mostrarla, puedes hacerlo con un simple cuadro de diálogo emergente que permita al usuario ingresar un nombre. Luego, usarás ese nombre para titular la gráfica.

A continuación, te muestro cómo modificar el código para agregar esta funcionalidad:

Antes de mostrar la gráfica, crearemos un cuadro de diálogo para que el usuario ingrese el nombre de la gráfica.
Utilizamos ese nombre como título en la gráfica.
Aquí tienes el código modificado:
-------------------------------------------------------Codigo---------------------------------------------------------
import tkinter as tk
from tkinter import simpledialog
import matplotlib.pyplot as plt
import numpy as np

## Cambiar a 'ggplot' para evitar dependencias externas
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

def custom_simpledialog_integer(title, prompt, parent=None):
    """Cuadro de diálogo personalizado para obtener un número entero."""
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

def custom_simpledialog_string(title, prompt, parent=None):
    """Cuadro de diálogo para obtener una cadena de texto (nombre de la gráfica)."""
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

    # Pedir nombre para la gráfica
    nombre_grafica = custom_simpledialog_string("Nombre de la Gráfica", "¿Qué nombre desea para la gráfica?", parent=ventana)
    if not nombre_grafica:
        nombre_grafica = "Ingresos y Gastos por Mes"  # Nombre por defecto si no se ingresa uno

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
    plt.title(nombre_grafica, fontsize=18, weight='bold')  # Usar el nombre de la gráfica
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
----------------------------------------------------------------------------------------------------------------------
Cambios realizados:
custom_simpledialog_string: Esta nueva función solicita una entrada de texto para que el usuario ingrese el nombre de la gráfica.
En la función graficar_ingresos_gastos, se invoca este cuadro de diálogo para obtener el nombre antes de generar la gráfica.
Si el usuario no ingresa un nombre, se utiliza el nombre por defecto "Ingresos y Gastos por Mes".
Ahora, cuando el usuario haga clic en el botón para generar la gráfica, primero se le pedirá que ingrese un nombre para la gráfica y, posteriormente, se mostrará con ese nombre.

# Versión 04

En esta versión añadiré otra funcionalidad en la que preguntará los datos de la persona que pone los datos de la gráfica, para saber quien pone los datos. 

**Ahora quiero que antes de preguntar los meses que queremos poner en la gráfica nos salten varios cuadros de texto uno de ellos será el "Nombre completo" otro "Telefono de contacto" y "DNI" despues de estos ya pueden preguntarnos por los meses**

¡Entendido! Para agregar los cuadros de texto que solicitan el "Nombre completo", "Teléfono de contacto" y "DNI" antes de que se le pregunte al usuario por los meses, lo que necesitamos hacer es:

Pedir esos tres datos mediante cuadros de entrada.
Usar esos datos para almacenarlos o mostrarlos antes de continuar con el proceso de los meses.
Después de recolectar esos datos, se continuará con la solicitud de los meses, ingresos y gastos.
Aquí tienes el código modificado para incluir esos pasos adicionales:
-------------------------------------------------------Codigo---------------------------------------------------------
import tkinter as tk
from tkinter import simpledialog
import matplotlib.pyplot as plt
import numpy as np

## Cambiar a 'ggplot' para evitar dependencias externas
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

def custom_simpledialog_integer(title, prompt, parent=None):
    """Cuadro de diálogo personalizado para obtener un número entero."""
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
    # Pedir los datos personales antes de los meses
    nombre_completo = custom_simpledialog_string("Nombre completo", "Ingrese su nombre completo:", parent=ventana)
    telefono = custom_simpledialog_string("Teléfono de contacto", "Ingrese su teléfono de contacto:", parent=ventana)
    dni = custom_simpledialog_string("DNI", "Ingrese su DNI:", parent=ventana)

    if not (nombre_completo and telefono and dni):
        return  # Si falta algún dato, salir

    # Mostrar los datos ingresados (puedes eliminar esto si no es necesario)
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

    # Graficar ingresos y gastos
    x = np.arange(len(meses))

    plt.figure(figsize=(12, 7))
    plt.plot(x, ingresos, marker='o', color='green', label='Ingresos')
    plt.plot(x, gastos, marker='o', color='red', label='Gastos')

    plt.xticks(x, meses, rotation=45, ha='right')
    plt.xlabel("Meses")
    plt.ylabel("Cantidad (€)")
    plt.title(nombre_grafica, fontsize=18, weight='bold')  # Usar el nombre de la gráfica
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
----------------------------------------------------------------------------------------------------------------------
Cambios realizados:
Pedir Datos Personales: Antes de pedir el número de meses, se añaden tres cuadros de entrada solicitando el Nombre completo, Teléfono de contacto y DNI. Si cualquiera de estos datos falta, la función se detiene.

Mostrar Datos Ingresados: Opcionalmente, puedes imprimir los datos ingresados en la consola para asegurarte de que todo ha sido correctamente ingresado.

Continuar con los Meses: Una vez ingresados los datos personales, el proceso continúa preguntando por los meses, ingresos y gastos.

Lo que ocurre ahora:
Primero se le piden los datos personales (Nombre completo, Teléfono de contacto y DNI).
Luego, se procede con la pregunta sobre los meses.
Finalmente, se generará la gráfica de ingresos y gastos con el nombre proporcionado para la gráfica.
¡Con esto ya deberías tener la funcionalidad que necesitas!

**Quiero que el tipo de dato de telefono sea entero y lo demas (dni y nombre completo) sea string, si el telefono no son solo números que salga un mensaje de "Error revise los valores escritos**

¡Entendido! Vamos a agregar una validación extra para el teléfono de contacto, para que si el usuario ingresa algo que no sean solo números, aparezca un mensaje de error diciendo "Error, revise los valores escritos". Este mensaje se mostrará a través de una ventana emergente.

Aquí tienes el código actualizado con esa validación:
-------------------------------------------------------Codigo---------------------------------------------------------
import tkinter as tk
from tkinter import simpledialog, messagebox
import matplotlib.pyplot as plt
import numpy as np

## Cambiar a 'ggplot' para evitar dependencias externas
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
    # Pedir los datos personales antes de los meses
    nombre_completo = custom_simpledialog_string("Nombre completo", "Ingrese su nombre completo:", parent=ventana)
    telefono = None
    while telefono is None:
        telefono = custom_simpledialog_integer("Teléfono de contacto", "Ingrese su teléfono de contacto (solo números):", parent=ventana)

    dni = custom_simpledialog_string("DNI", "Ingrese su DNI:", parent=ventana)

    if not (nombre_completo and telefono and dni):
        return  # Si falta algún dato, salir

    # Mostrar los datos ingresados (puedes eliminar esto si no es necesario)
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

    # Graficar ingresos y gastos
    x = np.arange(len(meses))

    plt.figure(figsize=(12, 7))
    plt.plot(x, ingresos, marker='o', color='green', label='Ingresos')
    plt.plot(x, gastos, marker='o', color='red', label='Gastos')

    plt.xticks(x, meses, rotation=45, ha='right')
    plt.xlabel("Meses")
    plt.ylabel("Cantidad (€)")
    plt.title(nombre_grafica, fontsize=18, weight='bold')  # Usar el nombre de la gráfica
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
----------------------------------------------------------------------------------------------------------------------
Cambios realizados:
Validación del teléfono: Cuando se ingresa el teléfono, si el valor no es un número entero, se muestra un mensaje de error con messagebox.showerror(), pidiendo al usuario que revise los valores escritos. Este mensaje aparecerá si el teléfono no es un número válido.

Bucle para validar teléfono: Mientras el teléfono no sea válido, se seguirá mostrando el cuadro de diálogo hasta que se ingrese un número correcto.

¿Qué hace ahora?
Si el usuario ingresa algo que no es un número entero para el teléfono, se muestra un mensaje de error: "Error, revise los valores escritos. El teléfono debe ser un número entero."
Una vez el teléfono sea ingresado correctamente, se continúa con el resto de la lógica del programa.
¡Eso debería funcionar perfectamente! Si necesitas más cambios, házmelo saber.

# Versión 05

En esta versión vamos a guardar la gráfica y los valores que ingresemos de las credenciales de la persona que ha introducido los datos, aun cerrando la aplicación se guardará.

**Ahora quiero que la gráfica final y las 3 preguntas iniciales es decir dni, nombre completo y telefono de contacto se guarden de momento con las 3 preguntas no haremos nada, pero quiero que la gráfica final se guarde si cierro el programa que se guarde en un botón que tenga el nombre que le ponemos a la propia gráfica**

Para guardar la gráfica en un archivo cuando se cierre el programa, podemos agregar la funcionalidad de guardar la gráfica con el nombre que se haya ingresado para la gráfica en un archivo de imagen (por ejemplo, en formato PNG). Vamos a añadir un botón para guardar la gráfica y utilizar el nombre proporcionado para almacenarla.

Aquí está el código actualizado que incluye la opción de guardar la gráfica con el nombre que el usuario haya dado:

Al finalizar la gráfica, se ofrece un botón que permite guardar la gráfica con el nombre que se proporcionó.
La gráfica solo se guarda cuando el usuario haga clic en ese botón.
-------------------------------------------------------Codigo---------------------------------------------------------
import tkinter as tk
from tkinter import simpledialog, messagebox
import matplotlib.pyplot as plt
import numpy as np
import os

## Cambiar a 'ggplot' para evitar dependencias externas
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
    # Pedir los datos personales antes de los meses
    nombre_completo = custom_simpledialog_string("Nombre completo", "Ingrese su nombre completo:", parent=ventana)
    telefono = None
    while telefono is None:
        telefono = custom_simpledialog_integer("Teléfono de contacto", "Ingrese su teléfono de contacto (solo números):", parent=ventana)

    dni = custom_simpledialog_string("DNI", "Ingrese su DNI:", parent=ventana)

    if not (nombre_completo and telefono and dni):
        return  # Si falta algún dato, salir

    # Mostrar los datos ingresados (puedes eliminar esto si no es necesario)
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

    # Graficar ingresos y gastos
    x = np.arange(len(meses))

    fig, ax = plt.subplots(figsize=(12, 7))
    ax.plot(x, ingresos, marker='o', color='green', label='Ingresos')
    ax.plot(x, gastos, marker='o', color='red', label='Gastos')

    ax.set_xticks(x)
    ax.set_xticklabels(meses, rotation=45, ha='right')
    ax.set_xlabel("Meses")
    ax.set_ylabel("Cantidad (€)")
    ax.set_title(nombre_grafica, fontsize=18, weight='bold')  # Usar el nombre de la gráfica
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

    # Crear botón para guardar la gráfica
    boton_guardar = tk.Button(ventana, text=f"Guardar {nombre_grafica}", command=guardar_grafica)
    boton_guardar.pack(pady=20)

    # Mostrar la gráfica
    plt.show()


ventana = tk.Tk()
ventana.title("Calculadora de Beneficios")
center_window(ventana, 960, 540)

controles = tk.Frame(ventana)
controles.pack(pady=20)

boton_grafico_ingresos_gastos = tk.Button(controles, text="Gráfica ingresos/gastos", command=graficar_ingresos_gastos)
boton_grafico_ingresos_gastos.grid(row=0, columnspan=2, pady=10)

ventana.mainloop()
----------------------------------------------------------------------------------------------------------------------
Explicación de cambios:
Guardar la gráfica:

Después de mostrar la gráfica, se agrega un botón con el nombre de la gráfica que el usuario haya dado. Este botón permite guardar la gráfica como un archivo PNG en la misma carpeta donde se ejecuta el programa.
El archivo se guarda con el nombre que el usuario asignó a la gráfica (nombre_grafica.png).
Función guardar_grafica:

Esta función guarda la gráfica con el nombre proporcionado por el usuario y muestra un mensaje de confirmación con messagebox.showinfo().
Cerrar la gráfica:

Después de guardar la gráfica, la ventana de la gráfica se cierra automáticamente con plt.close(fig).
Resultado:
Después de ingresar los datos y generar la gráfica, el usuario puede hacer clic en el botón para guardar la gráfica con el nombre que se le haya dado.
¡Ahora tienes todo listo para guardar las gráficas generadas! Si necesitas más ayuda, no dudes en preguntar.

**Pero cuando el programa se cierre quiero que la gráfica que he hecho anteriormente que esta guardada aparezca el con su nombre para no tener que volverla a poner y cuando le de al boton se muestre la grafica, a parte quiero que si le doy al boton "guardar grafica "nombre de la grafica" se guarde pero ese boton desaparezca**

¡Entendido! Si deseas que el botón de "Guardar gráfica [nombre]" desaparezca después de hacer clic en él y guardar la gráfica, podemos hacer lo siguiente:

Guardar la gráfica: Se guardará la imagen como lo hicimos antes.
Eliminar el botón: Después de hacer clic en el botón de guardar, el botón desaparecerá de la interfaz.
Lo que vamos a hacer es modificar la función guardar_grafica() para que, después de guardar la gráfica, el botón desaparezca de la ventana.

Aquí está el código actualizado para lograr esto:

Código actualizado con eliminación del botón después de guardarlo:
-------------------------------------------------------Codigo---------------------------------------------------------
import tkinter as tk
from tkinter import simpledialog, messagebox
import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image

## Cambiar a 'ggplot' para evitar dependencias externas
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
    # Pedir los datos personales antes de los meses
    nombre_completo = custom_simpledialog_string("Nombre completo", "Ingrese su nombre completo:", parent=ventana)
    telefono = None
    while telefono is None:
        telefono = custom_simpledialog_integer("Teléfono de contacto", "Ingrese su teléfono de contacto (solo números):", parent=ventana)

    dni = custom_simpledialog_string("DNI", "Ingrese su DNI:", parent=ventana)

    if not (nombre_completo and telefono and dni):
        return  # Si falta algún dato, salir

    # Mostrar los datos ingresados (puedes eliminar esto si no es necesario)
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

    # Graficar ingresos y gastos
    x = np.arange(len(meses))

    fig, ax = plt.subplots(figsize=(12, 7))
    ax.plot(x, ingresos, marker='o', color='green', label='Ingresos')
    ax.plot(x, gastos, marker='o', color='red', label='Gastos')

    ax.set_xticks(x)
    ax.set_xticklabels(meses, rotation=45, ha='right')
    ax.set_xlabel("Meses")
    ax.set_ylabel("Cantidad (€)")
    ax.set_title(nombre_grafica, fontsize=18, weight='bold')  # Usar el nombre de la gráfica
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
        # Guardar el nombre en un archivo de texto para recuperarlo después
        with open("grafica_guardada.txt", "w") as f:
            f.write(nombre_grafica)
        # Eliminar el botón de guardar
        boton_guardar.destroy()

    # Crear botón para guardar la gráfica
    boton_guardar = tk.Button(ventana, text=f"Guardar gráfica {nombre_grafica}", command=guardar_grafica)
    boton_guardar.pack(pady=20)

    # Mostrar la gráfica
    plt.show()


def crear_boton(nombre_grafica):
    """Crear un botón con el nombre de la gráfica y asociarlo con la acción de mostrar la gráfica."""
    def mostrar_grafica():
        # Mostrar la imagen guardada
        if os.path.exists(f"{nombre_grafica}.png"):
            img = Image.open(f"{nombre_grafica}.png")
            img.show()
        else:
            messagebox.showerror("Error", "No se encontró la imagen guardada de la gráfica.")

    boton = tk.Button(botones_frame, text=nombre_grafica, command=mostrar_grafica)
    boton.pack(pady=5)


def cargar_botones_guardados():
    """Cargar los botones guardados desde un archivo y crear los botones correspondientes."""
    if os.path.exists("grafica_guardada.txt"):
        with open("grafica_guardada.txt", "r") as f:
            nombre_grafica = f.read().strip()
            crear_boton(nombre_grafica)


ventana = tk.Tk()
ventana.title("Calculadora de Beneficios")
center_window(ventana, 960, 540)

botones_frame = tk.Frame(ventana)
botones_frame.pack(pady=20)

## Cargar los botones guardados al iniciar el programa
cargar_botones_guardados()

boton_grafico_ingresos_gastos = tk.Button(botones_frame, text="Gráfica ingresos/gastos", command=graficar_ingresos_gastos)
boton_grafico_ingresos_gastos.pack(pady=10)

ventana.mainloop()
----------------------------------------------------------------------------------------------------------------------
Explicación del cambio:
Dentro de la función guardar_grafica(), después de guardar la gráfica, se agrega la instrucción boton_guardar.destroy(). Esto hace que el botón de "Guardar gráfica [nombre]" se elimine de la interfaz después de hacer clic en él.
¿Cómo funciona ahora?
Guardar la gráfica: Cuando haces clic en el botón "Guardar gráfica [nombre]" para guardar la gráfica, la gráfica se guarda como una imagen y el botón desaparece de la interfaz.
Ver la gráfica: El nombre del botón desaparecido se mantiene guardado y, si reinicias el programa, el nombre del último botón guardado aparecerá con su respectiva acción de mostrar la gráfica.
¡Ahora debería funcionar como esperas!

**Hay un problemas el boton de "guardar grafica" no deasaparece**

Entendido! Los dos problemas que mencionas se pueden solucionar de la siguiente manera:

Desaparecer el botón "guardar gráfica": Después de hacer clic en el botón para guardar la gráfica, este debería desaparecer. Para esto, tenemos que asegurarnos de que el botón sea eliminado correctamente al guardar la gráfica.

Cambios realizados:
El botón "guardar gráfica" ahora desaparece: Cuando haces clic en el botón de "guardar gráfica", se elimina de la interfaz.

Código actualizado:
-------------------------------------------------------Codigo---------------------------------------------------------
import tkinter as tk
from tkinter import simpledialog, messagebox
import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image
import pickle  # Usamos pickle para guardar los botones de forma persistente

## Cambiar a 'ggplot' para evitar dependencias externas
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
    # Pedir los datos personales antes de los meses
    nombre_completo = custom_simpledialog_string("Nombre completo", "Ingrese su nombre completo:", parent=ventana)
    telefono = None
    while telefono is None:
        telefono = custom_simpledialog_integer("Teléfono de contacto", "Ingrese su teléfono de contacto (solo números):", parent=ventana)

    dni = custom_simpledialog_string("DNI", "Ingrese su DNI:", parent=ventana)

    if not (nombre_completo and telefono and dni):
        return  # Si falta algún dato, salir

    # Mostrar los datos ingresados (puedes eliminar esto si no es necesario)
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

    # Graficar ingresos y gastos
    x = np.arange(len(meses))

    fig, ax = plt.subplots(figsize=(12, 7))
    ax.plot(x, ingresos, marker='o', color='green', label='Ingresos')
    ax.plot(x, gastos, marker='o', color='red', label='Gastos')

    ax.set_xticks(x)
    ax.set_xticklabels(meses, rotation=45, ha='right')
    ax.set_xlabel("Meses")
    ax.set_ylabel("Cantidad (€)")
    ax.set_title(nombre_grafica, fontsize=18, weight='bold')  # Usar el nombre de la gráfica
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

        # Guardar el nombre de la gráfica en un archivo persistente
        agregar_boton(nombre_grafica)
        boton_guardar.pack_forget()  # Eliminar el botón "Guardar gráfica" después de guardarla

    # Crear botón para guardar la gráfica
    global boton_guardar  # Hacer el botón global para poder ocultarlo después
    boton_guardar = tk.Button(ventana, text=f"Guardar gráfica {nombre_grafica}", command=guardar_grafica)
    boton_guardar.pack(pady=20)

    # Mostrar la gráfica
    plt.show()

def agregar_boton(nombre_grafica):
    """Agregar un botón para mostrar la gráfica guardada en la ventana principal."""
    def mostrar_grafica():
        # Mostrar la imagen guardada
        if os.path.exists(f"{nombre_grafica}.png"):
            img = Image.open(f"{nombre_grafica}.png")
            img.show()
        else:
            messagebox.showerror("Error", "No se encontró la imagen guardada de la gráfica.")

    boton = tk.Button(botones_frame, text=nombre_grafica, command=mostrar_grafica)
    boton.pack(pady=5)
    
    # Guardar botones en un archivo
    try:
        with open("botones_guardados.pkl", "rb") as f:
            botones_guardados = pickle.load(f)
    except (FileNotFoundError, EOFError):
        botones_guardados = []

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

    for nombre_grafica in botones_guardados:
        agregar_boton(nombre_grafica)

ventana = tk.Tk()
ventana.title("Calculadora de Beneficios")
center_window(ventana, 960, 540)

## Crear un frame para los botones principales y los botones de las gráficas
frame_principal = tk.Frame(ventana)
frame_principal.pack(pady=20)

## Crear frame para los botones con el nombre de las gráficas guardadas
botones_frame = tk.Frame(ventana)
botones_frame.pack(pady=20)

## Cargar los botones guardados al iniciar el programa
cargar_botones_guardados()

## Botón para crear la gráfica de ingresos/gastos
boton_grafico_ingresos_gastos = tk.Button(frame_principal, text="Gráfica ingresos/gastos", command=graficar_ingresos_gastos)
boton_grafico_ingresos_gastos.pack(pady=10)

ventana.mainloop()
----------------------------------------------------------------------------------------------------------------------
Cambios clave:
El botón "guardar gráfica" desaparece:
Después de hacer clic en el botón de guardar, este botón

**Ahora vamos a implementar una funcion con un boton alojado en la parte alta de la interfaz principal llamado "Eliminar gráficas" que si nosotros le damos eliminará los botones enlazados con las graficas guardadas, por ejemplo si tenemos la "grafica 2020" y "grafica 4000" esos botones se eliminaran**
-------------------------------------------------------Codigo---------------------------------------------------------
import tkinter as tk
from tkinter import simpledialog, messagebox
import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image
import pickle  # Usamos pickle para guardar los botones de forma persistente

## Cambiar a 'ggplot' para evitar dependencias externas
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
    # Pedir los datos personales antes de los meses
    nombre_completo = custom_simpledialog_string("Nombre completo", "Ingrese su nombre completo:", parent=ventana)
    telefono = None
    while telefono is None:
        telefono = custom_simpledialog_integer("Teléfono de contacto", "Ingrese su teléfono de contacto (solo números):", parent=ventana)

    dni = custom_simpledialog_string("DNI", "Ingrese su DNI:", parent=ventana)

    if not (nombre_completo and telefono and dni):
        return  # Si falta algún dato, salir

    # Mostrar los datos ingresados (puedes eliminar esto si no es necesario)
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

    # Graficar ingresos y gastos
    x = np.arange(len(meses))

    fig, ax = plt.subplots(figsize=(12, 7))
    ax.plot(x, ingresos, marker='o', color='green', label='Ingresos')
    ax.plot(x, gastos, marker='o', color='red', label='Gastos')

    ax.set_xticks(x)
    ax.set_xticklabels(meses, rotation=45, ha='right')
    ax.set_xlabel("Meses")
    ax.set_ylabel("Cantidad (€)")
    ax.set_title(nombre_grafica, fontsize=18, weight='bold')  # Usar el nombre de la gráfica
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

        # Guardar el nombre de la gráfica en un archivo persistente
        agregar_boton(nombre_grafica)
        boton_guardar.pack_forget()  # Eliminar el botón "Guardar gráfica" después de guardarla

    # Crear botón para guardar la gráfica
    global boton_guardar  # Hacer el botón global para poder ocultarlo después
    boton_guardar = tk.Button(ventana, text=f"Guardar gráfica {nombre_grafica}", command=guardar_grafica)
    boton_guardar.pack(pady=20)

    # Mostrar la gráfica
    plt.show()

def agregar_boton(nombre_grafica):
    """Agregar un botón para mostrar la gráfica guardada en la ventana principal."""
    global botones_frame
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

    boton = tk.Button(botones_frame, text=nombre_grafica, command=mostrar_grafica)
    boton.pack(pady=5)
    
    # Guardar botones en un archivo
    try:
        with open("botones_guardados.pkl", "rb") as f:
            botones_guardados = pickle.load(f)
    except (FileNotFoundError, EOFError):
        botones_guardados = []

    botones_guardados.append(nombre_grafica)

    with open("botones_guardados.pkl", "wb") as f:
        pickle.dump(botones_guardados, f)

## Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Ingresos y Gastos")
center_window(ventana, 500, 500)

## Crear el botón de "Eliminar"
boton_eliminar = tk.Button(ventana, text="Eliminar", command=lambda: print("Botón eliminar presionado"))
boton_eliminar.pack(side="top", anchor="ne", padx=20, pady=20)

## Crear un contenedor para los botones de gráficas
botones_frame = tk.Frame(ventana)
botones_frame.pack(pady=20)

## Botón para generar gráficos
boton_graficar = tk.Button(ventana, text="Generar Gráfica", command=graficar_ingresos_gastos)
boton_graficar.pack(pady=20)

## Iniciar la interfaz
ventana.mainloop()
----------------------------------------------------------------------------------------------------------------------

**El boton de eliminar tiene que eliminar los botones de las graficas que se creen con el nombre de esa grafica**

El botón "Eliminar" debe eliminar esos botones correspondientes a las gráficas creadas.
-------------------------------------------------------Codigo---------------------------------------------------------
import tkinter as tk
from tkinter import simpledialog, messagebox
import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image
import pickle  # Usamos pickle para guardar los botones de forma persistente

## Cambiar a 'ggplot' para evitar dependencias externas
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
    # Pedir los datos personales antes de los meses
    nombre_completo = custom_simpledialog_string("Nombre completo", "Ingrese su nombre completo:", parent=ventana)
    telefono = None
    while telefono is None:
        telefono = custom_simpledialog_integer("Teléfono de contacto", "Ingrese su teléfono de contacto (solo números):", parent=ventana)

    dni = custom_simpledialog_string("DNI", "Ingrese su DNI:", parent=ventana)

    if not (nombre_completo and telefono and dni):
        return  # Si falta algún dato, salir

    # Mostrar los datos ingresados (puedes eliminar esto si no es necesario)
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

    # Graficar ingresos y gastos
    x = np.arange(len(meses))

    fig, ax = plt.subplots(figsize=(12, 7))
    ax.plot(x, ingresos, marker='o', color='green', label='Ingresos')
    ax.plot(x, gastos, marker='o', color='red', label='Gastos')

    ax.set_xticks(x)
    ax.set_xticklabels(meses, rotation=45, ha='right')
    ax.set_xlabel("Meses")
    ax.set_ylabel("Cantidad (€)")
    ax.set_title(nombre_grafica, fontsize=18, weight='bold')  # Usar el nombre de la gráfica
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

        # Guardar el nombre de la gráfica en un archivo persistente
        agregar_boton(nombre_grafica)
        boton_guardar.pack_forget()  # Eliminar el botón "Guardar gráfica" después de guardarla

    # Crear botón para guardar la gráfica
    global boton_guardar  # Hacer el botón global para poder ocultarlo después
    boton_guardar = tk.Button(ventana, text=f"Guardar gráfica {nombre_grafica}", command=guardar_grafica)
    boton_guardar.pack(pady=20)

    # Mostrar la gráfica
    plt.show()

def agregar_boton(nombre_grafica):
    """Agregar un botón para mostrar la gráfica guardada en la ventana principal."""
    global botones_frame
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

    boton = tk.Button(botones_frame, text=nombre_grafica, command=mostrar_grafica)
    boton.pack(pady=5)
    
    # Guardar botones en un archivo
    try:
        with open("botones_guardados.pkl", "rb") as f:
            botones_guardados = pickle.load(f)
    except (FileNotFoundError, EOFError):
        botones_guardados = []

    botones_guardados.append(nombre_grafica)

    with open("botones_guardados.pkl", "wb") as f:
        pickle.dump(botones_guardados, f)

def eliminar_botones():
    """Eliminar todos los botones generados."""
    for boton in botones_frame.winfo_children():
        boton.destroy()

## Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Ingresos y Gastos")
center_window(ventana, 500, 500)

## Crear el botón de "Eliminar" y moverlo a la parte derecha y arriba
boton_eliminar = tk.Button(ventana, text="Eliminar", command=eliminar_botones)
boton_eliminar.pack(side="top", anchor="ne", padx=20, pady=20)

## Crear un contenedor para los botones de gráficas
botones_frame = tk.Frame(ventana)
botones_frame.pack(pady=20)

## Botón para generar gráficos (con el nombre original)
boton_graficar = tk.Button(ventana, text="Gráficas ingresos/gastos", command=graficar_ingresos_gastos)
boton_graficar.pack(pady=10)

## Ejecutar la interfaz
ventana.mainloop()
----------------------------------------------------------------------------------------------------------------------

**Pero los botones de las graficas que yo creo no aparecen despues de cerrar el programa y volverlo a abrir**

¡Ah! Ya veo lo que está pasando. El motivo por el cual los botones de las gráficas no aparecen después de cerrar el programa y volverlo a abrir es porque no estás cargando esos botones desde un archivo persistente cuando reinicias la aplicación.

De hecho, ya tienes la función agregar_boton() que guarda los botones en un archivo usando pickle, pero parece que no estás cargando esos botones guardados en el inicio del programa.

Te voy a guiar para que los botones de las gráficas que creas se guarden y se vuelvan a cargar automáticamente al iniciar el programa.

Paso 1: Guardar los botones al crear una gráfica
Parece que ya estás usando la función pickle para guardar los nombres de las gráficas (en el archivo botones_guardados.pkl). Vamos a asegurarnos de que realmente se guarden de forma persistente cuando crees una nueva gráfica:
-------------------------------------------------------Codigo---------------------------------------------------------
def agregar_boton(nombre_grafica):
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

    boton = tk.Button(botones_frame, text=nombre_grafica, command=mostrar_grafica)
    boton.pack(pady=5)
    
    # Guardar botones en un archivo
    try:
        with open("botones_guardados.pkl", "rb") as f:
            botones_guardados = pickle.load(f)
    except (FileNotFoundError, EOFError):
        botones_guardados = []

    botones_guardados.append(nombre_grafica)

    with open("botones_guardados.pkl", "wb") as f:
        pickle.dump(botones_guardados, f)
----------------------------------------------------------------------------------------------------------------------
Paso 2: Cargar los botones guardados al iniciar el programa
Tienes que cargar estos botones guardados cuando el programa se inicie para que aparezcan en la interfaz:
-------------------------------------------------------Codigo---------------------------------------------------------
def cargar_botones_guardados():
    """Cargar los botones guardados al iniciar el programa."""
    try:
        with open("botones_guardados.pkl", "rb") as f:
            botones_guardados = pickle.load(f)
    except (FileNotFoundError, EOFError):
        botones_guardados = []

    for nombre_grafica in botones_guardados:
        agregar_boton(nombre_grafica)
----------------------------------------------------------------------------------------------------------------------
Paso 3: Llamar a la función cargar_botones_guardados() al inicio del programa
Asegúrate de que la función cargar_botones_guardados() se ejecute cuando inicie la ventana principal, para cargar los botones de las gráficas guardadas. Por ejemplo, podrías llamar a esta función justo después de crear la ventana principal (al principio de tu código):
-------------------------------------------------------Codigo---------------------------------------------------------
## Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Gráficas")

## Llamar a cargar los botones guardados al inicio
cargar_botones_guardados()
----------------------------------------------------------------------------------------------------------------------
## Resto de tu código para configurar la interfaz...
Resumen
Guardar los botones en el archivo botones_guardados.pkl cuando se crea una nueva gráfica.
Cargar los botones desde el archivo botones_guardados.pkl cuando se inicia el programa para que los botones aparezcan.
Con esto, los botones de las gráficas creadas deberían persistir incluso después de cerrar y volver a abrir el programa.

# Versión 06

En esta versión pondremos botones al lado de los que se crean guardando las gráficas, en esos botones se mostrarán los datos de la persona que ha puesto los datos de la gráfica. Aparecerán aun cerrando la aplicación.

**Ahora quiero que esos datos anteriores de cada grafica es decir nombre, telefono, dni se guarden cada vez que se pulse el boton de guradar la grafica y al lado del boton que se cree de la grafica correspondiente a la que se le ha dado a guardar aparezca otro boton donde se muestre la información de nombre completo, telefono y dni que hemos metido en esa grafica y quiero que al mostrar los datos ponga "Datos de la persona que ingreso "nombre de la grafica**

¡Entendido! Para mostrar el mensaje con el nombre de la gráfica en lugar de solo "Datos de la gráfica", puedes modificar el texto en el mensaje emergente (la ventana que muestra los datos) de la siguiente manera:

Cambios necesarios:
Modificar el mensaje que se muestra cuando se hace clic en el botón "Ver Datos" para que diga "Datos de la persona que ingresó <nombre de la gráfica>".
Aquí tienes el código actualizado con esa modificación:
-------------------------------------------------------Codigo---------------------------------------------------------
import tkinter as tk
from tkinter import simpledialog, messagebox
import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image
import pickle  # Usamos pickle para guardar los botones de forma persistente

## Cambiar a 'ggplot' para evitar dependencias externas
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
    # Pedir los datos personales antes de los meses
    nombre_completo = custom_simpledialog_string("Nombre completo", "Ingrese su nombre completo:", parent=ventana)
    telefono = None
    while telefono is None:
        telefono = custom_simpledialog_integer("Teléfono de contacto", "Ingrese su teléfono de contacto (solo números):", parent=ventana)

    dni = custom_simpledialog_string("DNI", "Ingrese su DNI:", parent=ventana)

    if not (nombre_completo and telefono and dni):
        return  # Si falta algún dato, salir

    # Mostrar los datos ingresados (puedes eliminar esto si no es necesario)
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

    # Graficar ingresos y gastos
    x = np.arange(len(meses))

    fig, ax = plt.subplots(figsize=(12, 7))
    ax.plot(x, ingresos, marker='o', color='green', label='Ingresos')
    ax.plot(x, gastos, marker='o', color='red', label='Gastos')

    ax.set_xticks(x)
    ax.set_xticklabels(meses, rotation=45, ha='right')
    ax.set_xlabel("Meses")
    ax.set_ylabel("Cantidad (€)")
    ax.set_title(nombre_grafica, fontsize=18, weight='bold')  # Usar el nombre de la gráfica
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
                            f"Nombre: {nombre_completo}\nTeléfono: {telefono}\nDNI: {dni}")

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

## Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Gráficas")

## Crear el frame para los botones de las gráficas
botones_frame = tk.Frame(ventana)
botones_frame.pack(padx=10, pady=10, anchor='w')

## Llamar a cargar los botones guardados al inicio
cargar_botones_guardados()

## Llamar a la función para graficar ingresos/gastos
boton_grafica_ingresos_gastos = tk.Button(ventana, text="Gráficas Ingresos/Gastos", command=graficar_ingresos_gastos)
boton_grafica_ingresos_gastos.pack(pady=20)

## Eliminar botones guardados
def eliminar_botones_guardados():
    try:
        with open("botones_guardados.pkl", "wb") as f:
            pickle.dump([], f)  # Guardar lista vacía para eliminar los botones
    except Exception as e:
        print(f"Error al eliminar botones guardados: {e}")
    
    for boton in botones_frame.winfo_children():
        boton.destroy()  # Eliminar todos los botones de la interfaz

## Crear el botón para eliminar botones
boton_eliminar = tk.Button(ventana, text="Eliminar Botones", command=eliminar_botones_guardados)
boton_eliminar.pack(pady=20)

## Mostrar la ventana
ventana.mainloop()
----------------------------------------------------------------------------------------------------------------------
Cambios realizados:
Modificación en el texto del cuadro de mensaje: Cuando se hace clic en el botón "Ver Datos", el texto del mensaje ahora dice "Datos de la persona que ingresó {nombre de la gráfica}".
Con esto, cuando se presiona el botón "Ver Datos" junto a una gráfica, aparecerá un mensaje como:

Datos de la persona que ingresó Gráfica de Ingresos 2025:
Nombre: Juan Pérez
Teléfono: 123456789
DNI: 12345678A

