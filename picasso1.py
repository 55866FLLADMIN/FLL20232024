from hub import light_matrix, motion_sensor, port, sound
import motor,motor_pair, runloop
from motor import HOLD
from motor_pair import move_tank_for_degrees, stop
from app import music

#
## Gobal variables ##
DefaultsDict={}
DefaultsDict['MotorSpeed_MPS'] = '500'
DefaultsDict['MotorTurn_Degrees']='900'
##

def init():
    '''
    Initialize motors and sensors
    '''
    motor_pair.unpair(motor_pair.PAIR_1)
    motor_pair.pair(motor_pair.PAIR_1,port.D,port.F)
    motion_sensor.set_yaw_face(motion_sensor.FRONT)
    motion_sensor.reset_yaw(0)
    sound.volume(100)
    moveSpeed = 500


async def moveForward(distance):
    '''
    Move forward
    '''  
    if distance is None:
        return
    
    await light_matrix.write("F")    
    #await motor_pair.move_for_time(motor_pair.PAIR_1,5000,0,velocity=1000,acceleration=500)
    motor_pair.move_tank(motor_pair.PAIR_1, 100, 100)
    sound.beep()

async def moveBackward():
    '''
    Move backward
    + WORKS
    '''
    await light_matrix.write("B")
    await motor_pair.move_for_time(motor_pair.PAIR_1,5000,0,velocity=-1000,acceleration=500)
    sound.beep()



async def moveForward_ms(timeInMs):
    '''
    Move forward in ms
    '''
    if timeInMs is None:
        return

    light_matrix.write("===============================================================")
    await motor_pair.move_for_time(motor_pair.PAIR_1, timeInMs, 0, velocity=1000, stop=HOLD, acceleration=500)
    # params: motorPair,time_ms,steer(-100 to 100),velocity,accelaration)
    #motor_pair.move_tank(motor_pair.PAIR_1, 100, 100)
    motor_pair.stop(motor_pair.PAIR_1)
    sound.beep()


async def moveBackward_ms(timeInMs):
    '''
    Move Backward in ms
    '''
    if timeInMs is None:
        return

    light_matrix.write("B")
    await motor_pair.move_for_time(motor_pair.PAIR_1, timeInMs, 0, velocity=-1000, stop=HOLD, acceleration=500)
    # params: motorPair,time_ms,steer(-100 to 100),velocity,accelaration)
    #motor_pair.move_tank(motor_pair.PAIR_1, 100, 100)
    motor_pair.stop(motor_pair.PAIR_1)
    sound.beep()


async def turnLeft_ms(timeInMs):
    '''
    turn left
    + WORKS
    '''
    await light_matrix.write("L")
    # Perform tank turn
    motor_pair.move_tank(motor_pair.PAIR_1, -100, 100)
    await runloop.sleep_ms(timeInMs)
    motor_pair.stop(motor_pair.PAIR_1)
    sound.beep()

    #while motion_sensor.tilt_angles()[0]<1800: #getting yaw value from tuple
    #    motor_pair.move(motor_pair.PAIR_1,9000)
    #motor_pair.stop(motor_pair.PAIR_1)


async def turnRight_ms(timeInMs):
    '''
    turn right
    + WORKS
    '''
    await light_matrix.write("R")
    motor_pair.move_tank(motor_pair.PAIR_1, 100, -100)
    await runloop.sleep_ms(timeInMs)
    motor_pair.stop(motor_pair.PAIR_1)
    sound.beep()

    #while motion_sensor.tilt_angles()[0]<1800: #getting yaw value from tuple
    #    motor_pair.move(motor_pair.PAIR_1,9000)
    #motor_pair.stop(motor_pair.PAIR_1)


async def turnLeft(degrees):
    '''
    turn left by degrees from 1 to 360. 
    + WORKING
    '''
    if degrees is None:
        return

    motion_sensor.reset_yaw(0)
    lDegrees = degrees*10 # input to tilt_angle is 100 to 3600 in incremnts of 10.
    light_matrix.write("L")
    while motion_sensor.tilt_angles()[0]<lDegrees: #getting yaw value from tiltAngle function
        motor_pair.move(motor_pair.PAIR_1,-100) # -100 is steering value Left = -100 to right = 100
    motor_pair.stop(motor_pair.PAIR_1)
    sound.beep()


async def turnRight(degrees):
    '''
    turn left by degrees from 1 to 360.
    - NOT WORKING CORRECTLY
    '''
    if degrees is None:
        return

    motion_sensor.reset_yaw(0)
    lDegrees = degrees*10 # input to tilt_angle is 100 to 3600 in incremnts of 10.
    light_matrix.write("R")
    while motion_sensor.tilt_angles()[0]<(lDegrees): #getting yaw value from tiltAngle function
        motor_pair.move(motor_pair.PAIR_1,100) # -100 is steering value Left = -100 to right = 100
    motor_pair.stop(motor_pair.PAIR_1)
    sound.beep()


async def turnRight2(degrees):
    '''
    turn left by degrees from 1 to 360.
    - NOT WORKING CORRECTLY
    '''
    if degrees is None:
        return

    motion_sensor.reset_yaw(0)
    lDegrees = (360-degrees) # input to tilt_angle is 100 to 3600 in incremnts of 10.
    light_matrix.write("R")
    print (lDegrees)
    while motion_sensor.tilt_angles()[0]<(lDegrees): #getting yaw value from tiltAngle function
        motor_pair.move(motor_pair.PAIR_1,100) # -100 is steering value Left = -100 to right = 100
    motor_pair.stop(motor_pair.PAIR_1)
    sound.beep()

async def turn(direction,degrees):
    if direction is None or degrees is None:
        return
    
    '''
    DIRECTION: L or R
    DEGREES: 1 TO 360 degrees

    turn = wheel turn
    180 = 296
    90  = 148
    45  = 74
    '''

    #LEFT
    if direction == "LEFT":
        await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 296, -200, 200)
    #RIGHT   
    if direction == "RIGHT":
        await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, -148, -200, 200)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 74, -200, 200)

        #motor_pair.move_for_degrees(motor_pair.PAIR_1, 90, 0)



async def main():
    # write your code here
    init()

    #motor.run(port.B,5000)
    #motor.stop(port.B)
    #motor.run(port.C,5000)
    #motor.stop(port.C)

    sound.beep()
    #await moveBackward_ms(8000)
    await turn("L",90)
    await turn("R",90)
    '''
    await light_matrix.write("DJP!")
    await moveForward_ms(2000)
    await turnLeft(90)
    await moveForward_ms(2000)
    await turnLeft(90)
    await moveForward_ms(2000)
    await turnLeft(90)
    await moveForward_ms(2000)

    ''
    await turnRight2(90) #not working
    await moveForward_ms(2000)
    await moveBackward_ms(2000)
    await moveForward(10)
    #motor_pair.stop(motor_pair.PAIR_1)
    #await moveBackward()
    #motor_pair.stop(motor_pair.PAIR_1)
    await runloop.sleep_ms(1000)
    await turnRight2(90)
    await runloop.sleep_ms(1000)
    await turnLeft(90)
    #motor_pair.stop(motor_pair.PAIR_1)
    await runloop.sleep_ms(1000)
    await turnRight_ms(2000)
    #await turnLeft_ms(2000)
    motor_pair.stop(motor_pair.PAIR_1)
    sound.beep(440,1000,100)
    music.play_drum(8)
    '''

    #await moveForward_ms(10000)


runloop.run(main())
