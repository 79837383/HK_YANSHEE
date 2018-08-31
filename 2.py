#!/usr/bin/python
# _*_ coding: utf-8 -*-
import time
import RobotApi
RobotApi.ubtRobotInitialize()
# ------------------------------Connect----------------------------------------
robotinfo = RobotApi.UBTEDU_ROBOTINFO_T()
# The robot name you want to connect
robotinfo.acName="Yanshee_438F"
ret=RobotApi.ubtRobotDiscovery("SDK", 15, robotinfo)
if (0!= ret):
    print ("Return value: %d" % ret)
    exit(1)

gIPAddr = robotinfo.acIPAddr
print gIPAddr
gIPAddr="127.0.0.1"

ret = RobotApi.ubtRobotConnect("SDK", "1", gIPAddr)

if (0 != ret):
    print ("Can not connect to robot %s" % robotinfo.acName)
    exit(1)
# ---------------------------Do one action-----------------------------------
#actionName = ['Forward','Hitleft','Hitright','Left slide tackle','reset','Right']
iRepeat=1
# for name in pcName:
actionName = "Hit left"
ret = RobotApi.ubtStartRobotAction(actionName, iRepeat)
if ret != 0:
    print("Can not start robot action! Error Code: %d" % ret)
    exit(3)  
    
# ---------------------------Disconnect--------------------------------------

RobotApi.ubtRobotDisconnect("SDK","1",gIPAddr)
RobotApi.ubtRobotDeinitialize()
