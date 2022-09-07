import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
playerSys = 0

while True:
  cls()
  
  print(row1)
  print(row2)
  print(row3)
  
  playerSys += 1
  
  if playerSys % 2 == 0:
      # O turn
      print("O turn")
      player = "O"
  else:
      # X turn
      print("X turn")
      player = "X"
      
  print("Please write like so:")
  play = input("<Row> <Col>: ")
  
  play = play.split(" ")
  col = play[1]
  row = play[0]
  
  col = int(col)
  
  if row == "1":
      row1[col - 1] = player
  elif row == "2":
      row2[col - 1] = player
  elif row == "3":
      row3[col - 1] = player
