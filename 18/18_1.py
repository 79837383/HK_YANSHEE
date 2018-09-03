#coding=utf-8
##############################################################
################Author: Xuyang Jie###########################
################Date: 14/03/2018##############################
##############################################################
import cv2
import numpy
import os
import struct


# save train/test images\par
def save_image(save_path,path):
    file = open(path,'rb')
    buf = file.read()
    file.close()
    index = 0
    magic,size,rows,cols = struct.unpack_from('>IIII',buf,index)
    index += struct.calcsize('>IIII')

    for i in range(size):
        temp = struct.unpack_from('>784B',buf,index)
        img_array = numpy.array(temp)
        img = img_array.reshape(28,28)
        cv2.imwrite(save_path + str(i) + '.jpg',img)
        index += struct.calcsize('>784B')

# load labels
def load_label(number,path,rand_index):
    file = open(path,'rb')
    buf = file.read()
    index = 0
    magic,size = struct.unpack_from('>II',buf,index)
    index += struct.calcsize('>II')
    temp_label = []
    label = numpy.zeros(len(rand_index))
    temp_label = struct.unpack_from('>' + str(size) + 'B',buf,index)
    #print len(temp_label)
    for counter in range(len(rand_index)):
        for i in range(len(temp_label)):
            if rand_index[counter] == i:
                label[counter] = temp_label[i]
                break
    return label


# pre_process, binarization\par
# No need to gray_scale the picture\par
def pre_process(load_path):
    img = cv2.imread(load_path)
    temp_gray_img = img
    gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    for x in range(28):
        for y in range(28):
            if gray_img[x,y] >= 127:
                gray_img[x,y] = 1
            else:
                gray_img[x,y] = 0
    return gray_img,temp_gray_img

# Load image
def load_image(name,number,load_path):
    imglist = []
    img_vec = numpy.zeros([number, 28 * 28],int)
    counter = 0
    index = numpy.random.randint(10000, size = number)
    for parent, dirname, files in os.walk(load_path):
        for file in files:
#print(load_path + file)\par
            #print(load_path +str(counter) + '.jpg')
            if name == 'test':
                pre_process_img,img = pre_process(load_path + str(index[counter]) + '.jpg')
            else:
                pre_process_img,img = pre_process(load_path + str(counter) + '.jpg')
            imglist.append(img)
            for rows in range(28):
                for cols in range(28):
                    img_vec[counter, rows * 28 + cols] = pre_process_img[rows,cols]
            counter += 1
            if counter == number:
                return img_vec,index,imglist