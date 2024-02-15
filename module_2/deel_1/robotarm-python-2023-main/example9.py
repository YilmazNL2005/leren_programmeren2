from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:

# robotArm.grab()

# for a in range(5):
#     robotArm.moveRight()
# robotArm.drop()

# for b in range(4):
#     robotArm.moveLeft()

# for z in range(2):
#     robotArm.grab()
#     for x in range(5):
#         robotArm.moveRight()
#     robotArm.drop()
#     for y in range(5):
#         robotArm.moveLeft()

for stapel in range(1,5): 
    for blok3 in range(stapel):
        robotArm.grab()
        for b in range(5):
            robotArm.moveRight()
        robotArm.drop()    
        for c in range(5): 
            robotArm.moveLeft()
    robotArm.moveRight()





# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()