#This is a tic-tac-toe game
main_loop= True
ask_loop= True
play_again= True
game_is_running = True
which_player=""
board=["-","-","-","-","-","-","-","-","-"]


def print_board():
  print(board[0],board[1],board[2])
  print(board[3],board[4],board[5])
  print(board[6],board[7],board[8])

def input_numeric():
  correct_choice =True
  while correct_choice:
    choice=(input("Enter 1 - 9 :"))
    if choice in "123456789" :
      correct_choice=False
    else:
      print("Only Enter 1 - 9 : ")
      correct_choice= True
  return choice


def player_move():
  global board
  is_empty=True
  while is_empty:
    choice=input_numeric()
    #check the board is not already taken
    if board[int(choice)-1]!="X" and board[int(choice)-1]!="O":
      is_empty=False
      board[int(choice) - 1] = "X"
    else:
      print("Selected Position is not empty, make another choice: ")
      is_empty= True
    

def AI_move():
  global board
  if board[0]=="-" and board[1]==board[2]=="O":
    board[0]="O"
  elif board[1]=="-" and board[0]==board[2]=="O" :
    board[1]="O"
  elif board[2]=="-" and board[0]==board[1]=="O":
    board[2]="O" 
  elif board[3]=="-" and board[4]==board[5]=="O":
    board[3]="O"
  elif board[4]=="-" and board[3]==board[5]=="O":
    board[4]="O"
  elif board[5]=="-" and board[3]==board[4]=="O":
    board[1]="O"
  elif board[6]=="-" and board[7]==board[8]=="O":
    board[6]="O"
  elif board[7]=="-" and board[6]==board[8]=="O":
    board[7]="O"
  elif board[8]=="-" and board[6]==board[7]=="O":
    board[8]="O"
  elif board[0]=="-" and board[4]==board[8]=="O":
    board[0]="O"
  elif board[4]=="-" and board[0]==board[8]=="O":
    board[4]="O"
  elif board[8]=="-" and board[0]==board[4]=="O":
    board[8]="O"
  elif board[2]=="-" and board[4]==board[6]=="O":
    board[2]="O"
  elif board[4]=="-" and board[2]==board[6]=="O":
    board[4]="O"
  elif board[6]=="-" and board[2]==board[4]=="O":
    board[6]="O"
  #couner attack and dont let X win
  elif board[0]==board[1]=="X" and board[2]=="-":
    board[2]="O"
  elif board[0]==board[2]=="X" and board[1]=="-":
    board[1]="O"
  elif board[1]==board[2]=="X" and board[0]=="-":
    board[0]="O"
  elif board[3]==board[4]=="X" and board[5]=="-":
    board[5]="O"
  elif board[3]==board[5]=="X" and board[4]=="-":
    board[4]="O"
  elif board[4]==board[5]=="X" and board[3]=="-":
    board[3]="O"
  elif board[6]==board[7]=="X" and board[8]=="-":
    board[8]="O"
  elif board[6]==board[8]=="X" and board[7]=="-":
    board[7]="O"
  elif board[7]==board[8]=="X" and board[6]=="-":
    board[6]="O"
  elif board[0]==board[4]=="X" and board[8]=="-":
    board[8]="O"
  elif board[0]==board[8]=="X" and board[4]=="-":
    board[4]="O"
  elif board[4]==board[8]=="X" and board[0]=="-":
    board[0]="O"
  elif board[2]==board[4]=="X" and board[6]=="-":
    board[6]="O"
  elif board[2]==board[6]=="X" and board[4]=="-":
    board[4]="O"
  elif board[4]==board[6]=="X" and board[2]=="-":
    board[2]="O"
    #Take center
  elif board[4]=="-": 
    board[4]="O"
    #Take free slot
  elif board[0]=="-":
    board[0]="O"
  elif board[1]=="-":
    board[1]="O"
  elif board[2]=="-":
    board[2]="O"
  elif board[3]=="-":
    board[3]="O"
  elif board[4]=="-":
    board[4]="O"
  elif board[5]=="-":
    board[5]="O"
  elif board[6]=="-":
    board[6]="O"
  elif board[7]=="-":
    board[7]="O"
  elif board[8]=="-":
    board[8]="O"
  print("AI moved.")

def check_tie():
  return

def check_winner(board):
  global game_is_running
  if board[0] == board[1] == board[2] != "-":
    game_is_running = False
    if board[0]== "X":
      print("You won !")
    else:
      print("AI won !")
  elif board[3] == board[4] == board[5] != "-":
    game_is_running = False
    if board[3]== "X":
      print("You won !")
    else:
      print("AI won !")
  elif board[6] == board[7] == board[8] != "-":
    game_is_running = False
    if board[6]== "X":
      print("You won !")
    else:
      print("AI won !")
  elif board[0] == board[3] == board[6] != "-":
    game_is_running = False
    if board[3]== "X":
      print("You won !")
    else:
      print("AI won !")
  elif board[1] == board[4] == board[7] != "-":
    game_is_running = False
    if board[1]== "X":
      print("You won !")
    else:
      print("AI won !")
  elif board[2] == board[5] == board[8] != "-":
    game_is_running = False
    if board[2]== "X":
      print("You won !")
    else:
      print("AI won !")
  elif board[0] == board[4] == board[8] != "-":
    game_is_running = False
    if board[0]== "X":
      print("You won !")
    else:
      print("AI won !")
  elif board[2] == board[4] == board[6] != "-":
    game_is_running = False
    if board[2]== "X":
      print("You won !")
    else:
      print("AI won !")
  elif game_is_running == False:
    print("Tie")

def check_end_game(board):
  global game_is_running
  dash_flag = False
  for item in board:
    if item == "-":
      dash_flag = True
  if dash_flag == True:
    game_is_running = True
  else:
    game_is_running = False
    check_winner(board)

def select_player():
  global which_player
  check_answer = True
  while check_answer:
    answer= input("Do you want to play game first? y/n")
    if answer == "y":
      check_answer = False
      # X is player, O is AI
      which_player= "X"
      print("You go first.")
    elif answer == "n":
      check_answer = False
      which_player= "O"
      print("AI goes first.")
    else:
      check_answer = True
      print("Only enter y or n: ")     

def ask_yn():
  global play_again
  global ask_loop
  while ask_loop:
      yes_no = input("Do you want to play again? y/n")
      if yes_no == "y":
        play_again = True
        ask_loop = False
      elif yes_no == "n":
        play_again = False
        ask_loop = False
      else:
        ask_loop = True
        print("Only enter y or n: ")

def start_game():
  global which_player
  global game_is_running
  select_player()
  while game_is_running:
    print_board()  
    if which_player == "X":
      player_move()
      which_player= "O"
    elif which_player == "O":
      AI_move()
      which_player="X"
    check_winner(board)
    if game_is_running == True:
      check_end_game(board) 

def main_loop():
  global play_again 
  global board
  global ask_loop
  global game_is_running
  play_again = True
  while play_again:
    start_game()
    print_board()
    board=["-","-","-","-","-","-","-","-","-"]
    ask_loop = True
    ask_yn()
    if play_again== True:
      game_is_running=True 
    
main_loop()

print("Exiting...")
