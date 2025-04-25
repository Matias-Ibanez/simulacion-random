import customtkinter as ctk

class _Serie:

    @staticmethod
    def continuar(frame, estadistico_input, divisiones_input,muestra):
        estadistico = estadistico_input.get()
        divisiones = divisiones_input.get()

        for widget in frame.winfo_children():
            widget.destroy()

        _Serie.calcular(frame, estadistico, divisiones,muestra)

    @staticmethod
    def calcular(frame, estadistico, divisiones,muestra):
        n = len(muestra) // 2
        pares = [(muestra[2 * i], muestra[2 * i + 1]) for i in range(n)]

        fe = n / (divisiones * divisiones)

        label1 = ctk.CTkLabel(frame, text="", font=font_bold, text_color="white", wraplength=300)
        label1.pack(padx=20, pady=20, fill="both", expand=True)
        label1.configure(text=f"Frecuencia esperada (Fe): {fe}")

        # Inicializamos la matriz de frecuencias observadas
        frecuencias_observadas = [[0 for _ in range(x)] for _ in range(x)]

        for u1, u2 in pares:
            j = min(int(u1 * x), x - 1)
            k = min(int(u2 * x), x - 1)
            frecuencias_observadas[j][k] += 1

        # Mostrar frecuencias observadas
        print("\nFrecuencias observadas (Fojk):")
        for j in range(x):
            for k in range(x):
                print(f"F{j + 1}{k + 1} = {frecuencias_observadas[j][k]}")

        # Cálculo del estadístico chi-cuadrado
        chi_cuadrado = sum(
            (frecuencias_observadas[j][k] - fe) ** 2 / fe
            for j in range(x)
            for k in range(x)
        )

        print(f"\nEstadístico 𝜒²: {chi_cuadrado:.5f}")

        if chi_cuadrado < chi_cuadrado_alpha:
            print(f"{chi_cuadrado:.5f} < {chi_cuadrado_alpha} → No se rechaza la hipótesis de uniformidad.")
        else:
            print(f"{chi_cuadrado:.5f} ≥ {chi_cuadrado_alpha} → Se rechaza la hipótesis de uniformidad.")


    @staticmethod
    def prueba_serie(muestra, frame):
        font_bold = CTkFont(family="Arial", size=25, weight="bold")

        label = ctk.CTkLabel(frame, text="Prueba de la serie", wraplength=500, font=font_bold, text_color="white")
        label.pack(padx=20, pady=15, fill="both", expand=True)

        label2 = ctk.CTkLabel(frame, text="Ingrese el dato del estadístico:", font=("Arial", 20), text_color="white")
        label2.pack(padx=20, pady=5, fill="both", expand=True)

        estadistico_input = ctk.CTkEntry(master=frame, placeholder_text="Estadístico", font=("Arial", 15))
        estadistico_input.pack(pady=5)

        label2 = ctk.CTkLabel(frame, text="Ingrese el número de divisiones (X):", font=("Arial", 20), text_color="white")
        label2.pack(padx=20, pady=5, fill="both", expand=True)

        divisiones_input = ctk.CTkEntry(master=frame, placeholder_text="Número", font=("Arial", 15))
        divisiones_input.pack(pady=5)

        boton_continuar = ctk.CTkButton(frame, text="Continuar", command=lambda: _Serie.continuar(frame, estadistico_input, divisiones_input, muestra))
        boton_continuar.pack(pady=5)


"""
        if len(muestra) < 2:
            print("La muestra debe tener al menos 2 valores.")
            return

        try:
            x = int(input("Ingrese el número de divisiones (x): "))
            chi_cuadrado_alpha = float(input("Ingrese el valor crítico 𝜒²α: "))
        except ValueError:
            print("Error: Ingrese valores numéricos válidos.")
            return

        # Se forman n pares consecutivos
        n = len(muestra) // 2
        pares = [(muestra[2 * i], muestra[2 * i + 1]) for i in range(n)]

        fe = n / (x * x)
        print(f"\nFrecuencia esperada (Fe): {fe:.3f}")

        # Inicializamos la matriz de frecuencias observadas
        frecuencias_observadas = [[0 for _ in range(x)] for _ in range(x)]

        for u1, u2 in pares:
            j = min(int(u1 * x), x - 1)
            k = min(int(u2 * x), x - 1)
            frecuencias_observadas[j][k] += 1

        # Mostrar frecuencias observadas
        print("\nFrecuencias observadas (Fojk):")
        for j in range(x):
            for k in range(x):
                print(f"F{j+1}{k+1} = {frecuencias_observadas[j][k]}")

        # Cálculo del estadístico chi-cuadrado
        chi_cuadrado = sum(
            (frecuencias_observadas[j][k] - fe) ** 2 / fe
            for j in range(x)
            for k in range(x)
        )

        print(f"\nEstadístico 𝜒²: {chi_cuadrado:.5f}")

        if chi_cuadrado < chi_cuadrado_alpha:
            print(f"{chi_cuadrado:.5f} < {chi_cuadrado_alpha} → No se rechaza la hipótesis de uniformidad.")
        else:
            print(f"{chi_cuadrado:.5f} ≥ {chi_cuadrado_alpha} → Se rechaza la hipótesis de uniformidad.")
"""
