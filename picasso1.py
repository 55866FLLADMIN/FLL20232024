from hub import light_matrix, motion_sensor, port, sound
import motor,motor_pair, runloop, math
from motor import BRAKE, HOLD
from motor_pair import move_tank, move_tank_for_degrees, stop


def init():
    ##Initialize motors and sensors
    motor_pair.unpair(motor_pair.PAIR_1)
    motor_pair.pair(motor_pair.PAIR_1,port.D,port.F)
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

async def armDown():
    '''
    Purpose:Lift up Arm
    degrees: 1 to 360
    speed: 100 to 1000
    '''
    print ('arm down')
    await motor.run_for_degrees(port.B, -360, 1000, acceleration=10000)


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
#Mission 01
async def Mission_3DCinema():
    await armUp()
    await tailUp()
    await moveForward(15)
    await turnLeft(6)
    await armDown()
    await turnRight(8)
    await armUp()
    await turnLeft(8)
    await armDown()
    await turnRight(8)
    await armUp()


#Mission 02
async def Mission_TheaterSceneChange():
    await armUp()
    await tailUp()

#Mission 03
async def mission_ImmersiveExperience():
    await armUp()
    await tailUp()

#Mission 04
async def mission_MasterPiece():
    await armUp()
    await tailUp()

#Mission 05
async def mission_5():
    await armUp()
    await tailUp()

#Mission 06
async def mission_6():
    await armUp()
    await tailUp()

#Mission 07
async def mission_7():
    await armUp()
    await tailUp()

#Mission 08
async def mission_8():
    await armUp()
    await tailUp()

#Mission 09
async def mission_9():
    await armUp()
    await tailUp()

#Mission 10
async def mission_SoundMixer():
    await armUp()
    await tailUp()moveBackward
    await moveBackward(3)
    await sound.beep()
    await turnRight(60)
    await moveForward(14)
    await turnLeft(40)
    await moveForward(4)
    await armUp()

'''
MISSIONS END
'''

async def main():
    # write your code here
    init()
    #await turnRight(90)
    await Mission_3DCinema()
    await mission_SoundMixer()
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
