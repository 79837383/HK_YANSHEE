#!/usr/bin/python
# _*_ coding: utf-8 -*-
from ctypes import *
#query gyro
class GYROSENSOR(Structure):
    _fields_ = [
    ("fValue", c_double*12)
    ]
if __name__=='__main__':
    print'''*********************'''
    ll = cdll.LoadLibrary
    api=ll("/mnt/1xrobot/lib/librobot.so")
    api.ubtRobotInitialize()
    api.ubtRobotConnect("sdk","1","127.0.0.1")
    pValue = pointer(GYROSENSOR())
    length = sizeof(GYROSENSOR)
    ret = api.ubtReadSensorValue("gyro",pValue,length)
if ret ==0:
    print"angle_x:",pValue[0].fValue[9]
    print"angle_y:",pValue[0].fValue[10]
    print"angle_z:",pValue[0].fValue[11]
else:
    print'Read mp9250 error!'
if pValue[0].fValue[9] >160or pValue[0].fValue[9] <-160:
    print'getup from fall back'
    api.ubtStartRobotAction("getup_in_back", 1)
elif pValue[0].fValue[9] >-20and pValue[0].fValue[9] <20:
    print'geup from fall front'
api.ubtStartRobotAction("getup_in_front", 1)
api.ubtRobotDisconnect("13825237954", "v1.2.3.0", "127.0.0.1")
api.ubtRobotDeinitialize()