from random import randint
import pandas as pd 
import matplotlib.pyplot as plt
from math import pow
from math import sqrt

class Ruleta(object):
    
    def __init__(self):
        #Los arreglos terminados en A son arreglos de arreglos
        self.resultados = []
        self.frecuenciaRelativa = []
        self.vp = []
        self.varianzas = []
        self.desvios = []
        self.nroTirada =[]
        self.frecuenciaRelativaA = []
        self.vpA = []
        self.varianzasA = []
        self.desviosA = []
        self.nroTiradaA =[]
        self.ocurrencias = 0
        self.acumRelativas = 0
        self.acumResultados = 0
        self.promedio = 0
        self.acumVar = 0
        self.varEsp = 0
        self.desEsp = 0
        self.colores = ['gold','darkblue','darkorange','forestgreen','darkorchid']

    def tirar(self, n, e):
        self.tiradas = n
        for esperado in e:
            self.esperado = esperado
            for i in range(n+1):
                if i == 0:
                    pass
                else:
                    x = randint(0, 36)
                    self.resultados.append(x)
                    self.frt(i, x, esperado)
                    self.vpt(i,x)
                    self.varianza(i,x)
            self.fa()
            self.reiniciar(esperado, e)
            self.calculosFinales()
        self.imprimirGraficos()
        self.imprimirGraficosDeTodos()

    #Fecuencia por tirada
    def frt(self, i , x, esperado):
        if x == esperado:
            self.ocurrencias += 1
        if self.ocurrencias != 0:
            aux = self.ocurrencias/i
        else:
            aux = 0
        self.frecuenciaRelativa.append(aux)
        self.nroTirada.append(i)
        self.acumRelativas += aux

    #Valor Promedio de las tiradas
    def vpt(self, i, x):
        self.acumResultados = self.acumResultados + x
        self.vp.append(self.acumResultados/i)


    #Valor del desvio
    def desvio(self, var):
        self.desvios.append(sqrt(var))

    #Valor de la varianza
    def varianza(self, i, x):
        aux = pow((x-(self.acumResultados/i)),2)
        self.acumVar = self.acumVar + aux
        aux2 = self.acumVar/i
        self.varianzas.append(aux2)
        self.desvio(aux2)

    #Frecuencia absoluta de cada uno de los resultados
    def fa(self):
        a = pd.Series(self.resultados).value_counts()
        b = pd.DataFrame(a)
        b.columns = ['Cantidad']

    #calculos finales
    def calculosFinales(self):
         #Calculo para la FR
        print(self.acumRelativas)
        self.acumRelativas = self.acumRelativas / self.tiradas


        #Calculo del Promedio General
        aux = 0
        for i in range(37):
            aux = aux + i
        self.promedio = aux/37

        aux2 = 0
        for i in range(37):
            aux2 = aux2 + pow((i - self.promedio), 2)
        self.varEsp = aux2/37
        self.desEsp = sqrt(self.varEsp)

    def reiniciar(self, esperado, e):

        self.frecuenciaRelativaA.append(self.frecuenciaRelativa)
        self.vpA.append(self.vp)
        self.varianzasA.append(self.varianzas)
        self.desviosA.append(self.desvios)
        self.nroTiradaA.append(self.nroTirada)

        self.resultados = []
        self.frecuenciaRelativa = []
        self.vp = []
        self.varianzas = []
        self.desvios = []
        self.nroTirada =[]
        self.ocurrencias = 0
        if esperado == e[-1]:
            pass
        else:
            self.acumRelativas = 0
        self.acumResultados = 0
        self.promedio = 0
        self.acumVar = 0
        self.varEsp = 0
        self.desEsp = 0

    def imprimirGraficos(self):
        print(self.acumRelativas)
        print(self.tiradas)
        #Graficos
        plt.title('Graficos')

        p = len(self.nroTiradaA) - 1

        plt.subplot(2, 2, 1)
        plt.plot(self.nroTiradaA[p], self.frecuenciaRelativaA[p], color=self.colores[p])
        plt.axhline(y=self.acumRelativas, color='r', linestyle='-')
        plt.xlabel('n (numero de tiradas)')
        plt.ylabel('fr (frecuencia relativa)')

        plt.subplot(2, 2, 2)
        plt.plot(self.nroTiradaA[p], self.vpA[p], color=self.colores[p])
        plt.axhline(y=self.promedio, color='r', linestyle='-')
        plt.grid(True)
        plt.xlabel('n (numero de tiradas)')
        plt.ylabel('VP(Valor Promedio de las Tiradas)')


        plt.subplot(2, 2, 3)
        plt.plot(self.nroTiradaA[p], self.desviosA[p], color=self.colores[p])
        plt.axhline(y=self.desEsp, color='r', linestyle='-')
        plt.grid(True)
        plt.xlabel('n (numero de tiradas)')
        plt.ylabel('Desvio')

        plt.subplot(2, 2, 4)
        plt.plot(self.nroTiradaA[p], self.varianzasA[p], color=self.colores[p])
        plt.axhline(y=self.varEsp, color='r', linestyle='-')
        plt.grid(True)
        plt.xlabel('n (numero de tiradas)')
        plt.ylabel('Varianza')

        x = randint(10000, 99999)
        plt.savefig('full_figure_one_Tp_1_'+ str(x) +'.png')
        plt.show()

    def imprimirGraficosDeTodos(self):

        #Graficos
        plt.title('Graficos')
        plt.subplot(2, 2, 1)
        for p in range(len(self.nroTiradaA)):
            plt.plot(self.nroTiradaA[p], self.frecuenciaRelativaA[p], color=self.colores[p])
        plt.axhline(y=self.acumRelativas, color='r', linestyle='-')
        plt.xlabel('n (numero de tiradas)')
        plt.ylabel('fr (frecuencia relativa)')

        plt.subplot(2, 2, 2)
        for p in range(len(self.nroTiradaA)):
            plt.plot(self.nroTiradaA[p], self.vpA[p], color=self.colores[p])
        plt.axhline(y=self.promedio, color='r', linestyle='-')
        plt.grid(True)
        plt.xlabel('n (numero de tiradas)')
        plt.ylabel('VP(Valor Promedio de las Tiradas)')

        plt.subplot(2, 2, 3)
        for p in range(len(self.nroTiradaA)):
            plt.plot(self.nroTiradaA[p], self.desviosA[p], color=self.colores[p])
        plt.axhline(y=self.desEsp, color='r', linestyle='-')
        plt.grid(True)
        plt.xlabel('n (numero de tiradas)')
        plt.ylabel('Desvio')

        plt.subplot(2, 2, 4)
        for p in range(len(self.nroTiradaA)):
            plt.plot(self.nroTiradaA[p], self.varianzasA[p], color=self.colores[p])
        plt.axhline(y=self.varEsp, color='r', linestyle='-')
        plt.grid(True)
        plt.xlabel('n (numero de tiradas)')
        plt.ylabel('Varianza')

        x = randint(10000, 99999)
        plt.savefig('full_figure_all_TP_1_'+ str(x) +'.png')
        plt.show()



def main():
    r = Ruleta()
    r.tirar(10000, [5, 20, 33, 15, 18])


 
main()
