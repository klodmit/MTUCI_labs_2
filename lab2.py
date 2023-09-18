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
print('x_data shape:', np.array(x_data_no_trees).shape)

X_datatrees = []
for files in range(len(trees_files)):
    path = 'C:\\Users\\dmitr\\PycharmProjects\\pythonProject\\Trees\\Trees\\' + trees_files[files]
    image = io.imread(path)
    X_datatrees.append(image)
print('x_data shape:', np.array(X_datatrees).shape)

# Задание 2 б Отобразить на экране изображение № j из папки NoTrees, если j < 50
path_first_image = 'C:\\Users\\dmitr\\PycharmProjects\\pythonProject\\Trees\\NoTrees\\' + no_trees_files[0]
io.imshow(path_first_image)
io.show()


#TODO Задание 3 Создать массив параметров X для машинного обучения.
# Каждая компонента R,G,B каждого пикселя -- это отдельный параметр - столбец,
# каждое изображение -- строка.


#TODO Задание 3 а Превратить изображения в одномерные массивы параметров с помощью метода .flatten().


#TODO Задание 3 .б Объединить одномерные массивы в многомерный, где каждая строка X[i,:]-- это одномерный массив, полученный из i-го изображения.


#TODO Задание 4 Создать массив результатов y, так, что элемент y[i,0] = 0, если строка X[i,:]
# соответствует изображению без деревьев, а y[i,0] = 1, если строка X[i,:] соответствует изображению с деревьями.

#TODO Задание 5 Перемешать строки массивов X и y, сохранив соотношение из предыдущего пункта.
# Если j нечётно: создать порядок перемешивания с помощью функции perm = np.random.permutation(n) и
# применить его к обоим массивам по типу: arr = arr[perm]


#TODO Задание 6  Разделить наборы данных на 3 части: для обучения, для кроссвалидации, для тестирования:
# Если j заканчивается на 0-5: 60%, 20%, 20% соответственно


#TODO Задание 7 Для каждой из трёх частей (обучение, кроссвалидация, тестирования) вывести первое изображение и напечатать на экране,
# есть ли на нём деревья.
# Чтобы из одномерного массива восстановить изображение, воспользоваться функцией reshape:
# img = np.reshape(X[i,:], (width, height,3))

