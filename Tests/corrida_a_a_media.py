import customtkinter as ctk

class _Corrida:
    @staticmethod

    def prueba_corrida(muestra, frame):

        label = ctk.CTkLabel(muestra, text="Prueba corrida", font=("Arial", 20))
        label.pack(pady=20)


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


