j = 1
print(j % 5 + 1)

import numpy as np
from skimage import io
import os

# Задание 1 Составить список файлов в каждой папке
no_trees_files = os.listdir('Trees\\NoTrees')
trees_files = os.listdir('Trees\\Trees')

# Задание 2 а Создать список из массивов numpy с изображениями для каждой папки.
x_data_no_trees = []
for files in range(len(no_trees_files)):
    path = 'C:\\Users\\dmitr\\PycharmProjects\\pythonProject\\Trees\\NoTrees\\' + no_trees_files[files]
    image = io.imread(path)
    x_data_no_trees.append(image)
print('x_data_no_trees shape:', np.array(x_data_no_trees).shape)

x_datatrees = []
for files in range(len(trees_files)):
    path = 'C:\\Users\\dmitr\\PycharmProjects\\pythonProject\\Trees\\Trees\\' + trees_files[files]
    image = io.imread(path)
    x_datatrees.append(image)
print('x_datatrees shape:', np.array(x_datatrees).shape)