from hub import light_matrix, port, motion_sensor, sound
import motor_pair
import motor
import runloop
import math
from hub import motion_sensor

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
    print ('Moving Forward')
    degrees = distance * 26 * 2
    # 26:           for amount of degrees to rotate the wheels to move by 1/2 inch with small wheel
    # degrees * 2: when using the small wheel, you have to double the rotations to move by 1 inch.
    # 26 for aomut of degrees to rotate the wheels to move by 1 inch with "big wheel"
    print (degrees)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, -degrees, 100, 100)
    motor_pair.stop(motor_pair.PAIR_1)

async def moveBackward(distance):
    print ('Moving Backward')
    degrees = distance * 26 * 2
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, degrees, 700, 700)
    motor_pair.stop(motor_pair.PAIR_1)


async def turnRight(degrees):
    print ('Turning Right')
    await light_matrix.write("R")
    '''
        if 534 degrees wheel rotation = 360 degree real turn
        90 degree turn = (534*90)/360
    '''
    #turnDegrees = degrees * 1.6444
    turnDegrees = (534* degrees)/360 # 1.644/2 = 0.822
    turnDegrees = math.ceil(turnDegrees) *-1
    print (degrees)
    print (turnDegrees)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 360, -1000, 1000,stop=motor.HOLD)

async def turnLeft(degrees):
    print ('Turning Left')
    await light_matrix.write("L")
    turnDegrees = degrees * 1.6444
    turnDegrees = math.ceil(turnDegrees)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_2, 360, -1000, 1000,stop=motor.HOLD)

async def draw_Circle1():
    print ('Drawing circle')
    for x in range(360):
        await moveForward(.1)
        await turnRight(1)


async def draw_FullCircle():
    '''
    534 wheel turn = 360 actual turn on paper
    '''
    print ('Drawing FULL circle')
    motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 536, -100, 100)


async def turn90():
    '''
        if 534 degrees wheel rotation = 360 degree real turn
        90 degree turn = (534*90)/360 = 133.5
    '''
    print ('90 degree turn')
    motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 134, -1000, 1000)



async def draw_Circle(radius):
    '''
    534 wheel turn = 360 actual turn on paper
    '''
    print ('Drawing circle')
    for x in range(10):
        await moveForward(.5)
        await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 53, -100, 100)

async def draw_Square(length):
    print ('Drawing Square')
    #await turnRight(90)
    #await turn90()
    await moveForward(length)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 134, -100, 100)
    await moveForward(length)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 134, -100, 100)
    await moveForward(length)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 134, -100, 100)
    await moveForward(length)

async def draw_Triangle(length):
    # drawing equilateral triangle
    print ('Drawing Triangle')
    await moveForward(length)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 178, -100, 100)
    await moveForward(length)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 178, -100, 100)
    await moveForward(length)


async def draw_Rectangle(length):
    print ('Drawing Rectangle *')

async def draw_Star(length):
    print ('Drawing Star *')




    '''
    #mp = motor_pair.pair(motor_pair.PAIR_2,port.E,port.F)
    motion_sensor.reset_yaw(0)
    #await runloop.sleep_ms(2000)
    #motor_pair.move(motor_pair.PAIR_2,100,velocity=1000)
    while motion_sensor.tilt_angles()[0]<(degrees): #getting yaw value from tiltAngle function
        motor_pair.move_tank(motor_pair.PAIR_2,100,-100) # -100 is steering value Left = -100 to right = 100
    motor_pair.stop(motor_pair.PAIR_2)

    #await runloop.until( motion_sensor.tilt_angles()[0] = (90))

    #wait_until(motion_sensor.get_yaw_angle, greater_than_or_equal_to, 90)

    #Motor_Pair('A', 'E')
    #mp.set_stop_action('brake')
    #mp.start_tank(20, 0)
    #motion_sensor.reset_yaw_angle()
    #wait_until(hub.motion_sensor.get_yaw_angle, greater_than_or_equal_to, 90)
    #motor_pair.stop()
    
async def prnt():
    print
    '''


async def main():
    # init
    motor_pair.unpair(motor_pair.PAIR_2)
    motor_pair.pair(motor_pair.PAIR_2,port.E,port.F)
    motion_sensor.set_yaw_face(motion_sensor.FRONT)
    motion_sensor.reset_yaw(0)
    sound.volume(100)

    motor_pair.unpair(motor_pair.PAIR_1)
    motor_pair.unpair(motor_pair.PAIR_2)
    motor_pair.unpair(motor_pair.PAIR_3)
    motor_pair.pair(motor_pair.PAIR_1, port.E, port.F)
    
    #await draw_FullCircle()
    #await turn90()
    #await draw_Square(3)
    await draw_Triangle(3)
    # Turn right for 180 degrees
    #motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 535, -100, 100)

    '''
    with 180 degree wheel rotation, It takes a little less than 3 rounds for 360 degree turn. 
    Second variable Number of degrees = number degrees of wheel rotation - not turning the hub. 
    '''

    #backward
    await motor.run_for_degrees(port.D,500,100)
    #forward
    await motor.run_for_degrees(port.D,-500,100)

    #motor.stop(port.D)
    #await motor_pair.move_for_time(motor_pair.PAIR_1, 1000, 100,velocity=300)
    #motor_pair.move_tank(motor_pair.PAIR_1,100,-100)
    #await runloop.sleep_ms(3)
    #motor_pair.stop(motor_pair.PAIR_1)
    #await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 180, 100, 100)

    #light_matrix.write("Hi!")
    #motion_sensor.reset_yaw(0)
    #
    #light_matrix.write("Hi!")
    #while motion_sensor.tilt_angles()[0]<(360):   
    #    i=motion_sensor.tilt_angles()[0]
    #    light_matrix.write(str(i))

    #await moveBackward(10)
    #await moveForward(3)

    
    # await turn90(degrees)
    # turnDegrees = degrees * 1.644 # 1.644/2 = 0.822
    # turnDegrees = math.ceil(turnDegrees) *-1
    #await motor_pair.move_tank_for_degrees(motor_pair.PAIR_2, degrees, 200, -200,stop=motor.HOLD)
    
    

    #await turnLeft(4010)
    #await draw_Circle1()
    #await moveBackward(10)
    #await turnLeft(45)
    #await turnRight(180)

runloop.run(main())
