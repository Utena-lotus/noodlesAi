from PIL import Image
import os, glob
import numpy as np
from sklearn import model_selection

classes = ['friednoodles', 'Pasta', 'Ramen']
numClasses = len(classes)
imageSize = 50

#　画像の読み込み

X = []
Y = []
for index, classlabel in enumerate(classes):
    photos_dir = '/Users/ngc7293/Desktop/NoodlesAi/' + classlabel
    files = glob.glob(photos_dir + '/*.jpg')
    for i, file in enumerate(files):
        if i >= 100: break
        image = Image.open(file)
        image = image.convert('RGB')
        image = image.resize((imageSize, imageSize))
        data = np.asarray(image)
        X.append(data)
        Y.append(index)

X = np.array(X)
Y = np.array(Y)

x_train, x_test, y_train, y_test = model_selection.train_test_split(X, Y)
xy =(x_train, x_test, y_train, y_test)
print(x_train)
# np.save('./noodles.npy', xy)
