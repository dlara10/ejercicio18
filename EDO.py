import numpy as num
import matplotlib.pyplot as plt

datos = num.loadtxt('dat2.txt')

x  = datos[:,0]
y = datos[:,1]
z = datos[:,2]

h = 0.1
N = 10/h
x1 = num.linspace(0, 10, N)
y1 = num.cos(x1)

plt.figure()
plt.scatter(x, y)
plt.plot(x1, y1)
plt.savefig('grafica2.pdf')
