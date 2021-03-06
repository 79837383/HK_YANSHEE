 #!/usr/bin/python
# _*_ coding: utf-8 -*-
import time 
import RobotApi
 
RobotApi.ubtRobotInitialize() 
#------------------------------Connect----------------------------------
gIPAddr =""
robotinfo = RobotApi.UBTEDU_ROBOTINFO_T()
#The robot name you want to connect 
robotinfo.acName="Yanshee_438F"
ret = RobotApi.ubtRobotDiscovery("SDK", 15, robotinfo) 
if (0!= ret):
    print ("Return value: %d"% ret)
    exit(1)
gIPAddr = robotinfo.acIPAddr
ret = RobotApi.ubtRobotConnect("SDK", "1", gIPAddr)
if (0!= ret):
    print ("Can not connect to robot %s"% robotinfo.acName) 
    exit(1)
#---------------------------Read Sensor Value---------------------------
res = RobotApi.ubtSearchExtendSensor()
print res

environment_sensor = RobotApi.UBTEDU_ROBOTENV_SENSOR_T() 
while True:
    time.sleep(2)
    ret = RobotApi.ubtReadSensorValue("environment",environment_sensor ,12)
    if ret !=0:
        print("Can not read Sensor value. Error code: %d"% (ret)) 
    else:
        print("Read Environment Sensor tempValue: %d "% (environment_sensor.iTempValue))
        print("Read Environment Sensor HumiValue: %d " % (environment_sensor.iHumiValue))
        print("Read Environment Sensor PresValue: %d " % (environment_sensor.iPresValue))
#---------------------------Disconnect----------------------------------
RobotApi.ubtRobotDisconnect("SDK","1",gIPAddr)
RobotApi.ubtRobotDeinitialize()