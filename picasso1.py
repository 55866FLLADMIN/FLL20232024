from hub import light_matrix, motion_sensor, port, sound
import motor,motor_pair, runloop, math
from motor import BRAKE, HOLD, run
from motor_pair import move_tank, move_tank_for_degrees, stop
import color_sensor
import color 


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

async def moveForwardSlow(distance):
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
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, degrees, 700, 700, acceleration=750)
    motor_pair.stop(motor_pair.PAIR_1)
    #await motor_pair.move_for_time(motor_pair.PAIR_1,5000,0,velocity=1000,acceleration=500)
    #motor_pair.move_tank(motor_pair.PAIR_1, 100, 100)


    #await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, -360, 500, 500)
    #await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, -180, 500, 500)
    sound.beep()

async def moveForwardByHalf(distance):
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
    degrees = distance * 13
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
 
async def moveBackward_byQuarterInch(distance):
    '''
    purpose: Move backward
    distance: distance in inches
    '''
    await light_matrix.write("B")
    degrees = -distance * 6
    #await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 360, 500, 500)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, degrees, 700, 700)
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

async def armUpFast():
    '''
    Purpose:Lift up Arm
    degrees: 1 to 360
    speed: 100 to 1000
    '''
    print ('arm up')
    await motor.run_for_degrees(port.B, 360, 720, acceleration=10000)


async def armUpByAngle(angle):
    '''
    Purpose:Lift up Arm
    degrees: 1 to 360
    speed: 100 to 1000
    '''
    print ('arm up')
    await motor.run_for_degrees(port.B, angle, 720)

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


async def tailUp():
    '''
    Purpose:Lift up Arm
    degrees: 1 to 360
    speed: 100 to 1000
    '''
    print ('tail up')
    await motor.run_for_degrees(port.E, 360, 720)

async def tailUpByAngle(angle):
    '''
    Purpose:Lift up Arm
    degrees: 1 to 360
    speed: 100 to 1000
    '''
    print ('tail up')
    await motor.run_for_degrees(port.E,angle, 360, 720)



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
    await turnRight(18)
    await moveForward(2)
    await armDownByAngle(100)
    await turnLeft(21)
    await armUp()

    #Mission 11
async def dj():
    await moveBackward(14)
    await turnLeft(50)
    await moveForward(19)
    await turnRight(90)
    await moveForwardSlow(8)
 
    #Mission 12
async def sounds():
    await moveBackward(8)
    # while color_sensor.color(port.D) != color.BLACK or color_sensor.color(port.F) != color.BLACK:
    #     await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 10, 10, 10)
    # motor_pair.stop(motor_pair.PAIR_1)
    #await moveBackward_byQuarterInch(1)
    # await runloop.sleep_ms(10000)
    await turnLeft(18)
    await armDown()
    #await turnRight(10)
    await moveForward(4)
    await moveForwardByHalf(1)
    await armUpFast()
    await armDownByAngle(110)
    await turnLeft(9)
    #await moveForward(2)
    await armDown()

    #side mission
async def comehome():
    await turnLeft(30)
    await moveBackward(39)

    #Misson 13
async def masterpiece():
    await armDown()
    await moveForward(25)
    await turnLeft(69)
    await moveForwardSlow(38)
    await turnRight(25)
    await moveBackward(3)
    await turnLeft(45)
    await moveBackward(2)
    await armUp()
    await moveForward(7)
    await turnRight(80)
    await tailDown()

    #Misson 13
async def lighttower():
    await moveBackward(45)
    await turnRight(90)
    await tailUp()
    await moveBackward(8)

    




    "missions ends"




async def main():
    # write your code here
    init()
    
    #await rollingCamera2()
    await lights()
    await dj()
    await sounds()
    await comehome()
    #await masterpiece()
    #await lighttower()
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
