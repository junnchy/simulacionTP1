from random import randint
import pandas as pd
import matplotlib.pyplot as plt


class Ruleta(object):

    def __init__(self):
        #Los arreglos terminados en A son arreglos de arreglos
        self.resultados = []
        self.apuestas = []
        self.ganadores =[]
        self.nro_juego= 0
        self.panio = {
            'paridad': {
                'par': [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36],
                'impar': [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35],
                'paga': 2
            },
            'mitades':{
                '1':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],
                '2':[19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36],
                'paga': 2
            },
            'color':{
                'rojo': [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36],
                'negro':[2,4,5,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35],
                'paga': 2
            },
            'docenas':{
                '1': [1,2,3,4,5,6,7,8,9,10,11,12],
                '2': [13,14,15,16,17,18,9,20,21,22,23,24],
                '3': [25,26,27,28,29,30,31,32,33,34,35,36],
                'paga': 1.5
            },
            'columnas':{
                '1': [1,4,7,10,13,16,19,22,25,28,31,34],
                '2': [2,5,8,11,14,17,20,23,26,29,32,35],
                '3': [3,6,9,12,15,18,21,24,27,30,33,36],
                'paga': 1.5
            },
        }

    def jugar(self):
        self.definirGanador(self.tirar())
        print(self.resultados)
        print(self.ganadores)

    def tomarApuestas(self, apuestas, nro_juego):
        for apuesta in apuestas:
            self.apuestas.append(apuesta)
        self.nro_juego = nro_juego

    def tirar(self):
        x = randint(0, 36)
        self.resultados.append(x)
        return x

    def definirGanador(self, nro):
        ganadores = []
        if nro == 0:
            ganadores.append(nro)
        else:
            #Paridad
            if nro in self.panio['paridad']['par']:
                ganadores.append('par')
            elif nro in self.panio['paridad']['impar']:
                ganadores.append('impar')

            #Mitades
            if nro in self.panio['mitades']['1']:
                ganadores.append('m-1')
            elif nro in self.panio['mitades']['2']:
                ganadores.append('m-2')

            #Colores
            if nro in self.panio['color']['rojo']:
                ganadores.append('rojo')
            elif nro in self.panio['color']['negro']:
                ganadores.append('negro')

            #Docenas
            if nro in self.panio['docenas']['1']:
                ganadores.append('d-1')
            elif nro in self.panio['docenas']['2']:
                ganadores.append('d-2')
            elif nro in self.panio['docenas']['3']:
                ganadores.append('d-3')

            #Columnas
            if nro in self.panio['columnas']['1']:
                ganadores.append('c-1')
            elif nro in self.panio['columnas']['2']:
                ganadores.append('c-2')
            elif nro in self.panio['columnas']['3']:
                ganadores.append('c-3')

            self.ganadores.append(ganadores)

    def pagar(self):
        print('nro j',self.nro_juego)
        print('ganador',self.ganadores)
        print('apuestas de jugadores', self.apuestas)
        for apuesta in self.apuestas:
            if apuesta['apuesta'] in self.ganadores[self.nro_juego]:
                aux = apuesta['cantidad'] * 2
                print('gano:', aux)
                return {'pago': aux, 'nombre': apuesta['nombre']}
            else:
                return {'pago': 0, 'nombre': apuesta['nombre']}


class Jugador(object,):

    def __init__(self, nombre):
        self.capital = 100000000
        self.nombre = nombre
        self.apuesta = 100
        self.evolucionCapital = []
        self.ganancias = []
        self.resultados = []
        self.apuestas =[]
        self.nroJuego = []
        self.j = 0

    def apostar(self):
        self.j += 1
        self.nroJuego.append(self.j)
        if self.capital >= self.apuesta:
            self.capital -= self.apuesta
            self.apuestas.append(self.apuesta)
            return {
                'apuesta': 'par',
                'cantidad': self.apuesta,
                'nombre': self.nombre
            }
        else:
            print('Ya no queda plata')

    def tomarGanancia(self, ganancia):
        if ganancia['pago'] == 0:
            self.resultados.append('perdi')
            self.apuesta = self.apuesta * 2

        else:
            self.capital += ganancia['pago']
            self.resultados.append('gane')

        self.ganancias.append(ganancia['pago'])
        self.evolucionCapital.append(self.capital)
        self.mostarResultados()

    def mostarResultados(self):
        print('Capital:', self.capital)
        print('Evolucion Capital: ', self.evolucionCapital)
        print('Resultados: ', self.resultados)
        print('Ganancias: ', self.ganancias)
        print('Apuestas: ', self.apuestas)
        print('1...', self.nroJuego)

    def imprimirGraficos(self):
        plt.plot(self.nroJuego, self.evolucionCapital, color='r')
        plt.xlabel('n (numero de tiradas)')
        plt.ylabel('CAPITAL')

        plt.show()

def main():
    r = Ruleta()
    j1 = Jugador('j1')
    for n in range(20):
        r.tomarApuestas([j1.apostar()], n)
        r.jugar()
        j1.tomarGanancia(r.pagar())
    j1.imprimirGraficos()

main()
