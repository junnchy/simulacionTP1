from random import randint
import pandas as pd
import matplotlib.pyplot as plt


class Ruleta(object):

    def __init__(self):
        #Los arreglos terminados en A son arreglos de arreglos
        self.resultados = []
        self.apuestas = []
        self.ganadores = {}
        self.listaGanadores =[]
        self.tiradas= []
        self.paga2 = ['par', 'impar', 'm-1', 'm-2','rojo', 'negro']
        self.paga1_5 = ['c-1','c-2','c-3','d-1','d-2','d-3']
        self.pagos =[]
        self.panio = {
            'paridad': {
                'par': [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36],
                'impar': [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
            },
            'mitades':{
                '1':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],
                '2':[19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
            },
            'color':{
                'rojo': [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36],
                'negro':[2,4,5,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
            },
            'docenas':{
                '1': [1,2,3,4,5,6,7,8,9,10,11,12],
                '2': [13,14,15,16,17,18,9,20,21,22,23,24],
                '3': [25,26,27,28,29,30,31,32,33,34,35,36]
            },
            'columnas':{
                '1': [1,4,7,10,13,16,19,22,25,28,31,34],
                '2': [2,5,8,11,14,17,20,23,26,29,32,35],
                '3': [3,6,9,12,15,18,21,24,27,30,33,36]
            },
        }

    def jugar(self, n):
        self.definirGanador(self.tirar(n))


    def tomarApuestas(self, apuestas):
        if apuestas == [None]:
            self.apuestas = []
        else:
            self.apuestas = []
            for apuesta in apuestas:
                self.apuestas.append(apuesta)


    def tirar(self,n):
        x = randint(0, 36)
        self.resultados.append(x)
        self.tiradas.append(n)
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

            self.ganadores = ganadores
            self.listaGanadores.append(ganadores)

    def pagar(self):
        self.pagos =[]
        if self.apuestas is not None:
            for apuesta in self.apuestas:
                if apuesta['apuesta'] in self.ganadores:
                    if apuesta['apuesta'] in self.paga2:
                        aux = apuesta['cantidad'] * 2
                        self.pagos.append({'pago': aux, 'nombre': apuesta['nombre']})
                    elif apuesta['apuesta'] in self.paga1_5:
                        aux = apuesta['cantidad'] * 1.5
                        self.pagos.append({'pago': aux, 'nombre': apuesta['nombre']})
                else:
                    self.pagos.append({'pago': 0, 'nombre': apuesta['nombre']})
            return self.pagos
        else:
            pass
            # print('No se recibieron apuestas')


class Jugador(object,):

    def __init__(self, nombre, tc, jugada, aque):
        self.capital = 10000000
        self.nombre = nombre
        self.apuesta = 1
        self.evolucionCapital = []
        self.ganancias = []
        self.resultados = []
        self.apuestas =[]
        self.nroJuego = []
        self.ganadoxt = []
        self.ganados = 0
        self.perdidos = 0
        self.jugada = jugada
        self.aque =aque
        self.tc = tc #Tipo de capital 0 limitado 1 ilimitado
        self.juega = True
        self.j = 0

    def continua(self):
        return self.juega

    def apostarMartingala(self, valor):
        if self.juega:
            if self.capital >= self.apuesta:
                self.j += 1
                self.nroJuego.append(self.j)
                self.capital -= self.apuesta
                self.apuestas.append(self.apuesta)

                return {
                    'apuesta': valor,
                    'cantidad': self.apuesta,
                    'nombre': self.nombre
                }
            else:
                # print('Ya no queda plata')
                self.juega = False
        else:
            pass

    def tomarGanancia(self, ganancia):
        if self.juega:
            for pago in ganancia:
                if pago['nombre'] == self.nombre:
                    if pago['pago'] == 0:
                        self.resultados.append('perdi')
                        self.perdidos += 1
                        self.apuesta = self.apuesta * 2
                        if self.tc == 1:
                            self.capital = self.capital * 2   #Capital limitado
                        else:
                            pass
                    else:
                        self.capital = (self.capital - self.apuesta) + pago['pago']
                        self.resultados.append('gane')
                        self.ganados += 1

                    self.ganancias.append(pago['pago'])
                    self.evolucionCapital.append(self.capital)
                    # self.mostarResultados()
                else:
                    pass
            else:
                pass

    def mostarResultados(self):
        # print('Capital:', self.capital)
        # print('Evolucion Capital: ', self.evolucionCapital)
        print('Resultados: ', self.resultados)
        print('Ganancias: ', self.ganancias)
        print('Apuestas: ', self.apuestas)
        print('1...', self.nroJuego)
        print('Ganados:', self.ganados)
        print('Perdidos', self.perdidos)

    def defineJuagda(self):
        if self.jugada == 1:
            return self.apostarMartingala(self.aque)

    def devolverResultados(self):
        if self.tc == 1:
            return [self.apuestas, self.ganancias, self.nroJuego]
        else:
            return [self.apuestas, self.ganancias, self.nroJuego, self.evolucionCapital]

    def imprimirGraficos(self):
        print(len(self.nroJuego), self.nroJuego)
        print(len(self.evolucionCapital), self.evolucionCapital)
        print(len(self.apuestas), self.apuestas)

        plt.subplot(2, 2, 1)
        plt.plot(self.nroJuego, self.apuestas, color='darkblue')
        plt.xlabel('n (numero de tiradas)')
        plt.ylabel('Apuestas')

        plt.subplot(2, 2, 2)
        plt.plot(self.nroJuego, self.ganancias, color='darkblue')
        plt.xlabel('n (numero de tiradas)')
        plt.ylabel('Ganancias')

        # plt.subplot(2, 2, 3)
        # plt.plot(self.nroJuego, self.evolucionCapital, color='darkblue')
        # plt.xlabel('n (numero de tiradas)')
        # plt.ylabel('CAPITAL')

        plt.show()

def main():
    resultados =[]
    colores = ['gold','darkblue','darkorange','forestgreen','darkorchid','violet', 'dark']
    r = Ruleta()
    #Instancias de Jugador (Primer parametro) => Nombre
    #Instancias de Jugador (Segundo parametro) => 0 para capital limitado 1 para ilimitado
    #Instancias de Jugador (Tercer parametro) => Metodologia de apuesta
    #instancias de jugador (Cuarto parametro) => A que apuesta
    j1 = Jugador('j1', 0, 1, 'par')
    j2 = Jugador('j2', 1, 1, 'impar')
    j3 = Jugador('j3', 0, 1, 'd-3')

    jugadores = [j1, j2, j3]

    for n in range(5):
        apuestas =[]
        # if j1.continua:
        for j in jugadores:
            apuestas.append(j.defineJuagda())
        r.tomarApuestas(apuestas)
        r.jugar(n)
        for j in jugadores:
            print(r.pagar())
            j.tomarGanancia(r.pagar())
          # else:
          #   print('ya no se juega')
          #   pass
    for j in jugadores:
        resultados.append(j.devolverResultados())
    print(resultados)

    plt.subplot(2, 2, 1)
    for r in range(len(resultados)):
        plt.plot(resultados[r][2], resultados[r][0], color=colores[r])
    plt.xlabel('n (numero de tiradas)')
    plt.ylabel('Apuestas')

    plt.subplot(2, 2, 2)
    for r in range(len(resultados)):
        plt.plot(resultados[r][2], resultados[r][1], color=colores[r])
    plt.xlabel('n (numero de tiradas)')
    plt.ylabel('Ganancias')

    plt.subplot(2, 2, 3)
    for r in range(len(resultados)):
        if len(resultados[r])>3:
            plt.plot(resultados[r][2], resultados[r][3], color=colores[r])
        else:
            pass
    plt.xlabel('n (numero de tiradas)')
    plt.ylabel('CAPITAL')

    plt.show()

main()
