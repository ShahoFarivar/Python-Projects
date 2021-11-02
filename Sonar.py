import math , random

gameBoard = [] #change a to gameBoard
chests = []
playerCoordinations= []
row = 30
column = 10
numberOfChests = 3
remainingSonars = 20
instruct = "game instruction"

def make_board():
	global column
	global row
	global gameBoard
	for i in range(column):
		gameBoard.append([])
		for j in range(row):
			choice=random.randint(0,1)
			if choice==0:
				gameBoard[i].append("~")
			else:
				gameBoard[i].append("`")

def print_board():
	global column
	global row
	global gameBoard
	for i in range(column):
		print("\n")
		for j in range(row):
			print(gameBoard[i][j],end=" ")
			
def calculate_dis(indexOfCoor):
  # search of nearest chest and add distance, if distance greater than 10 add X aslo found chest 
  global playerCoordinations
  global chests
  dis = []
  dis.clear()
  for i in range(len(chests)):
    x=abs(int(playerCoordinations[indexOfCoor][0]) - chests[i][0])
    y = abs(int(playerCoordinations[indexOfCoor][1]) - chests[i][1])
    distance = int(math.sqrt(pow(x,2)+pow(y,2)))
    dis.append(distance)
    nearestChest = dis[0]
  dis.sort()
  nearestChest=dis[0]
  if nearestChest == 0:
    gameBoard[int(playerCoordinations[indexOfCoor][1])][int(playerCoordinations[indexOfCoor][0])] = "X"
    chests.remove([int(playerCoordinations[indexOfCoor][0]),int(playerCoordinations[indexOfCoor][1])])
    print("\n!!!!!!!You found a chest!!!!!")
    for item in range(indexOfCoor):
      gameBoard[int(playerCoordinations[indexOfCoor][1])][int(playerCoordinations[indexOfCoor][0])] = "X"
    for item in range(len(playerCoordinations)):
      gameBoard[int(playerCoordinations[item][1])][int(playerCoordinations[item][0])]="X"
  elif nearestChest < 10:
    gameBoard[int(playerCoordinations[indexOfCoor][1])][int(playerCoordinations[indexOfCoor][0])] = nearestChest
  else:
    gameBoard[int(playerCoordinations[indexOfCoor][1])][int(playerCoordinations[indexOfCoor][0])] = "X"
def get_input():
  global playerCoordinations
  while True:
    flag=0
    getInput = input(f"\nEnter sonar coordinations(0-{row-1} 0-{column-1}): ")
    tempInput = getInput.split(" ")
    for item in range(len(playerCoordinations)):
      if tempInput in playerCoordinations:
        flag=1
    if int(tempInput[0])<row-1 and int(tempInput[1])<column-1 and flag==0:
      playerCoordinations.append(tempInput)
      return 
    else:
      print(f"Wrong coordinations or already entered:(0-{row-1} 0-{column-1})")

def make_chests():
  global row
  global column
  global numberOfChests
  global chests
  for count in range(numberOfChests):
    newChest = [random.randint(0,row-1),random.randint(0,column-1)]
    chests.append(newChest)
	
def game():
  global remainingSonars
  global chests
  make_board()
  print_board()
  make_chests()
  tries = 0
  indexOfCoor = tries
  running = True
  while tries < remainingSonars and running == True:
    get_input()
    distance = calculate_dis(indexOfCoor)
    tries +=1
    indexOfCoor = tries
    print(20 - tries , " sonars left." , len(chests) ,  " chests left.\n")
    print_board()
    if len(chests) == 0:
      print("\nAll chests found.")
      running =False
  if tries == remainingSonars and running == True:
    print("You failed to find all chests.")
		
def replay():
  while True:
    answer = input("Do you want to play again? (y/n)")
    if answer == "y":
      return True
    elif answer == "n":
      return False
    else:
      print("Only enter <y> for yes and <n> for no.")

def print_ins():
  ins = '''Instructions:
You are the captain of the Simon, a treasure-hunting ship.\nYour current mission is to use sonar devices to find three sunken treasure chests at theb bottom of the ocean.\nBut you only have cheap sonar that finds distance, not direction.\nEnter the coordinates to drop a sonar device.\nThe ocean map will be marked with how far away the nearest chest is, or an X if it is beyond the sonar device's range.\nFor example, the C marks are where chests are.\nThe sonar device shows a 3 because the closest chest is 3 spaces away.

 1 2 3
 012345678901234567890123456789012

 0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
 1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
 2 `~`C``3`~~~~`C`~~~~`````~~``~~~`` 2
 3 ````````~~~`````~~~`~`````~`~``~` 3
 4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4

 012345678901234567890123456789012
 1 2 3
 
In the real game, the chests are not visible in the ocean.)'''
  answer=input("Do you want to show game instructions?(y for yes) ")
  if answer.lower() =="y":
    print(ins)
  else:
    return

def main():
  running = True
  while running:
    gameBoard.clear()
    chests.clear()
    playerCoordinations.clear()
    print_ins()
    game()
    running = replay()
  print("Exiting...")

main()
