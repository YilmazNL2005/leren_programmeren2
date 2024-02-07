from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

# Jouw python instructies zet je vanaf hier:
a = 7
b = 1
for x in range(7):
    robotArm.moveRight()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()  
while b < 8:
    for x in range(2):
        robotArm.moveLeft()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    b += 1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()