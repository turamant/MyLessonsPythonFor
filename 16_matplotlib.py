import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5, 6]
y = [i**2 for i in x]
plt.scatter(x, y, c='blue', marker='x', s=100)
plt.scatter(x, y, color='red', linewidths=2)

plt.xlabel('x data')
plt.ylabel('y data')
plt.title('Пример плоттера')
plt.show()