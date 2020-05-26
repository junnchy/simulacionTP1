import matplotlib.pyplot as plt

def resultados():
    res = []
    r = [[1000, 1, 0]]
    res.append(r)


    for i in range(10):
        aux = []
        for j in res[i]:
            nc1 = j[0] + j[1]
            na1 = j[1]
            nc2 = j[0] - j[1]
            na2 = j[1] * 2
            aux.append([nc1, na1, i+1])
            aux.append([nc2, na2, i+1])
        res.append(aux)

    # for r in res:
    #     print(r)
    #     print(len(r))

    for r in res:
        print('-------------------')
        aux = []
        num = []
        j = 0
        g = 0
        p = 0
        for c in r:
            if c[0] not in aux:
                aux.append(c[0])
                j += 1
            num.append(j)
            if c[0] >= 1000:
                g += 1
            else:
                p += 1
        aux.sort()
        print(aux)
        print('Cantidad de Resultados distintos: ', len(aux))
        print('Cantidad de Resultados positivos: ', g)
        print('Cantidad de Resultados Negativos; ', p)
        #
        # plt.plot()
        # plt.title('Martingala: Analisis de Resultados')
        # plt.xlabel('Capital Posible')
        # plt.ylabel('Cantidad de Resultados')
        # plt.plot(num, aux, color='darkblue')
        # plt.axhline(1000, color='r', linestyle='-')
        # plt.show()
        #
        #
        # labels = 'Positivos', 'Negativos'
        # sizes = [g, p]
        # explode = (0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
        # fig1, ax1 = plt.subplots()
        # ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%')
        # plt.suptitle('Martingala: Analisis de Resultados')
        # plt.show()



resultados()
