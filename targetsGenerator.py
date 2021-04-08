import sys
import csv
import math
import numpy as np
from random import randrange, random

def writeCsv(fileName, points):
    with open(fileName, 'w') as csvFile:
        writer = csv.writer(csvFile, quoting=csv.QUOTE_NONE, delimiter='\n')
        for i in range(len(points)):    
            writer.writerow(points[i])

def toClose(X, Y, sampleBck, xn, r):
    for a in range(X - 1, X + 1):
        for o in range(Y - 1, Y + 1):
            if (sampleBck[a][o] != -1 and math.dist(sampleBck[a][o], xn) < r ):
                return True
    return False

def targetsGenerator(r=10, k=30):
    # taille du tableau r/sqrt(2)
    taille = r / math.sqrt(2)
    dimX = (1024/taille)-1
    dimY = (800/taille)-1
    sampleBck = [[-1 for x in range(int(dimX))] for y in range(int(dimY))] 
    x0 = (randrange(1, len(sampleBck)-1), randrange(1, len(sampleBck[0])-1))
    activeList = [x0]
    sampleBck[int(x0[0]/taille)][int(x0[1]/taille)] = x0


    while (len(activeList) > 0):
        xi = activeList[randrange(0, len(activeList))]
        for i in range(k):
            theta = (random() * 2 * math.pi)
            rang = r+random()*r
            xn = (xi[0] + math.cos(theta) * rang, xi[1] + math.sin(theta) * rang)

            X = int(xn[0]/taille)
            Y = int(xn[1] / taille)
            # print(X,Y)
            if (0 <= X < dimX and 0 <= Y < dimY):
                if (sampleBck[X][Y] == -1 and toClose(X,Y,sampleBck, xn, r) is False):
                    sampleBck[X][Y] = xn
                    activeList.append(xn)
                    # print("+++ =>",activeList)
                    break
            if (i == k - 1):
                activeList.remove(xi)
                # print("--- =>",activeList)
    for i in range(len(sampleBck)):
        for j in range(len(sampleBck[0])):
            print(sampleBck[i][j])
    return sampleBck
    
points = targetsGenerator()
# print(points)
writeCsv("test.csv", points)