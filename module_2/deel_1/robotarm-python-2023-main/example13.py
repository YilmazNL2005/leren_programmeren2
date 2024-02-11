from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:

verplaatsingen = 1
while verplaatsingen < 8:
    robotArm.grab()
    if robotArm.scan() == str(""):
        verplaatsingen = 10
        terug = 10
    else:
        for x in range(verplaatsingen):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(verplaatsingen):    
            robotArm.moveLeft()
        verplaatsingen = verplaatsingen + 1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()