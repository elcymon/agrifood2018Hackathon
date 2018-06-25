import serial
import time
# Gripper code in arduino needs only desired angle
class Gripper:
    '''Class to control open and close position of gripper'''
    def __init__(self,port,rate,tOut):
        '''initialize with port name, baudrate and timeout for serial'''
        self.ser = serial.Serial('/dev/'+port,rate,timeout=tOut,angleMax=180,angleMin=0,sizeMax=160,sizeMin=0)
        self.rate = rate
        self.port = port
        self.serialTimeout = tOut
        self.angleMax = angleMax
        self.angleMin = angleMin
        self.sizeMax = 160
        self.sizeMin = 0
        self.open = self.angleMax
        self.grip = self.angleMin

    def size2angle(fruitDimension):
        '''set the gripping angle based on the dimension of beet root'''
        self.grip = (self.angleMax - self.angleMin) * fruitDimension / float(self.sizeMax - self.sizeMin)

    def moveGripper(desiredAngle):
        '''Send desired angle to serial port'''
        desiredAngleStr = str(desiredAngle)
        ser.write(desiredAngleStr.encode('utf-8'))

    def gripTestMinMax():
        '''test minimum and maximum angle of gripper'''
        self.moveGripper(self.angleMax)
        time.sleep(10)
        self.moveGripper(self.angleMin)
        time.sleep(10)
        self.moveGripper(self.angleMax)

        
if __name__ == '__main__':
    gripper = Gripper('ttyACM0',115200,0.01)
    gripper.moveGripper(gripper.open)
    time.sleep(10)
    gripper.moveGripper(gripper.grip)

    # gripper.gripTestMinMax()