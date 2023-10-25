from hub import light_matrix, motion_sensor, port, sound
import motor,motor_pair, runloop, math
from motor import BRAKE, HOLD
from motor_pair import move_tank, move_tank_for_degrees, stop


def init():
    ##Initialize motors and sensors
    motor_pair.unpair(motor_pair.PAIR_1)
    motor_pair.pair(motor_pair.PAIR_1,port.C,port.A)
    motion_sensor.set_yaw_face(motion_sensor.FRONT)
    motion_sensor.reset_yaw(0)
    sound.volume(100)
    #moveSpeed = 1000
    #inch2Degree = 26
    #tail = motor



async def moveForward(distance):
    '''
    purpose: Move Forward
    distance: distance in inches
    '''
    if distance is None:
        return

    '''
    inch= degree
    14=360
    7=180
    1=26
    '''
    light_matrix.write("F")
    degrees = distance * 26
    #await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 360, 500, 500)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, degrees, 700, 700)
    motor_pair.stop(motor_pair.PAIR_1)
    #await motor_pair.move_for_time(motor_pair.PAIR_1,5000,0,velocity=1000,acceleration=500)
    #motor_pair.move_tank(motor_pair.PAIR_1, 100, 100)


    #await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, -360, 500, 500)
    #await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, -180, 500, 500)
    sound.beep()

async def moveBackward(distance):
    '''
    purpose: Move backward
    distance: distance in inches
    '''
    await light_matrix.write("B")
    degrees = -distance * 26
    #await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 360, 500, 500)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, degrees, 700, 700)
    motor_pair.stop(motor_pair.PAIR_1)
    sound.beep()
async def moveBackwardFast(distance):
    '''
    purpose: Move backward
    distance: distance in inches
    '''
    await light_matrix.write("B")
    degrees = -distance * 26
    #await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 360, 500, 500)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, degrees, 1000, 1000)
    motor_pair.stop(motor_pair.PAIR_1)
    sound.beep()

async def turnLeft(degrees):
    '''
    purpose: Turn robot left
    degrees: 1 to 360 in increments of 1
    '''
    if degrees is None:
        return

    '''
    DIRECTION: L or R
    DEGREES: 1 TO 360 degrees

    turn = wheel turn
    180 = 296
    90= 148
    45= 74
    1 degree turn = 0.61 degrees wheel turn.
    '''
    #LEFT
    await light_matrix.write("L")
    turnDegrees = degrees * 1.6444
    turnDegrees = math.ceil(turnDegrees)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, turnDegrees, -200, 200)
    sound.beep()
    #await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 296, -200, 200)

    #if direction == "LEFT":
    #    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 360, -200, 200)
    #RIGHT
    #if direction == "RIGHT":
    #    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, -360, -200, 200)
    #await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 74, -200, 200)

async def turnRight(degrees):
    '''
    purpose: turn robot right
    degrees: 1 to 360 in increments of 1
    '''
    if degrees is None:
        return

    '''
    180 = 296
    90= 148
    45= 74
    '''
    await light_matrix.write("R")
    turnDegrees = degrees * 1.6444
    print (turnDegrees)
    turnDegrees = math.ceil(turnDegrees) *-1
    print (turnDegrees)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, turnDegrees, -200, 200)

    #RIGHT
    #motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, -148, -200, 200)

async def armUp():
    '''
    Purpose:Lift up Arm
    degrees: 1 to 360
    speed: 100 to 1000
    '''
    print ('arm up')
    await motor.run_for_degrees(port.B, 360, 720)


async def armUpByAngle(angle):
    '''
    Purpose:Lift up Arm
    degrees: 1 to 360
    speed: 100 to 1000
    '''
    print ('arm up')
    await motor.run_for_degrees(port.B, angle, 720, acceleration=10000)

async def armDown():
    '''
    Purpose:Lift up Arm
    degrees: 1 to 360
    speed: 100 to 1000
    '''
    print ('arm down')
    await motor.run_for_degrees(port.B, -360, 1000, acceleration=10000)

async def armDownByAngle(angle):
    '''
    Purpose:Lift up Arm
    degrees: 1 to 360
    speed: 100 to 1000
    '''
    print ('arm down')
    await motor.run_for_degrees(port.B, -angle, 1000, acceleration=10000)

async def armDownByAngle_slow(angle):
    '''
    Purpose:Lift up Arm
    degrees: 1 to 360
    speed: 100 to 1000
    '''
    print ('arm down')
    await motor.run_for_degrees(port.B, -angle, 1000, acceleration=2050)


async def tailUp():
    '''
    Purpose:Lift up Arm
    degrees: 1 to 360
    speed: 100 to 1000
    '''
    print ('tail up')
    await motor.run_for_degrees(port.E, 360, 720)




async def tailDown():
    '''
    Purpose:Lift up Arm
    degrees: 1 to 360
    speed: 100 to 1000
    '''
    print ('tail Down')
    await motor.run_for_degrees(port.E, -360, 720)



'''
MISSIONS START
'''


#Mission 09
async def rollingCamera2():
    await armDown()
    await moveForward(19)
    await moveBackward(15) 
    await turnRight(90)
    await armUp()





#Mission 10
async def lights():
    await armUp()
    await moveForward(33)
    await turnRight(20)
    await moveForward(2)
    await armDownByAngle(90)
    await turnLeft(21)
    await armUp()

    #Mission 11
async def dj():
    await moveBackward(14)
    await turnLeft(50)
    await moveForward(19)
    await turnRight(90)
    await moveForward(7)

    #Mission 12
async def sounds():
    await moveBackward(8)
    await turnLeft(39)
    await moveForward(6)
    await armDownByAngle_slow(330)
    await armUpByAngle(130)
    await armDownByAngle_slow(345)
    await armUpByAngle(130)
    await armDownByAngle_slow(450)
    await armUp()
    await moveBackward(5)
    await turnRight(26)
    await armDown()
    await moveForward(4)
    await armUpByAngle(400)
    await turnLeft(7)
    await moveForward(1)
    await armDown()

    #await turnRight(11)
    #await moveForward(5)
    #await armUp()
    #await turnLeft(10)
    #await moveForward(2)
    #await armDown()

    #side mission
async def comehome():
    await turnLeft(20)
    await moveBackwardFast(39)

    #Misson 13
async def masterpiece():
    await armDown()
    await moveForward(22)
    await turnLeft(60)
    await moveForward(38)
    await turnRight(20)
    await moveBackward(7)
    await turnLeft(45)
    await armUp()
    await moveBackward(20)
    await turnRight(90)
    await moveBackwardFast(33)

    #Mission 14
async def printer():
    await armUp()
    await moveForward(20)
    await moveBackwardFast(24)
    
    
    




    
    


'''
MISSIONS END
'''

async def main():
    # write your code here
    init()
    #await rollingCamera2()
    await lights()
    await dj()
    await sounds()
    await comehome() 
    #await masterpiece()
    #await printer()
    #await turnRight(90)
    #await Mission_3DCinema()
    #await mission_SoundMixer()
    #motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, -500, 1000, 1000)
    #motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 500, 1000, 1000)
    #await moveForward(12)
    #await moveBackward(5)
    #await turnRight(180)
    #await turnLeft(180)
    #await turnLeft(90)


    ##Robot initial position

    #await tailDown()



    #await motor.run_for_degrees(port.B, 360, 720)
    #await motor.run_for_degrees(port.E, 360, 720)
    #await motor.run_for_degrees(port.B, -360, 720)
    #await motor.run_for_degrees(port.E, -360, 720)


runloop.run(main())
