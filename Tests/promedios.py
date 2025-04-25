import math
import customtkinter as ctk
from customtkinter import CTkLabel, CTkFont

class _Promedios:

    @staticmethod
    def continuar(frame, estadistico_input, muestra):
        estadistico = estadistico_input.get()

        for widget in frame.winfo_children():
            widget.destroy()

        _Promedios.calcular(frame, estadistico, muestra)

    @staticmethod
    def calcular(frame, estadistico, muestra):

        font_bold = CTkFont(family="Arial", size=25, weight="bold")

        n = len(muestra)
        promedio = sum(muestra) / n

        label3 = ctk.CTkLabel(frame, text="", font=font_bold, text_color="white",wraplength=300)
        label3.pack(padx=20, pady=20, fill="both", expand=True)
        label3.configure(text=f"Promedio aritmético: {promedio}")

        estadistico_z0 = (promedio - 0.5) * math.sqrt(n / (1 / 12))

        label4 = ctk.CTkLabel(frame, text="", font=font_bold, text_color="white",wraplength=300)
        label4.pack(padx=20, pady=20, fill="both", expand=True)
        label4.configure(text=f"Estadístico Z₀: {estadistico_z0}")

        label4 = ctk.CTkLabel(frame, text="", font=font_bold, text_color="white", wraplength=300)
        label4.pack(padx=20, pady=20, fill="both", expand=True)
        label4.configure(text=f"Estadístico ingresado: {estadistico}")

        if estadistico_z0 < float(estadistico):
            label9 = ctk.CTkLabel(frame, text="Al ser el estadístico Z₀ menor que el estadístico ingresado, no se rechaza la hipótesis de que los números provienen de un universo uniformemente distribuido", wraplength=400, font=font_bold, text_color="white")
            label9.pack(padx=20, pady=20, fill="both", expand=True)
        else:
            label10 = ctk.CTkLabel(frame, text="Al ser el estadístico X^2 mayor que el estadístico ingresado, se rechaza la hipótesis de que los números provienen de un universo uniformemente distribuido", wraplength=400, font=font_bold, text_color="white")
            label10.pack(padx=20, pady=20, fill="both", expand=True)



    @staticmethod
    def prueba_promedios(muestra,frame):

        font_bold = CTkFont(family="Arial", size=25, weight="bold")

        label = ctk.CTkLabel(frame, text="Prueba de los promedios", wraplength=500, font=font_bold, text_color="white")
        label.pack(padx=20, pady=15, fill="both", expand=True)

        label2 = ctk.CTkLabel(frame, text="Ingrese el dato del estadístico:", font=("Arial", 20), text_color="white")
        label2.pack(padx=20, pady=5, fill="both", expand=True)

        estadistico_input = ctk.CTkEntry(master=frame, placeholder_text="Estadístico", font=("Arial", 15))
        estadistico_input.pack(pady=5)

        boton_continuar = ctk.CTkButton(frame, text="Continuar", command=lambda: _Promedios.continuar(frame, estadistico_input, muestra))
        boton_continuar.pack(pady=5)