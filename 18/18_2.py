#coding=utf-8
##############################################################
################Author: Xuyang Jie###########################

################Date: 14/03/2018#############################
##############################################################
from project1_func import *
from sklearn.externals import joblib
from sklearn import neighbors
import time

# You need to refill the path according your file directory
train_image_path = 'E:/project/project/data/train-images.idx3-ubyte'
train_label_path = 'E:/project/project/data/train-labels.idx1-ubyte'
test_image_path = 'E:/project/project3/t10k-images.idx3-ubyte'
save_train_image_path = 'E:/project/project/train_image/'
save_test_image_path = 'E:/project/project/test_image/'
model_save_path = 'E:/project/project/train_model.mk1'


print 'Saving training images'
save_train_start = time.time()
save_image(save_train_image_path,train_image_path)
print('Finishing saving training images. Use time: %.2f' % (time.time() - save_train_start))


print 'Saving test images'
save_test_start = time.time()
save_image(save_test_image_path,test_image_path)
print('Finishing saving test images. Use time: %.2f' % (time.time() - save_test_start))


print 'Load train images'
load_train_start = time.time()
img_vec = load_image('train',60000,save_train_image_path)
print('Finishing loading training images. Use time: %.2f' % (time.time() - load_train_start))


print 'Load train labels'
load_train_label = time.time()
train_labels = load_label(60000,train_label_path)
print('Finishing loading training images. Use time: %.2f' % (time.time() - load_train_label))


#print labels[0:10]
print 'Training and saving model'
train_start = time.time()
knn = neighbors.KNeighborsClassifier(algorithm = 'kd_tree', n_neighbors = 3)
knn.fit(img_vec,train_labels)
joblib.dump(knn,model_save_path)
print('Finishing training and saving. Use time: %.2f' % (time.time() - train_start))