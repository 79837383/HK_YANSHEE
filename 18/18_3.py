#coding=utf-8
#############################################################

################Author: Xuyang Jie###########################

################Date: 14/03/2018#############################

##############################################################
from project1_func import *
from sklearn.externals import joblib
from sklearn import neighbors
import time
import sys

# You need to resign the path according your file directory
test_label_path = 'E:/project/project/data/t10k-labels.idx1-ubyte'
save_test_image_path = 'E:/project/project/test_image/'
model_save_path = 'E:/project/project/train_model.mk1'

print 'knn loading'
load_model_start = time.time()
knn = joblib.load(model_save_path)
print('Finishing loading. Use time: %.2f' % (time.time() - load_model_start))

print 'Loading test image'
load_start = time.time()
image_vec, rand_index, img = load_image('test',int(sys.argv[1]),save_test_image_path)
print('Finishing loading images. Use time: %.2f' % (time.time() - load_start))
#print len(rand_index)
#print rand_index

print 'Loading test labels'
load_label_start = time.time()
labels = load_label(int(sys.argv[1]),test_label_path,rand_index)
print('Finishing loading labels. Use time: %.2f' % (time.time() - load_label_start))
#print(len(labels))
#print labels

#print labels[0:10]\par
print 'Predict'
predict_start = time.time()
result = knn.predict(image_vec)
print('Finishing prediction. Use time: %.2f' % (time.time() - predict_start))

true_num = 0
for i in range(len(result)):
	res = cv2.resize(img[i],(240,180),interpolation = cv2.INTER_CUBIC)
	cv2.putText(res,'Predict:' + str(result[i]),(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0),1)
	cv2.imshow('Digits-Recognition',res)
	cv2.waitKey(0)
	if result[i] == labels[i]:
		true_num += 1
    #print('Predict number is %d. Actual number is %d.' % (result[i],labels[i]))
    #time.sleep(0.5)
print('true_num: %d' % true_num)
accuracy = float(true_num/100)
print('Accuracy: %.2f' % (accuracy * 100))