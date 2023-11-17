import matplotlib.pyplot as plt

dados = open("populacao_brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[0]))

plt.plot(x,y)
plt.title("Crescimento populacional no Brasil 1981-2016")
plt.xlabel("Ano")
plt.ylabel("Popoulação x100.000.000")
plt.show()

