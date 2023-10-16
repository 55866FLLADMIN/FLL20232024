from hub import light_matrix, port, motion_sensor, sound
import motor_pair
import motor
import runloop
import math

def init():
    motor_pair.unpair(motor_pair.PAIR_2)
    motor_pair.pair(motor_pair.PAIR_2,port.E,port.F)
    motion_sensor.set_yaw_face(motion_sensor.FRONT)
    motion_sensor.reset_yaw(0)
    sound.volume(100)
    moveSpeed = 1000


async def moveForward(distance):
    '''
    Make the base turn at an angle by degrees provided. 
    '''
    print ('move Forward')
    degrees = distance * 26 * 2
    # 26:           for amount of degrees to rotate the wheels to move by 1/2 inch with small wheel
    # degrees * 2: when using the small wheel, you have to double the rotations to move by 1 inch.
    # 26 for aomut of degrees to rotate the wheels to move by 1 inch with "big wheel"
    print (degrees)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_2, -degrees, 700, 700)
    motor_pair.stop(motor_pair.PAIR_2)

async def moveBackward(distance):
    print ('move Backward')
    degrees = distance * 26 * 2
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_2, degrees, 700, 700)
    motor_pair.stop(motor_pair.PAIR_2)


async def turnRight(degrees):
    print ('turnRight')
    await light_matrix.write("R")
    #turnDegrees = degrees * 1.6444
    turnDegrees = degrees * 0.822 # 1.644/2 = 0.822
    turnDegrees = math.ceil(turnDegrees) *-1
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_2, 360, -1000, 1000,stop=motor.HOLD)

async def turnLeft(degrees):
    print ('turnLeft')
    await light_matrix.write("L")
    turnDegrees = degrees * 1.6444
    turnDegrees = math.ceil(turnDegrees)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_2, 360, -1000, 1000,stop=motor.HOLD)


async def draw_Circle1():
    print ('Drawing circle')
    for x in range(360):
        await moveForward(.1)
        await turnRight(1)


async def draw_Circle(radius):
    print ('Drawing circle')

async def draw_Square():
    print ('Drawing Square')


async def main():
    # write your code here
    init()
    await light_matrix.write("Hi!")
    await moveBackward(10)

    await moveForward(10)
    #await turnLeft(4010)
    await draw_Circle1()
    #await moveBackward(10)
    #await turnLeft(45)
    #await turnRight(180)

runloop.run(main())
