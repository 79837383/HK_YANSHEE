#! /usr/local/bin/python

import argparse
from subprocess import call
import time
import datetime
import RobotApi


# Calls the Espeak TTS Engine to read aloud a sentence
def text_to_speech(text):
    #	-ven+m7:	Male voice
    #  The variants are +m1 +m2 +m3 +m4 +m5 +m6 +m7 for male voices and +f1 +f2 +f3 +f4 which simulate female voices by using higher pitches. Other variants include +croak and +whisper.
    #  Run the command espeak --voices for a list of voices.
    #	-s180:		set reading to 180 Words per minute
    #	-k20:		Emphasis on Capital letters
    # call(" amixer set PCM 100 ", shell=True)	# Crank up the volume!

    cmd_start = " espeak -ven-us+m7 -a 200 -s180 -k20 --stdout '"
    cmd_end = "' | aplay"

    call([cmd_start + text + cmd_end], shell=True)


def main():
    text_to_speech("Hello! I am Yanshee!")

    RobotApi.ubtRobotInitialize()
    robotinfo = RobotApi.UBTEDU_ROBOTINFO_T()
    robotinfo.acName = "Yanshee_A21A"
    ret = RobotApi.ubtRobotDiscovery("SDK", 15, robotinfo)
    if (0 != ret):
        text_to_speech("Return value: " + str(ret))
        time.sleep(1)
    gIPAddr = robotinfo.acIPAddr

    # Connect to robot
    while True:
        # The robot name you want to connect
        ret = RobotApi.ubtRobotConnect("SDK", "1", gIPAddr)
        if (0 != ret):
            text_to_speech("Warning! Warning! Warning! Cannot connect to the robot")
        else:
            break

    while True:  # Read the sensors
        infrared_sensor = RobotApi.UBTEDU_ROBOTINFRARED_SENSOR_T()
        iAddr = [17]
        for Addr in iAddr:
            ret = RobotApi.ubtReadSensorValueByAddr("infrared", Addr, infrared_sensor, 4)  # Use ctypes size
            if ret != 0:
                text = "Can not read senor " + str(Addr) + " Error code " + str(ret)
            else:
                # text = "Sensor " + str(Addr) + " is              " + str(infrared_sensor.iValue) + "centimeter"
                text = "I have detected something " + str(infrared_sensor.iValue) + "centimeter ahead"
                print infrared_sensor.iValue
            text_to_speech(text)
            time.sleep(1)

    # ---------------------------Disconnect--------------------------------------
    RobotApi.ubtRobotDisconnect("SDK", "1", gIPAddr)
    RobotApi.ubtRobotDeinitialize()


if __name__ == '__main__':
    main()