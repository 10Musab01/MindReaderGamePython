last_1 = 0
last_2 = 0

import numpy as np
import random
inputs = np.zeros(shape=(2, 2, 2), dtype=int)
inputs

def update_inputs(current):
  global last_2 , last_1
  if inputs[last_2][last_1][0] == current:
    inputs[last_2][last_1][1] = 1
    inputs[last_2][last_1][0] = current
  else:
    inputs[last_2][last_1][1] = 0
    inputs[last_2][last_1][0] = current

  last_2 = last_1
  last_1 = current

def prediction():
  if inputs[last_2][last_1][1] == 1:
    predict = inputs[last_2][last_1][0]
  else:
    predict = random.randint(0, 1)
  return predict



scores = [0 , 0]# [computer_score , player_score]
def update_scores(player_input , computer_prediction):
    if player_input == computer_prediction:
        scores[0] += 1
    else:
        scores[1] += 1
    print("Player score" , scores[1] , "Computer score" , scores[0])


def reset():
    for i in range(len(scores)):
        scores[i] = 0
    for i in range(0 , 2):
        for j in range(0 , 2):
            for k in range(0 , 2):
                inputs[i][j][k] = 0





def gameplay():
    reset()
    print(inputs)
    print(scores)
    valid_entries = [0 , 1]
    while True:
        pred = prediction()
        player_input = int(input("Enter a 0 or 1: "))
        while player_input not in valid_entries:
            print("Invalid entry")
            player_input = int(input("Enter a 0 or 1: "))
        update_inputs(player_input)
        update_scores(player_input , pred)
        if scores[0] == 10:
            print("Sorry, you lost!")
            break
        elif scores[1] == 10:
            print("Well done, you won!")
            break

gameplay()