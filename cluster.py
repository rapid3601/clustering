import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from sklearn.cluster import KMeans

#Массив данных
X = np.array([[20, 20000],
              [21, 21000],git
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
              [35, 40000]
             ])