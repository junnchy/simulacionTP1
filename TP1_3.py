from random import randint
import pandas as pd 
import matplotlib.pyplot as plt
from math import pow
from math import sqrt

class Ruleta(object):
    
    def __init__(self):
        self.resultados = []
        self.frecuenciaRelativa = []
        self.vp = []
        self.varianzas = []
        self.desvios = []
        self.nroTirada =[]
        self.ocurrencias = 0
        self.acumRelativas = 0
        self.acumResultados = 0
        self.promedio = 0
        self.acumVar = 0
        self.varEsp = 0
        self.desEsp = 0

    def tirar(self, n, esperado):
        self.tiradas = n
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
        print('Resultados: ', self.resultados)
        print(len(self.nroTirada), len(self.vp), len(self.frecuenciaRelativa))
        print(pd.DataFrame(self.frecuenciaRelativa))
        self.fa()
        self.calculosFinales()
        self.imprimirGraficos()
        print('Frecuencia Relativa esperada: ', self.acumRelativas)

    #Fecuencia por tirada
    def frt(self, i , x, esperado):
        if x == esperado:
            self.ocurrencias = self.ocurrencias + 1
        if self.ocurrencias != 0:
            aux = self.ocurrencias/i
        else:
            aux = 0
        self.frecuenciaRelativa.append(aux)
        self.nroTirada.append(i)
        self.acumRelativas = aux + self.acumRelativas

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
        print(b.loc[[self.esperado]])

    #calculos finales
    def calculosFinales(self):
         #Calculo para la FR
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


    def imprimirGraficos(self):

        #Graficos
        plt.title('Graficos')

        plt.subplot(2, 2, 1)
        plt.plot(self.nroTirada, self.frecuenciaRelativa, color='darkblue')
        plt.axhline(y=self.acumRelativas, color='r', linestyle='-')
        plt.xlabel('n (numero de tiradas)')
        plt.ylabel('fr (frecuencia relativa)')

        plt.subplot(2, 2, 2)
        plt.plot(self.nroTirada, self.vp, color='darkorange')
        plt.axhline(y=self.promedio, color='r', linestyle='-')
        plt.xlabel('n (numero de tiradas)')
        plt.ylabel('VP(Valor Promedio de las Tiradas)')


        plt.subplot(2, 2, 3)
        plt.plot(self.nroTirada, self.desvios, color='forestgreen')
        plt.axhline(y=self.desEsp, color='r', linestyle='-')
        plt.xlabel('n (numero de tiradas)')
        plt.ylabel('Desvio')

        plt.subplot(2, 2, 4)
        plt.plot(self.nroTirada, self.varianzas, color='darkorchid')
        plt.axhline(y=self.varEsp, color='r', linestyle='-')
        plt.xlabel('n (numero de tiradas)')
        plt.ylabel('Varianza')

        plt.savefig('full_figure.png')
        plt.show()



def main():
    r = Ruleta()
    r.tirar(10000, 5)


 
main()
