from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:
links = 8
verplaatsingen = 9

for i in range(5):
    robotArm.grab()
    for x in range(verplaatsingen):
        robotArm.moveRight()
    robotArm.drop()
    verplaatsingen -= 2
    for x in range(links):
        robotArm.moveLeft()
    links -= 2

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()

