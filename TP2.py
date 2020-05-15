import pandas as pd
from random import randint


class Metodos(object):

    def __init__(self, s, a, m, c):
        self.semilla = s
        self.a = a
        self.m = m
        self.c = c
        self.acumulaGCL = []
        self.acumulaC = []
        self.acumulaGCL.append(s)
        self.acumulaC.append(s)
        self.acC = []
        self.acGCL = []

        # arreglos para test
        self.paresGCL = []
        self.paresC = []

    def gcl(self):
        for i in range(self.m):
            y = (self.a * self.acumulaGCL[i]) % self.m
            self.acumulaGCL.append(y)
            self.acGCL.append(self.acumulaGCL[-1] / self.m)
        return self.acGCL

    def cuadrados(self):
        if int(len(str(self.semilla))) % 2 == 0:
            if len(str(self.semilla)) < self.c:
                print('Se requiere una semilla de mas de ', self.c, ' digitos')
            else:
                a = self.c / 2
                b = (self.c * 2) - a
                for i in range(self.m):
                    x = self.acumulaC[i] ** 2
                    while len(str(x)) < self.c * 2:
                        x = '0' + str(x)
                    self.acumulaC.append(int(str(x)[int(a):int(b):]))
                    self.acC.append(self.acumulaC[-1] / self.m)
            return self.acC
        else:
            print('Ingrese un numero de largo par, de ', self.c, ' digitos, para el metodo de cuadrados')

    def test_series(self, arrayGCL, arrayC):
        n = 5
        f_esp = (n-1)/n**2
        ejex = []
        ejey = []
        rC = {}
        rG = {}
        rR = {}
        rx = {}
        ry = {}
        nombres =[]
        for i in range(n):
            if i == 0:
                aux1 = 0
            else:
                aux1 = i/n
            aux2 = (i+1)/n
            nombrex = 'x'+ str(i)
            for j in range(n):
                nombrey = 'y'+ str(j)
                nombre = nombrex + nombrey
                rG[nombre] = 0
                rC[nombre] = 0
                rR[nombre] =0
                nombres.append(nombre)

            ny = 'y'+ str(i)
            ejex.append([aux1, aux2, nombrex])
            ejey.append([aux1, aux2, ny])
            rx[nombrex] = 0
            ry[ny] = 0

        random = []
        for i in range(self.m):
            random.append(randint(0,100)/100)

        paresRandom = []

        for i in range(int(len(arrayC) - 1)):
            self.paresC.append([arrayC[i], arrayC[i + 1]])

        for i in range(int(len(arrayGCL) - 1)):
            self.paresGCL.append([arrayGCL[i], arrayGCL[i + 1]])

        for i in range(int(len(random) - 1)):
            paresRandom.append([random[i], random[i + 1]])


        for par in self.paresC:
            for valx in ejex:
                if valx[0] <= par[0] < valx[1]:
                    rx[valx[2]] += 1
                    for valy in ejey:
                        if valy[0] <= par[1] < valy[1]:
                            ry[valy[2]] += 1
                            k = valx[2] + valy[2]
                            rC[k] = rC[k] + 1

        for par in self.paresGCL:
            for valx in ejex:
                if valx[0] <= par[0] < valx[1]:
                    rx[valx[2]] += 1
                    for valy in ejey:
                        if valy[0] <= par[1] < valy[1]:
                            ry[valy[2]] += 1
                            k = valx[2] + valy[2]
                            rG[k] = rG[k] + 1

        for par in paresRandom:
            for valx in ejex:
                if valx[0] <= par[0] < valx[1]:
                    for valy in ejey:
                        if valy[0] <= par[1] < valy[1]:
                            k = valx[2] + valy[2]
                            rR[k] = rR[k] + 1
        xo2R = 0
        xo2C = 0
        xo2G =0
        for j in nombres:
            xo2R += (((n-1) - rR[j])**2)/(n-1)
            xo2C += (((n-1) - rC[j])**2)/(n-1)
            xo2G += (((n-1) - rG[j])**2)/(n-1)


        print('tamanio random', len(paresRandom))
        print('tamanio gC', len(self.paresC))
        # print(self.paresC)
        # print(self.paresGCL)
        print(random)
        print(paresRandom)
        print('xo2R', xo2R)
        print('xo2C', xo2C)
        print('xo2G', xo2G)
        # print(ejex)
        # print(ejey)
        print('esperado: ', f_esp)
        print('test cudadrados', rC)
        print('test Congruencial', rG)
        print('random', rR)


def main():
    mgcl = Metodos(52, 6, 100, 2)
    # d = {'GCL': mgcl.gcl(), 'Cuadrados': mgcl.cuadrados()}
    # df = pd.DataFrame(data=d)
    # print(df)
    mgcl.test_series(mgcl.gcl(), mgcl.cuadrados())


main()

#bivliografia de utilidad https://es.slideshare.net/hectorperez923/prueba-de-series-exposicin
