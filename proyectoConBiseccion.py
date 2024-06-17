import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from scipy.optimize import bisect


def calcular_tasa_interes_biseccion():
    try:
        # Obtención y validación de entradas
        deposito_inicial = float(entry_deposito_inicial.get())
        aportes = float(entry_aportes.get())
        valor_final = float(entry_valor_final.get())
        periodos = int(entry_periodos.get())
        frecuencia = combo_frecuencia.get()

        if deposito_inicial < 50 or aportes < 5:
            raise ValueError(
                "El depósito inicial debe ser al menos 50 y los aportes al menos 5.")

        # Determinación de la frecuencia en términos de periodos anuales
        if frecuencia == "Semanal":
            n = 52
        elif frecuencia == "Mensual":
            n = 12
        elif frecuencia == "Bimestral":
            n = 6
        elif frecuencia == "Trimestral":
            n = 4

        t = periodos

        # Definición de la ecuación para encontrar la tasa de interés
        def ecuacion(tasa):
            saldo = deposito_inicial
            for _ in range(t * n):
                saldo += aportes
                saldo *= (1 + tasa / n)
            return saldo - valor_final

        # Uso del método de la bisección para encontrar la raíz de la ecuación
        tasa_interes = bisect(ecuacion, 0, 1)

        if tasa_interes < 0:
            raise ValueError(
                "No es posible alcanzar el valor final con las condiciones dadas.")

        mostrar_resultado(tasa_interes * 100)

    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Función para mostrar el resultado


def mostrar_resultado(tasa_interes):
    try:
        # Obtención de entradas
        deposito_inicial = float(entry_deposito_inicial.get())
        aportes = float(entry_aportes.get())
        periodos = int(entry_periodos.get())
        frecuencia = combo_frecuencia.get()

        if frecuencia == "Semanal":
            n = 52
        elif frecuencia == "Mensual":
            n = 12
        elif frecuencia == "Bimestral":
            n = 6
        elif frecuencia == "Trimestral":
            n = 4

        saldo = deposito_inicial
        datos = []

        # Cálculo del interés compuesto y actualización del saldo
        for i in range(1, periodos * n + 1):
            interes = saldo * (tasa_interes / 100 / n)
            saldo += aportes + interes
            datos.append((i, aportes, saldo - interes, interes, saldo))

        # Creación de la figura para graficar
        fig = Figure(figsize=(10, 6), dpi=100)
        ax = fig.add_subplot(111)

        # Preparación de datos para graficar
        periodos = [dato[0] for dato in datos]
        totales = [dato[4] for dato in datos]

        ax.plot(periodos, totales, label='Total ($)')
        ax.set_xlabel('Periodo')
        ax.set_ylabel('Total ($)')
        ax.set_title(f'Evolución del ahorro con {
                     tasa_interes:.2f}% de interés')
        ax.legend()

        # Mostrar el gráfico en la interfaz
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack()

    except ValueError as e:
        messagebox.showerror("Error", str(e))


# Crear la ventana principal
window = tk.Tk()
window.title("Calculadora de Ahorros")

# Crear el frame principal
frame = tk.Frame(window)
frame.pack(pady=20)

# Etiquetas y campos de entrada
tk.Label(frame, text="Depósito inicial ($)").grid(row=0, column=0)
entry_deposito_inicial = tk.Entry(frame)
entry_deposito_inicial.grid(row=0, column=1)

tk.Label(frame, text="Aportes ($)").grid(row=1, column=0)
entry_aportes = tk.Entry(frame)
entry_aportes.grid(row=1, column=1)

tk.Label(frame, text="Valor final deseado ($)").grid(row=2, column=0)
entry_valor_final = tk.Entry(frame)
entry_valor_final.grid(row=2, column=1)

tk.Label(frame, text="Periodos (años)").grid(row=3, column=0)
entry_periodos = tk.Entry(frame)
entry_periodos.grid(row=3, column=1)

tk.Label(frame, text="Frecuencia de aportes").grid(row=4, column=0)
combo_frecuencia = tk.StringVar()
frecuencia_menu = tk.OptionMenu(
    frame, combo_frecuencia, "Semanal", "Mensual", "Bimestral", "Trimestral")
frecuencia_menu.grid(row=4, column=1)
combo_frecuencia.set("Semanal")

# Botón de cálculo
btn_calcular = tk.Button(frame, text="Calcular Tasa de Interés",
                         command=calcular_tasa_interes_biseccion)
btn_calcular.grid(row=5, columnspan=2, pady=10)

# Iniciar el bucle principal de la ventana
window.mainloop()
