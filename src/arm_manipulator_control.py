import serial
import time
# Gripper code in arduino needs only desired angle
class Gripper:
    '''Class to control open and close position of gripper'''
    def __init__(self,port,rate,tOut,pauseTime=15,angleMax=180,angleMin=0,sizeMax=160,sizeMin=0):
        '''initialize with port name, baudrate and timeout for serial'''
        self.ser = serial.Serial('/dev/'+port,rate,timeout=tOut)
        self.rate = rate
        self.port = port
        self.serialTimeout = tOut
        self.angleMax = angleMax
        self.angleMin = angleMin
        self.sizeMax = sizeMax
        self.sizeMin = sizeMin
        self.open = self.angleMax
        self.grip = self.angleMin
        self.pauseTime = pauseTime

    def size2angle(self,fruitDimension):
        '''set the gripping angle based on the dimension of beet root'''
        self.grip = (self.angleMax - self.angleMin) * fruitDimension / float(self.sizeMax - self.sizeMin)

    def moveGripper(self,desiredAngle):
        '''Send desired angle to serial port'''
        desiredAngleStr = str(desiredAngle)+'\n'
        self.ser.write(desiredAngleStr.encode('utf-8'))
        print 'desired angle move',desiredAngle

    def gripTestMinMax(self):
        '''test minimum and maximum angle of gripper'''
        self.moveGripper(self.angleMax)
        time.sleep(self.pauseTime)
        self.moveGripper(self.angleMin)
        time.sleep(self.pauseTime)
        self.moveGripper(self.angleMax)

        
if __name__ == '__main__':
    gripper = Gripper('ttyACM0',9600,0.01)
    gripper.gripTestMinMax()
    # # print gripper.open
    # gripper.moveGripper(gripper.open)
    # print 'response open',gripper.ser.readline().rstrip('\r\n')
    # time.sleep(gripper.pauseTime)
    # gripper.moveGripper(gripper.grip)
    
    # print 'response grip',gripper.ser.readline().rstrip('\r\n')

    # gripper.gripTestMinMax()