
class _Ks:
    @staticmethod

    def prueba_ks(muestra):
        n = len(muestra) #tamano de la muestra
        estadistico = input()

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