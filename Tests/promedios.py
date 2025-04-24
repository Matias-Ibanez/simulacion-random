import math
import customtkinter as ctk

class _Promedios:
    @staticmethod
    def prueba_promedios(muestra,frame):
        frame.configure(fg_color="red")

        label = ctk.CTkLabel(frame, text="Prueba de los promedios", font=("Arial", 20))
        label.pack(padx=20, pady=20, fill="both", expand=True)

"""
        z_alpha = float(input("Ingrese el valor de Zα (nivel de significancia): "))
        n = len(muestra)
        promedio = sum(muestra) / n
        print(f"Promedio Aritmético (X̄): {promedio:.5f}")

        estadistico_z0 = (promedio - 0.5) * math.sqrt(n / (1 / 12))
        print(f"Estadístico Z₀: {estadistico_z0:.5f}")

        if abs(estadistico_z0) < z_alpha:
            print(f"{abs(estadistico_z0):.5f} < {z_alpha} -> No se rechaza la hipótesis")
        else:
            print(f"{abs(estadistico_z0):.5f} >= {z_alpha} -> Se rechaza la hipótesis")
"""