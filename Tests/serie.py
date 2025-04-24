import customtkinter as ctk

class _Serie:
    @staticmethod
    def prueba_serie(muestra, frame):

        label = ctk.CTkLabel(muestra, text="Prueba KS", font=("Arial", 20))
        label.pack(pady=20)

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
