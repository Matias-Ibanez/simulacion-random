import random
import math


# Función para realizar la prueba de los promedios
def prueba_promedios(n, z_alpha):
    # Paso 1: Generar una muestra de n números pseudo-aleatorios ui entre 0 y 1
    muestra = [random.random() for _ in range(n)]

    # Paso 2: Calcular el promedio aritmético de los números generados
    promedio = sum(muestra) / n
    print(f"Promedio Aritmético (X̄): {promedio}")

    # Paso 3: Calcular el estadístico Z0
    estadistico_z0 = (promedio - 0.5) * n / math.sqrt(n / 12)
    print(f"Estadístico Z0: {estadistico_z0}")

    # Paso 4: Comparar Z0 con Zα
    if abs(estadistico_z0) < z_alpha:
        print(f"{abs(estadistico_z0)} < {z_alpha} -> No se rechaza la hipótesis")
    else:
        print(f"{abs(estadistico_z0)} >= {z_alpha} -> Se rechaza la hipótesis")
