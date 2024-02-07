from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:

robotArm.moveRight()
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()

for x in range(0, 3):
    if x < 2:
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    if x == 2:
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveRight()
        robotArm.drop()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()