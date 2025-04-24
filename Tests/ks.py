import customtkinter as ctk

class _Ks:
    @staticmethod

    def prueba_ks(muestra, frame):
        frame.configure(fg_color="red")

        label = ctk.CTkLabel(frame, text="Prueba de Kolmogorov - Smirnov (K-S)", font=("Arial", 20))
        label.pack(padx=20, pady=20, fill="both", expand=True)




"""
        n = len(muestra) #tamano de la muestra
        estadistico_input = ctk.CTkEntry(placeholder_text="Introduce estadístico KS", font=("Arial", 15))
        estadistico_input.pack(pady=10)

        estadistico = estadistico_input.get()

        muestra.sort() #la ordena

        dist_acum = [] #distribucion acumulada

        for i in range(n):
            dist_acum.append(i/n)  #distribucion acumulada

        aux = []

        for i in range(n):
            aux.append(dist_acum[i]-muestra[i])

        estadisticoKS = max(aux)

        if estadisticoKS < estadistico:
            print("no se rechaza la hipótesis de que los números provienen de un universo uniformemente distribuido")
"""