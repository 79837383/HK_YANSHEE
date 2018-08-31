#!/usr/bin/python
 # _*_ coding: utf-8 -*-
from ctypes import *
class GYROSENSOR(Structure):
     _fields_ = [
     ("fValue", c_double*12)
     ]
     
if __name__=='__main__':
    print'''*********************'''
    ll = cdll.LoadLibrary
    api=ll("/mnt/1xrobot/lib/librobot.so")
    api.ubtRobotInitialize()
    api.ubtRobotConnect("sdk","v1","127.0.0.1")
    pValue = pointer(GYROSENSOR())
    length = sizeof(GYROSENSOR)
    ret = api.ubtReadSensorValue("gyro",pValue,length)
if ret ==0:
    print"angle_x:",pValue[0].fValue[9]
    print"angle_y:",pValue[0].fValue[10]
    print"angle_z:",pValue[0].fValue[11]
else:
    print'Read mp9250 error!'
api.ubtRobotDisconnect("sdk", "v1", "127.0.0.1")
 