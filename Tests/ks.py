import customtkinter as ctk

class _Ks:
    @staticmethod

    def prueba_ks(muestra, frame):

        label = ctk.CTkLabel(master=frame, text=f"Prueba KS {muestra}" , font=("Arial", 20))
        label.pack(pady=20)


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