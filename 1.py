# _*_ coding: utf-8 -*-
import time
import RobotApi
RobotApi.ubtRobotInitialize()
# ------------------------------Connect----------------------------------
gIPAddr ="127.0.0.1"
robotinfo = RobotApi.UBTEDU_ROBOTINFO_T()
ret = RobotApi.ubtRobotConnect("SDK", "1", gIPAddr)
if (0 != ret):
    print ("Can not connect to robot %s" % robotinfo.acName)
    exit(1)

#robotinfo2 = RobotApi.UBTEDU_ROBOTINFO_T()
#print robotinfo.acName
# --------------------------Test servo 17-------------------------------
servoinfo = RobotApi.UBTEDU_ROBOTSERVO_T()
# 在这里填写你希望头部舵机转到的角度
servoinfo.SERVO17_ANGLE = 60  #head
ret = RobotApi.ubtSetRobotServo(servoinfo, 20)
time.sleep(2)



# 回到默认 90 度位置
servoinfo.SERVO17_ANGLE = 90
ret = RobotApi.ubtSetRobotServo(servoinfo, 20)
# --------------------------DisConnection---------------------------------
RobotApi.ubtRobotDisconnect("SDK", "1", gIPAddr)
RobotApi.ubtRobotDeinitialize()
