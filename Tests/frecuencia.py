import math
import customtkinter as ctk
from customtkinter import CTkLabel, CTkFont

class _Frecuencia:

    @staticmethod
    def continuar(frame, estadistico_input, cant_intervalos_input,muestra):
        estadistico = estadistico_input.get()
        intervalos = cant_intervalos_input.get()

        for widget in frame.winfo_children():
            widget.destroy()

        _Frecuencia.calcular(frame, estadistico, intervalos,muestra)

    @staticmethod
    def calcular(frame, estadistico, intervalos, muestra):
        font_bold = CTkFont(family="Arial", size=25, weight="bold")

        n = len(muestra)

        fe = n / int(intervalos)

        label1 = ctk.CTkLabel(frame, text="", font=font_bold, text_color="white", wraplength=300)
        label1.pack(padx=20, pady=20, fill="both", expand=True)
        label1.configure(text=f"Frecuencia esperada (Fe): {fe}")

        frecuencias_observadas = [0] * int(intervalos)

        for valor in muestra:
            indice = min(int(valor * int(intervalos)), int(intervalos) - 1)
            frecuencias_observadas[indice] += 1

        label2 = ctk.CTkLabel(frame, text="Frecuencias observadas:", font=font_bold, text_color="white", wraplength=300)
        label2.pack(padx=20, pady=20, fill="both", expand=True)

        for i, fo in enumerate(frecuencias_observadas, 1):
            texto = f"Fo{i} = {fo}"
            label3 = ctk.CTkLabel(frame, text=texto, font=("Arial", 14))
            label3.pack(padx=20, pady=5, fill="both", expand=True)

        chi_cuadrado = sum((fo - fe) ** 2 / fe for fo in frecuencias_observadas)

        label4 = ctk.CTkLabel(frame, text="", font=font_bold, text_color="white", wraplength=300)
        label4.pack(padx=20, pady=20, fill="both", expand=True)
        label4.configure(text=f"Estadístico ingresado: {estadistico}")

        label4 = ctk.CTkLabel(frame, text="", font=font_bold, text_color="white", wraplength=300)
        label4.pack(padx=20, pady=20, fill="both", expand=True)
        label4.configure(text=f"Estadístico 𝜒²: {chi_cuadrado}")

        if chi_cuadrado < float(estadistico):
            label9 = ctk.CTkLabel(frame,
                                  text="Al ser el estadístico 𝜒² menor que el estadístico ingresado, no se rechaza la hipótesis de que los números provienen de un universo uniformemente distribuido",
                                  wraplength=400, font=font_bold, text_color="white")
            label9.pack(padx=20, pady=20, fill="both", expand=True)
        else:
            label10 = ctk.CTkLabel(frame,
                                   text="Al ser el estadístico 𝜒² mayor que el estadístico ingresado, se rechaza la hipótesis de que los números provienen de un universo uniformemente distribuido",
                                   wraplength=400, font=font_bold, text_color="white")
            label10.pack(padx=20, pady=20, fill="both", expand=True)


    @staticmethod
    def prueba_frecuencia(muestra, frame):
        font_bold = CTkFont(family="Arial", size=25, weight="bold")

        label = ctk.CTkLabel(frame, text="Prueba de la frecuencia", wraplength=500, font=font_bold, text_color="white")
        label.pack(padx=20, pady=15, fill="both", expand=True)

        label2 = ctk.CTkLabel(frame, text="Ingrese el dato del estadístico:", font=("Arial", 20), text_color="white")
        label2.pack(padx=20, pady=5, fill="both", expand=True)

        estadistico_input = ctk.CTkEntry(master=frame, placeholder_text="Estadístico", font=("Arial", 15))
        estadistico_input.pack(pady=5)

        label2 = ctk.CTkLabel(frame, text="Ingrese el número de subintervalos:", font=("Arial", 20), text_color="white")
        label2.pack(padx=20, pady=5, fill="both", expand=True)

        cant_intervalos_input = ctk.CTkEntry(master=frame, placeholder_text="Número", font=("Arial", 15))
        cant_intervalos_input.pack(pady=5)

        boton_continuar = ctk.CTkButton(frame, text="Continuar", command=lambda: _Frecuencia.continuar(frame, estadistico_input, cant_intervalos_input,muestra))
        boton_continuar.pack(pady=5)