import pandas as pd
import openpyxl
import clipboard as clp

class Metodos(object):

    def __init__(self, s, a ,m, c):
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


    def gcl(self):
        for i in range(self.m -1):
            y = self.a * self.acumulaGCL[i] % self.m
            self.acumulaGCL.append(y)
            self.acGCL.append(self.acumulaGCL[-1]/self.m)
        return self.acGCL

    def cuadrados(self):
        if int(len(str(self.semilla))) % 2 == 0:
            if len(str(self.semilla)) < self.c:
                print ('Se requiere una semilla de mas de ', self.c, ' digitos')
            else:
                a = self.c / 2
                b = (self.c * 2) - a
                for i in range(self.m -1):
                    x = self.acumulaC[i]**2
                    while len(str(x)) < self.c*2:
                        x = '0' + str(x)
                    self.acumulaC.append(int(str(x)[int(a):int(b):]))
                    self.acC.append(self.acumulaC[-1]/self.m)
            return self.acC
        else:
            print('Ingrese un numero de largo par, de ', self.c, ' digitos, para el metodo de cuadrados')


def main():
    mgcl = Metodos(52, 6, 100, 2)
    # print(mgcl.gcl())
    # print(mgcl.cuadrados())
    d = {'GCL': mgcl.gcl(), 'Cuadrados': mgcl.cuadrados()}
    df = pd.DataFrame(data=d)
    print(df)


main()




