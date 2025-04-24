import customtkinter as ctk

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

        n = len(muestra)  # tamano de la muestra

        label3 = ctk.CTkLabel(frame, text="Muestra ordenada de menor a mayor:",wraplength=300,font=("Arial", 15))
        label3.pack(padx=20, pady=20, fill="both", expand=True)

        label4 = ctk.CTkLabel(frame, text="", font=("Arial", 15))
        label4.pack(padx=20, pady=20, fill="both", expand=True)
        label4.configure(text=str(muestra))

        dist_acum = []  # distribucion acumulada

        for i in range(n):
            dist_acum.append(i / n)  # distribucion acumulada

        label5 = ctk.CTkLabel(frame, text="Distribución acumulada Fn(X):",wraplength=300, font=("Arial", 15))
        label5.pack(padx=20, pady=20, fill="both", expand=True)

        label6 = ctk.CTkLabel(frame, text="",wraplength=300 ,font=("Arial", 15))
        label6.pack(padx=20, pady=20, fill="both", expand=True)
        label6.configure(text=str(dist_acum))

        aux = []

        for i in range(n):
            aux.append(dist_acum[i] - muestra[i])

        estadisticoKS = max(aux)

        label10 = ctk.CTkLabel(frame, text="", font=("Arial", 15))
        label10.pack(padx=20, pady=20, fill="both", expand=True)
        label10.configure(text=f"Estadistico: {estadistico}")

        label7 = ctk.CTkLabel(frame, text="", font=("Arial", 15))
        label7.pack(padx=20, pady=20, fill="both", expand=True)
        label7.configure(text=f"Estadistico K-S: {estadisticoKS}")

        if estadisticoKS < float(estadistico):
            label8 = ctk.CTkLabel(frame, text="Al ser el estadistico K-S menor que el estadistico ingresado, no se rechaza la hipótesis de que los números provienen de un universo uniformemente distribuido",wraplength=400 ,font=("Arial", 15))
            label8.pack(padx=20, pady=20, fill="both", expand=True)
        else:
            label9 = ctk.CTkLabel(frame, text="Al ser el estadistico K-S mayor que el estadistico ingresado, se rechaza la hipótesis de que los números provienen de un universo uniformemente distribuido", wraplength=400, font=("Arial", 15))
            label9.pack(padx=20, pady=20, fill="both", expand=True)

    @staticmethod

    def prueba_ks(muestra, frame):

        label = ctk.CTkLabel(frame, text="Prueba de Kolmogorov - Smirnov (K-S)", font=("Arial", 20))
        label.pack(padx=20, pady=20, fill="both", expand=True)

        label2 = ctk.CTkLabel(frame, text="Ingrese el dato del estadístico:", font=("Arial", 15))
        label2.pack(padx=20, pady=20, fill="both", expand=True)

        estadistico_input = ctk.CTkEntry(master=frame, placeholder_text="Introduce estadístico", font=("Arial", 15))
        estadistico_input.pack(pady=10)

        boton_continuar = ctk.CTkButton(frame, text="Continuar", command=lambda: _Ks.continuar(frame, estadistico_input, muestra))
        boton_continuar.pack(pady=10)

