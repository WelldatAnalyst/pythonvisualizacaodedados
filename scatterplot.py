import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,3,7,1,0]

titulo = "Scatterplot: grafico de dispersão"
eixox = "Eixo X"
eixoy = "Eixoy"

plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.scatter(x ,y)
plt.plot(x,y)
plt.show()