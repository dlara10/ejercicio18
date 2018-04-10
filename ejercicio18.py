import numpy as num
import matplotlib.pyplot as plt

datos = num.loadtxt('dat.txt')

x  = datos[:,0]
y = datos[:,1]
z = num.exp(x)


plt.figure()
plt.scatter(x, y)
plt.plot(x, z)
plt.savefig('Funcion ex')
