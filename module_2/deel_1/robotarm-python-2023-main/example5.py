from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

# Jouw python instructies zet je vanaf hier:

for x in range(7):
    robotArm.moveRight()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()  
for z in range(7):
    for x in range(2):
        robotArm.moveLeft()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()