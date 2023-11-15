import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from sklearn.cluster import KMeans

# Массив данных
X = np.array([[20, 20000],
              [21, 21000],
              [22, 20000],
              [23, 23000],
              [24, 26000],
              [25, 25500],
              [26, 27000],
              [27, 31000],
              [28, 32000],
              [29, 31000],
              [30, 55000],
              [31, 30000],
              [32, 26000],
              [33, 27000],
              [34, 37000],
              [35, 40000],
              [36, 33000],
              [37, 32560],
              [38, 25600],
              [39, 24500],
              [40, 41000],
              [41, 31000],
              [42, 50000],
              [43, 59000],
              [44, 30000],
              [45, 36560],
              [46, 38600],
              [47, 29500],
              [48, 60000],
              [49, 46000],
              [50, 30000]
])

# Выполняем кластеризацию методом к-средних
kmeans_model = KMeans(n_clusters=3, random_state=0)
kmeans_model.fit(X)
labels = kmeans_model.labels_
centroids = kmeans_model.cluster_centers_

# Визуализируем данные
fig, ax = plt.subplots()
ax.scatter(X[:, 0], X[:, 1], c=labels)
ax.scatter(centroids[:, 0], centroids[:, 1], marker='x', color='red')

# Добавляем прямоугольники
for i in range(3):
    cluster_points = X[labels == i]
    x_min, y_min = np.min(cluster_points, axis=0)
    x_max, y_max = np.max(cluster_points, axis=0)
    width = x_max - x_min + 1
    height = y_max - y_min + 1
    rect = Rectangle ((x_min,y_min), width, height, fill=False,
color='black',linewidth=2)
    ax.add_patch(rect)

ax.set_title('Кластеризация методом к-средних')
ax.set_xlabel('Возраст')
ax.set_ylabel('Зарплата')
ax.set_xlim(15,60)
ax.set_ylim(18000,70000)
plt.show()

