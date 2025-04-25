import customtkinter as ctk
from customtkinter import CTkLabel, CTkFont

class _Ks:

    @staticmethod

    def continuar(frame, estadistico_input, muestra):
        estadistico = estadistico_input.get()

        for widget in frame.winfo_children():
            widget.destroy()

        _Ks.calcular(frame, estadistico, muestra)

    @staticmethod
    def calcular(frame, estadistico, muestra):
        muestra.sort()  # la ordena

        font_bold = CTkFont(family="Arial", size=20, weight="bold")

        n = len(muestra)  # tamano de la muestra

        label3 = ctk.CTkLabel(frame, text="Muestra ordenada de menor a mayor:",wraplength=300,font=font_bold, text_color="white")
        label3.pack(padx=20, pady=20, fill="both", expand=True)

        label4 = ctk.CTkLabel(frame, text="",wraplength=300 ,font=("Arial", 15))
        label4.pack(padx=20, pady=20, fill="both", expand=True)
        label4.configure(text=str(muestra))

        dist_acum = []  # distribucion acumulada

        for i in range(n):
            dist_acum.append(i / n)  # distribucion acumulada

        label5 = ctk.CTkLabel(frame, text="Distribución acumulada Fn(X):",wraplength=300, font=font_bold, text_color="white")
        label5.pack(padx=20, pady=20, fill="both", expand=True)

        label6 = ctk.CTkLabel(frame, text="",wraplength=300 ,font=("Arial", 15))
        label6.pack(padx=20, pady=20, fill="both", expand=True)
        label6.configure(text=str(dist_acum))

        aux = []

        for i in range(n):
            aux.append(dist_acum[i] - muestra[i])

        estadisticoKS = max(aux)

        label10 = ctk.CTkLabel(frame, text="", font=font_bold, text_color="white",wraplength=300)
        label10.pack(padx=20, pady=20, fill="both", expand=True)
        label10.configure(text=f"Estadistico: {estadistico}")

        label7 = ctk.CTkLabel(frame, text="", font=font_bold, text_color="white",wraplength=300)
        label7.pack(padx=20, pady=20, fill="both", expand=True)
        label7.configure(text=f"Estadístico K-S: {estadisticoKS}")

        if estadisticoKS < float(estadistico):
            label8 = ctk.CTkLabel(frame, text="Al ser el estadístico K-S menor que el estadístico ingresado, no se rechaza la hipótesis de que los números provienen de un universo uniformemente distribuido",wraplength=400 ,font=font_bold, text_color="white")
            label8.pack(padx=20, pady=20, fill="both", expand=True)
        else:
            label9 = ctk.CTkLabel(frame, text="Al ser el estadístico K-S mayor que el estadístico ingresado, se rechaza la hipótesis de que los números provienen de un universo uniformemente distribuido", wraplength=400, font=font_bold, text_color="white")
            label9.pack(padx=20, pady=20, fill="both", expand=True)

    @staticmethod

    def prueba_ks(muestra, frame):

        font_bold = CTkFont(family="Arial", size=25, weight="bold")

        label = ctk.CTkLabel(frame, text="Prueba de Kolmogorov - Smirnov (K-S)", font=font_bold,text_color="white")
        label.pack(padx=20, pady=20, fill="both", expand=True)

        label2 = ctk.CTkLabel(frame, text="Ingrese el dato del estadístico:", font=("Arial", 20),text_color="white")
        label2.pack(padx=20, pady=5, fill="both", expand=True)

        estadistico_input = ctk.CTkEntry(master=frame, placeholder_text="Estadístico", font=("Arial", 15))
        estadistico_input.pack(pady=5)

        boton_continuar = ctk.CTkButton(frame, text="Continuar", command=lambda: _Ks.continuar(frame, estadistico_input, muestra))
        boton_continuar.pack(pady=5)

