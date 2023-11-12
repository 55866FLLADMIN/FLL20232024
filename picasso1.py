from hub import light_matrix, motion_sensor, port, sound
import motor,motor_pair, runloop, math
from motor import BRAKE, HOLD, run, velocity
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

async def moveForwardFast(distance):
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
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, degrees, 700, 700,acceleration=10000)
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

async def turnRightSlow(degrees):
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
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, turnDegrees, -200, 200, acceleration=50)

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


async def tailDown():
    '''
    Purpose:Lift up Arm
    degrees: 1 to 360
    speed: 100 to 1000
    '''
    print ('tail up')
    await motor.run_for_degrees(port.E, 690, 690)

async def tailDownbyAngle(angle):
    '''
    Purpose:Lift up Arm
    degrees: 1 to 360
    speed: 100 to 1000
    '''
    print ('tail up')
    await motor.run_for_degrees(port.E, angle, 690)

async def tailUpByAngle(angle):
    '''
    Purpose:Lift up Arm
    degrees: 1 to 360
    speed: 100 to 1000
    '''
    print ('tail up')
    await motor.run_for_degrees(port.E,angle, 360)



async def tailUp():
    '''
    Purpose:Lift up Arm
    degrees: 1 to 360
    speed: 100 to 1000
    '''
    print ('tail Down')
    await motor.run_for_degrees(port.E, -360, 720)

async def moveForwardByDecDisByspeed(distance, speed):
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
    degrees = distance * (360/float(14))
    degrees = round(degrees)
    #await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 360, 500, 500)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, degrees, speed, speed)
    motor_pair.stop(motor_pair.PAIR_1)
    #await motor_pair.move_for_time(motor_pair.PAIR_1,5000,0,velocity=1000,acceleration=500)
    #motor_pair.move_tank(motor_pair.PAIR_1, 100, 100)


    #await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, -360, 500, 500)
    #await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, -180, 500, 500)
    sound.beep()

def sensed_color():
    return color_sensor.color(port.D) == color.BLACK or color_sensor.color(port.F) == color.BLACK

async def line_square():
    motor_pair.move(motor_pair.PAIR_1, 0, velocity =30)
    await runloop.until(sensed_color)
    if color_sensor.color(port.D) == color.BLACK:
        # motor_pair.move_tank(motor_pair.PAIR_1, -50, speed)
        while color_sensor.color(port.F) != color.BLACK:
            await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 10, -10, 10)
        motor_pair.stop(motor_pair.PAIR_1)
    else:
        while color_sensor.color(port.D) != color.BLACK:
            await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 10, 7, -7)
        motor_pair.stop(motor_pair.PAIR_1)




'''
MISSIONS START
'''


#mission 8
async def bananaboat():
    await armDown()
    await armUpByAngle(160)
    # await moveForward(2)
    # await turnRight(90)
    # await moveForwardByDecDisByspeed(4,280)
    # await turnLeft(90)
    await moveForwardByDecDisByspeed(58.75,5000)
    await turnLeft(84)
    #await moveBackward(1)
    # await moveForwardByDecDisByspeed(0.5,280)
    #await moveForwardByHalf(1)
    await armDown()
    await armDown()
    await turnRightSlow(45)
    await moveBackward(5)
    await armUp()
    await turnLeft(45)
    await moveForward(6)
    await armDown()
    #runloop.sleep_ms(30000)
    await moveBackward(3)
    await armUp()
    await turnLeft(90)
    await armUp()




    #Mission 9
async def lighttower():
    await line_square()
    await moveForward(5)
    await turnRight(90)

    #await moveForwardByDecDisByspeed(0.5,500)
    await moveForward(2)
    await tailUp()
    await tailDown()
    await moveBackward(8)
    i=0
    while i<6:
        await motor.run_for_degrees(port.E, -1000, 1000, acceleration=100000)
        runloop.sleep_ms(400)
        i=i+1
    await tailDown()
    await moveForward(5)
    await turnLeft(80)
    await moveForwardFast(50)




    #Mission 10
async def rollingCamera2():
    await armDown()
    await moveForward(19)
    await moveBackward(15)
    await turnRight(90)
    await armUp()





#Mission 11
async def lights():
    await armUp()
    await moveForward(33)
    await turnRight(18)
    await moveForward(2)
    await armDownByAngle(100)
    await turnLeft(21)
    await armUp()

    #Mission 12
async def dj():
    await moveBackward(14)
    await turnLeft(50)
    await moveForward(19)
    await turnRight(90)
    await moveForwardSlow(8)

    #Mission 13
async def sounds():
    await moveBackward(8)
    # while color_sensor.color(port.D) != color.BLACK or color_sensor.color(port.F) != color.BLACK:
    #    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 10, 10, 10)
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

    #Misson 15
async def masterpiece():
    await tailUp()
    await tailUp()
    await tailDown()
    await moveBackward(25)
    await turnLeft(69)
    await moveBackward(38)
    await turnRight(25)
    await moveBackward(5)
    await tailUp()
    await moveForward(6)
    await turnLeft(45)
    await moveForward(19)
    await armUp()
    await turnRight(65)
    await moveForward(35)








    "missions ends"




async def main():
    # write your code here
    init()
    #await bananaboat()
    #await lighttower()
    #await rollingCamera2()
    #await lights()
    #await dj()
    #await sounds()
    #await comehome()
    await masterpiece()
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
