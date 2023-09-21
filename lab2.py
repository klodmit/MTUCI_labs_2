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

# Задание 2 б Отобразить на экране изображение № j из папки NoTrees, если j < 50
path_first_image = 'C:\\Users\\dmitr\\PycharmProjects\\pythonProject\\Trees\\NoTrees\\' + no_trees_files[0]
io.imshow(path_first_image)
io.show()

# Задание 3 Создать массив параметров X для машинного обучения.
# Каждая компонента R,G,B каждого пикселя -- это отдельный параметр - столбец,
# каждое изображение -- строка.
x_data_no_trees_flat = [img.flatten() for img in x_data_no_trees]
x_datatrees_flat = [img.flatten() for img in x_datatrees]

# Объединить одномерные массивы в многомерный, где каждая строка X[i,:]-- это одномерный массив, полученный из i-го изображения.
X_no_trees = np.array(x_data_no_trees_flat)
X_trees = np.array(x_datatrees_flat)

# Проверим размерности полученных массивов
print('X_no_trees shape:', X_no_trees.shape)
print('X_trees shape:', X_trees.shape)

# Теперь у вас есть два массива X_no_trees и X_trees, которые представляют параметры для обучения модели.
# Вы можете объединить их в один массив X, если это необходимо.
X = np.vstack((X_no_trees, X_trees))
print('Общий X shape:', X.shape)

# Задание 3 а Превратить изображения в одномерные массивы параметров с помощью метода .flatten().
x_data_no_trees_flat = [img.flatten() for img in x_data_no_trees]
x_datatrees_flat = [img.flatten() for img in x_datatrees]

#Задание 3 .б Объединить одномерные массивы в многомерный, где каждая строка X[i,:]-- это одномерный массив, полученный из i-го изображения.
X = np.vstack((x_data_no_trees_flat, x_datatrees_flat))

#Задание 4 Создать массив результатов y, так, что элемент y[i,0] = 0, если строка X[i,:]
# соответствует изображению без деревьев, а y[i,0] = 1, если строка X[i,:] соответствует изображению с деревьями.
y_no_trees = np.zeros(len(x_data_no_trees))
y_trees = np.ones(len(x_datatrees))
y = np.concatenate((y_no_trees, y_trees)).reshape(-1, 1)

#Задание 5 Перемешать строки массивов X и y, сохранив соотношение из предыдущего пункта.
n = X.shape[0]
perm = np.random.permutation(n)
X = X[perm]
y = y[perm]

#Задание 6  Разделить наборы данных на 3 части: для обучения, для кроссвалидации, для тестирования:
# Если j заканчивается на 0-5: 60%, 20%, 20% соответственно
n_train = n // 10 * 6
n_cv = n // 10 * 2
n_test = n // 10 * 2

X_train = X[:n_train]
y_train = y[:n_train]

X_cv = X[n_train:n_train + n_cv]
y_cv = y[n_train:n_train + n_cv]

X_test = X[n_train + n_cv:]
y_test = y[n_train + n_cv:]

#Задание 7 Для каждой из трёх частей (обучение, кроссвалидация, тестирования) вывести первое изображение и напечатать на экране,
# есть ли на нём деревья.
# Чтобы из одномерного массива восстановить изображение, воспользоваться функцией reshape:
# img = np.reshape(X[i,:], (width, height,3))

def show_first_image(X, y, title):
    img = np.reshape(X[0], (64, 64, 3))
    io.imshow(img)
    io.show()
    label = "с деревьями" if y[0] == 1 else "без деревьев"
    print(f"Первое изображение {title}: {label}")

show_first_image(X_train, y_train, "для обучения")
show_first_image(X_cv, y_cv, "для кроссвалидации")
show_first_image(X_test, y_test, "для тестирования")