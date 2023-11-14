from hub import light_matrix, port, motion_sensor, sound
import motor_pair
import motor
import runloop
import math
from hub import motion_sensor

async def moveForward_byQuarter(distance):
    '''
    Make the base turn at an angle by degrees provided.
    '''
    #print ('Moving Forward')
    degrees = math.ceil(distance * (26 * 2)/4)
    # 26:        for amount of degrees to rotate the wheels to move by 1/2 inch with small wheel
    # degrees * 2: when using the small wheel, you have to double the rotations to move by 1 inch.
    # 26 for aomut of degrees to rotate the wheels to move by 1 inch with "big wheel"
    print (degrees)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, -degrees, 100, 100)
    motor_pair.stop(motor_pair.PAIR_1)

async def moveForward(distance):
    '''
    Make the base turn at an angle by degrees provided.
    '''
    #print ('Moving Forward')
    degrees = distance * 26 * 2
    print (degrees)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, -degrees, 100, 100)
    motor_pair.stop(motor_pair.PAIR_1)


async def moveBackward(distance):
    print ('Moving Backward')
    degrees = distance * 26 * 2
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, degrees, 700, 700)
    motor_pair.stop(motor_pair.PAIR_1)


async def draw_Circle(radius):
    print ('Drawing circle')
    light_matrix.show_image(light_matrix.IMAGE_HAPPY)
    for x in range(1200):
        await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1,1,-1000,-1000)
        await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1,1,-1000,1000)


async def draw_fastCircle():
    light_matrix.show_image(light_matrix.IMAGE_HAPPY)
    for x in range(130):
        await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1,5,-1000,-1000)
        await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1,5,-1000,1000)

async def draw_fastCircle2():
    for x in range(130):
        await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1,5,-1000,-1000)
        await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1,5,-1000,1000)


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
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 178, -100, 100) #178 wheel degree turn = 60 degree turn
    await moveForward(length)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 178, -100, 100)
    await moveForward(length)

async def draw_Rectangle(length):
    print ('Drawing Rectangle')
    await moveForward(length*2)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 134, -100, 100) #134 wheel degree turn = 90 degree turn
    await moveForward(length)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 134, -100, 100)
    await moveForward(length*2)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 134, -100, 100)
    await moveForward(length)

async def draw_Diamond(length):
    print ('Drawing Diamond')
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 44, -100, 100)
    await moveForward(length)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 89, -100, 100)
    await moveForward(length)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 178, -100, 100)
    await moveForward(length)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 89, -100, 100)
    await moveForward(length)


async def draw_Heart(length):
    print ('Drawing Heart')
    light_matrix.show_image(light_matrix.IMAGE_HEART)
    await moveForward_byQuarter(5)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 147, -100, 100)
    await moveForward_byQuarter(5)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, math.ceil(45*8), -100, 50)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1,134,500,-500)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, math.ceil(45*8), -100, 50)
    #await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 180*1, -1000, 500)


async def draw_Star(length):
    print ('Drawing Star')
    '''
    7 inches = one full wheel rotation.
    36 internal turn
    108 external turn
    '''
    for i in range(5):
        await moveForward(length)
        await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1,106,-100,100) # 72 degree turn
        await moveForward(length)
        await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1,213,100,-100) # = 144
        #await moveForward(1)


async def draw_Hexagon(length):
    for i in range(6):
        await moveForward(length)
        await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1,88,100,-100) # = 180


async def draw_Pentagon(length):
    for i in range(5):
        await moveForward(length)
        await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1,106,100,-100) # = 180


async def main():
    # init
    motor_pair.unpair(motor_pair.PAIR_1)
    motor_pair.unpair(motor_pair.PAIR_2)
    motor_pair.unpair(motor_pair.PAIR_3)
    motor_pair.pair(motor_pair.PAIR_1, port.E, port.F)
    motion_sensor.set_yaw_face(motion_sensor.FRONT)
    motion_sensor.reset_yaw(0)
    sound.volume(100)
    sound.beep()
    sound.beep()
    sound.beep()

    await draw_Square(2)
    await runloop.sleep_ms(4000)
    await draw_Rectangle(2)
    await runloop.sleep_ms(4000)
    await draw_Diamond(2)
    await runloop.sleep_ms(4000)
    await draw_Triangle(2)
    await runloop.sleep_ms(4000)
    await draw_Pentagon(2)
    await runloop.sleep_ms(4000)
    await draw_Hexagon(2)
    await runloop.sleep_ms(4000)
    await draw_Heart(1)
    await runloop.sleep_ms(4000)
    await draw_Star(2)
    await runloop.sleep_ms(4000)
    await draw_fastCircle()
    await runloop.sleep_ms(4000)
    await draw_Circle(1)


runloop.run(main())
