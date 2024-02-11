from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier:
for x in range(9):
    robotArm.moveRight()
for b in range(5):
    for z in range(6):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        if z < 5:
            robotArm.moveRight()
    if b < 4:
            robotArm.moveLeft()




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()