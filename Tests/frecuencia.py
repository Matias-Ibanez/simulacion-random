import math
import customtkinter as ctk

class _Frecuencia:
    @staticmethod

    def prueba_frecuencia(muestra, frame):

        label = ctk.CTkLabel(muestra, text="Prueba KS", font=("Arial", 20))
        label.pack(pady=20)

        n = len(muestra)
        x = int(input("Ingrese el número de sub-intervalos (x): "))
        chi_cuadrado_alpha = float(input("Ingrese el valor crítico de chi-cuadrado (𝜒²α): "))

        fe = n / x
        print(f"\nFrecuencia esperada (Fe): {fe:.2f}")

        frecuencias_observadas = [0] * x

        for valor in muestra:
            indice = min(int(valor * x), x - 1)
            frecuencias_observadas[indice] += 1

        print("\nFrecuencias observadas:")
        for i, fo in enumerate(frecuencias_observadas, 1):
            print(f"Fo{i} = {fo}")

        chi_cuadrado = sum((fo - fe) ** 2 / fe for fo in frecuencias_observadas)
        print(f"\nEstadístico 𝜒²: {chi_cuadrado:.5f}")

        if chi_cuadrado < chi_cuadrado_alpha:
            print(f"{chi_cuadrado:.5f} < {chi_cuadrado_alpha} → No se rechaza la hipótesis de uniformidad.")
        else:
            print(f"{chi_cuadrado:.5f} ≥ {chi_cuadrado_alpha} → Se rechaza la hipótesis de uniformidad.")
