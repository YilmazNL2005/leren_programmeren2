from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:

rijen = 9
while rijen != 0:
    robotArm.grab()
    scan = robotArm.scan()
    if scan != "red":
        robotArm.drop()
        robotArm.moveRight()
        rijen -= 1
    else:
        for y in range(rijen):
            robotArm.moveRight()
        robotArm.drop()
        for y in range(rijen - 1):
            robotArm.moveLeft()
        rijen -= 1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()