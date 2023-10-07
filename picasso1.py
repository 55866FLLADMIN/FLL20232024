from hub import light_matrix, motion_sensor, port, sound
import motor,motor_pair, runloop, math
from motor import BRAKE, HOLD
from motor_pair import move_tank, move_tank_for_degrees, stop


def init():
    ##  Initialize motors and sensors
    motor_pair.unpair(motor_pair.PAIR_1)
    motor_pair.pair(motor_pair.PAIR_1,port.D,port.F)
    motion_sensor.set_yaw_face(motion_sensor.FRONT)
    motion_sensor.reset_yaw(0)
    sound.volume(100)
    moveSpeed = 1000
    inch2Degree = 26



async def moveForward(distance):
    '''
    purpose: Move Forward
    distance: distance in inches
    '''
    if distance is None:
        return

    '''
    inch= degree
    14  =   360 
    7   =   180
    1   =   26
    '''
    light_matrix.write("F")
    degrees = distance * 26
    #await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 360, 500, 500)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, degrees, 1000, 1000)
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
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, degrees, 1000, 1000)
    motor_pair.stop(motor_pair.PAIR_1)
    sound.beep()

async def turnLeft(degrees):
    '''
    degrees: ??
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
    #await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 296, -200, 200)

    #if direction == "LEFT":
    #    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 360, -200, 200)
    #RIGHT
    #if direction == "RIGHT":
    #    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, -360, -200, 200)
    #await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 74, -200, 200)

async def turnRight(degrees):
    '''
    degrees: 1 to 360 in increments of 10
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


async def main():
    # write your code here
    init()

    await moveForward(12)
    await moveBackward(5)
    #await turnRight(180)
    #await turnLeft(180)
    await turnLeft(90)

    await motor.run_for_degrees(port.B, 360, 720)
    await motor.run_for_degrees(port.E, 360, 720)
    await motor.run_for_degrees(port.B, -360, 720)
    await motor.run_for_degrees(port.E, -360, 720)



runloop.run(main())
