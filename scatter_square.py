import matplotlib.pyplot as plt 

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, s=40)

#Define o titulo do gráfico e nomeia os eixos
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=24)

#Define o tamano dos rótulos das marcações
plt.tick_params(axis='both', which='major', labelsize=14)

#Define o intervalo para cada eixo
plt.axis([0, 1100, 0,1100000])

plt.show()