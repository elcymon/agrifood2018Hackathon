import serial
import time
# Gripper code in arduino needs only desired angle
class Gripper:
    '''Class to control open and close position of gripper'''
    def __init__(self,port,rate,tOut):
        '''initialize with port name, baudrate and timeout for serial'''
        self.ser = serial.Serial('/dev/'+port,rate,timeout=tOut)
        self.rate = rate
        self.port = port
        self.serialTimeout = tOut

    def open(desiredAngle):
        '''Send desired angle to serial port'''
        desiredAngleStr = str(desiredAngle)
        ser.write(desiredAngleStr.encode('utf-8'))
        
