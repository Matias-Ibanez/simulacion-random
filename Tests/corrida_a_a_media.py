import customtkinter as ctk

class _Corrida:

    @staticmethod
    def continuar(frame, estadistico_input, muestra):
        estadistico = estadistico_input.get()

        for widget in frame.winfo_children():
            widget.destroy()

        _Corrida.calcular(frame, estadistico, muestra)

    @staticmethod

    @staticmethod
    def calcular(frame, estadistico, muestra):
        n = len(muestra)  # tamano de la muestra

        s = []  # secuencia binaria

        for i in range(n):
            if muestra[i] <= 0.5:
                s.append(0)
            else:
                s.append(1)

        label3 = ctk.CTkLabel(frame, text="Secuencia binaria S: ", font=("Arial", 20))
        label3.pack(padx=20, pady=20, fill="both", expand=True)

        label4 = ctk.CTkLabel(frame, text="", font=("Arial", 15))
        label4.pack(padx=20, pady=20, fill="both", expand=True)
        label4.configure(text=s)

        longitudes = []
        contador = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                contador += 1
            else:
                longitudes.append(contador)
                contador = 1  # Reiniciar el contador para la nueva secuencia

        longitudes.append(contador)

        fo = {}  # diccionario de frecuencias observadas

        for i in longitudes:
            if i in fo:
                fo[i] += 1  # si ya esta agrego una
            else:
                fo[i] = 1  # si no esta la empiezo

        min_clave = min(fo.keys())
        max_clave = max(fo.keys())

        # Completar el diccionario con 0 para las claves faltantes
        for cantidad in range(min_clave, max_clave + 1):
            if cantidad not in fo:
                fo[cantidad] = 0

        fo_ordenado = dict(sorted(fo.items(), key=lambda x: x[0], reverse=False))

        label5 = ctk.CTkLabel(frame, text="Freciencias observadas: ", font=("Arial", 20))
        label5.pack(padx=20, pady=20, fill="both", expand=True)

        for i, (clave, valor) in enumerate(sorted(fo_ordenado.items())):
            texto = f"{clave}: {valor}"
            label6 = ctk.CTkLabel(frame, text=texto, font=("Arial", 14))
            label6.pack(padx=20, pady=20, fill="both", expand=True)

        fe = {}  # diccionario de frecuencias esperadas

        for i in range(1, max(longitudes) + 1):
            fe[i] = (n - i + 3) / (2 ** (i + 1))

        print("fe", fe)

        estadisticoXcuadrado = 0

        for i in range(len(fe)):
            clave = list(fo_ordenado.keys())[i]
            valorFo = fo_ordenado[clave]
            valorFe = fe[clave]
            estadisticoXcuadrado += (((valorFo - valorFe) ** 2) / valorFe)

        print(estadisticoXcuadrado)

        if estadisticoXcuadrado < estadistico:
            print("No se rechaza la hipótesis de que los números provienen de un universo uniformemente distribuido")

    def prueba_corrida(muestra, frame):
        label = ctk.CTkLabel(frame, text="Prueba de corrida arriba y abajo de la media", font=("Arial", 20))
        label.pack(padx=20, pady=20, fill="both", expand=True)

        label2 = ctk.CTkLabel(frame, text="Ingrese el dato del estadístico:", font=("Arial", 15))
        label2.pack(padx=20, pady=20, fill="both", expand=True)

        estadistico_input = ctk.CTkEntry(master=frame, placeholder_text="Introduce estadístico", font=("Arial", 15))
        estadistico_input.pack(pady=10)

        boton_continuar = ctk.CTkButton(frame, text="Continuar", command=lambda: _Corrida.continuar(frame, estadistico_input, muestra))
        boton_continuar.pack(pady=10)



"""
        n = len(muestra) #tamano de la muestra
        estadistico = float(input("Introduce el valor del estadístico: "))

        s = [] #secuencia binaria

        for i in range(n):
            if muestra[i] <= 0.5:
                s.append(0)
            else:
                s.append(1)

        print("muestra",muestra)
        print("secuencia",s)

        longitudes = []
        contador = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                contador += 1
            else:
                longitudes.append(contador)
                contador = 1  # Reiniciar el contador para la nueva secuencia

        longitudes.append(contador)

        fo = {} #diccionario de frecuencias observadas

        for i in longitudes:
            if i in fo:
                fo[i] += 1 #si ya esta agrego una
            else:
                fo[i] = 1 #si no esta la empiezo

        min_clave = min(fo.keys())
        max_clave = max(fo.keys())

        # Completar el diccionario con 0 para las claves faltantes
        for cantidad in range(min_clave, max_clave + 1):
            if cantidad not in fo:
                fo[cantidad] = 0

        fo_ordenado = dict(sorted(fo.items(), key=lambda x: x[0], reverse=False))


        print(fo_ordenado)

        fe = {} #diccionario de frecuencias esperadas

        for i in range(1, max(longitudes)+1):
            fe[i] = (n-i+3)/(2**(i+1))

        print("fe",fe)

        estadisticoXcuadrado = 0

        for i in range(len(fe)):
            clave = list(fo_ordenado.keys())[i]
            valorFo = fo_ordenado[clave]
            valorFe = fe[clave]
            estadisticoXcuadrado += (((valorFo-valorFe)**2)/valorFe)

        print(estadisticoXcuadrado)

        if estadisticoXcuadrado < estadistico:
            print("No se rechaza la hipótesis de que los números provienen de un universo uniformemente distribuido")

"""
