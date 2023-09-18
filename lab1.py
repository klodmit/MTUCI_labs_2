import cv
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, data
from skimage.io import imread

plt.style.use('ggplot')
img = io.imread('https://upload.wikimedia.org/wikipedia/commons/8/82/UEIT_captured.jpg')
img_norm = io.imread('https://upload.wikimedia.org/wikipedia/commons/8/82/UEIT_captured.jpg')


# 1 Вывод размеров изображения
def showImageSize():
    print(img.shape[0])
    print(img.shape[1])


# 2 Вывод изображения
def showImage():
    plt.imshow(img[:, :, :], cmap="Greys")
    plt.show()


# 3 Создать негативное изображение
def showNegativeImage(im):
    height = len(im)
    width = len(im[0])
    for row in range(height):
        for col in range(width):
            red = 255 - im[row][col][0]
            green = 255 - im[row][col][1]
            blue = 255 - im[row][col][2]
            im[row][col] = [red, green, blue]
    io.imshow(im)
    io.show()


# 4 Создать копию фрагмента изображения
def createImageFragment(im):
    partial_img = im[115:230, 240:360, :]
    io.imshow(partial_img)
    io.show()
    


# 5 Отображаем красный в сером
def showReddedImage():
    R = img[:, :, 0]
    io.imshow(R)
    io.show()


# 6 Создать копию изображения по условию синий темнее, чем красный и зелёный суммарно каждый пункт должен быть отдельной функцией
def createImageCopyByIf(im):
    sum = 0
    height = len(im)
    width = len(im[0])
    for row in range(height):
        for col in range(width):
            red = im[row][col][0]
            green = im[row][col][1]
            blue = im[row][col][2]
            sum = int(red)+int(green)
            if int(blue) < sum:
                im[row][col] = [red, green, blue]
            else:
                im[row][col] = [0, 0, 0]
    io.imshow(im)
    io.show()


showImageSize()
showImage()
showNegativeImage(img)
createImageFragment(img_norm)
showReddedImage()
createImageCopyByIf(img_norm)
