import customtkinter as ctk
from customtkinter import CTkLabel, CTkFont

class _Corrida:

    @staticmethod
    def continuar(frame, estadistico_input, muestra):
        estadistico = estadistico_input.get()

        for widget in frame.winfo_children():
            widget.destroy()

        _Corrida.calcular(frame, estadistico, muestra)

    @staticmethod
    def calcular(frame, estadistico, muestra):
        n = len(muestra)  # tamano de la muestra

        s = []  # secuencia binaria

        font_bold = CTkFont(family="Arial", size=20, weight="bold")

        for i in range(n):
            if muestra[i] <= 0.5:
                s.append(0)
            else:
                s.append(1)

        label3 = ctk.CTkLabel(frame, text="Secuencia binaria S: ", font=font_bold, text_color="white")
        label3.pack(padx=20, pady=20, fill="both", expand=True)

        label4 = ctk.CTkLabel(frame, text="", wraplength=300, font=("Arial", 15))
        label4.pack(padx=20, pady=20, fill="both", expand=True)
        label4.configure(text=s)

        longitudes = []
        contador = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                contador += 1
            else:
                longitudes.append(contador)
                contador = 1

        longitudes.append(contador)

        fo = {}

        for i in longitudes:
            if i in fo:
                fo[i] += 1
            else:
                fo[i] = 1

        min_clave = min(fo.keys())
        max_clave = max(fo.keys())

        for cantidad in range(min_clave, max_clave + 1):
            if cantidad not in fo:
                fo[cantidad] = 0

        fo_ordenado = dict(sorted(fo.items(), key=lambda x: x[0], reverse=False))

        label5 = ctk.CTkLabel(frame, text="Frecuencias observadas: ", font=font_bold, text_color="white")
        label5.pack(padx=20, pady=20, fill="both", expand=True)

        for i, (clave, valor) in enumerate(sorted(fo_ordenado.items())):
            texto = f"{clave}: {valor}"
            label6 = ctk.CTkLabel(frame, text=texto, font=("Arial", 14))
            label6.pack(padx=20, pady=5, fill="both", expand=True)

        fe = {}

        for i in range(1, max(longitudes) + 1):
            fe[i] = (n - i + 3) / (2 ** (i + 1))

        label6 = ctk.CTkLabel(frame, text="Frecuencias esperadas: ", font=font_bold, text_color="white")
        label6.pack(padx=20, pady=20, fill="both", expand=True)

        for i, (clave, valor) in enumerate(sorted(fe.items())):
            texto = f"{clave}: {valor}"
            label6 = ctk.CTkLabel(frame, text=texto, font=("Arial", 14))
            label6.pack(padx=20, pady=5, fill="both", expand=True)

        estadisticoXcuadrado = 0

        for i in range(len(fe)):
            clave = list(fo_ordenado.keys())[i]
            valorFo = fo_ordenado[clave]
            valorFe = fe[clave]
            estadisticoXcuadrado += (((valorFo - valorFe) ** 2) / valorFe)

        label7 = ctk.CTkLabel(frame, text="", font=font_bold, text_color="white",wraplength=300)
        label7.pack(padx=20, pady=20, fill="both", expand=True)
        label7.configure(text=f"Estadístico X^2: {estadisticoXcuadrado}")

        label8 = ctk.CTkLabel(frame, text="", font=font_bold, text_color="white",wraplength=300)
        label8.pack(padx=20, pady=20, fill="both", expand=True)
        label8.configure(text=f"Estadístico: {estadistico}")

        if estadisticoXcuadrado < float(estadistico):
            label9 = ctk.CTkLabel(frame, text="Al ser el estadístico X^2 menor que el estadístico ingresado, no se rechaza la hipótesis de que los números provienen de un universo uniformemente distribuido", wraplength=400, font=font_bold, text_color="white")
            label9.pack(padx=20, pady=20, fill="both", expand=True)
        else:
            label10 = ctk.CTkLabel(frame, text="Al ser el estadístico X^2 mayor que el estadístico ingresado, se rechaza la hipótesis de que los números provienen de un universo uniformemente distribuido", wraplength=400, font=font_bold, text_color="white")
            label10.pack(padx=20, pady=20, fill="both", expand=True)

    @staticmethod
    def prueba_corrida(muestra, frame):

        font_bold = CTkFont(family="Arial", size=25, weight="bold")

        label = ctk.CTkLabel(frame, text="Prueba de corrida arriba y abajo de la media", wraplength=500, font=font_bold, text_color="white")
        label.pack(padx=20, pady=15, fill="both", expand=True)

        label2 = ctk.CTkLabel(frame, text="Ingrese el dato del estadístico:", font=("Arial", 20), text_color="white")
        label2.pack(padx=20, pady=5, fill="both", expand=True)

        estadistico_input = ctk.CTkEntry(master=frame, placeholder_text="Estadístico", font=("Arial", 15))
        estadistico_input.pack(pady=5)

        boton_continuar = ctk.CTkButton(frame, text="Continuar", command=lambda: _Corrida.continuar(frame, estadistico_input, muestra))
        boton_continuar.pack(pady=5)


