import string
import random

class BoggleBoard:
  
  def __init__(self):
    print(f'____\n____\n____\n____')

  def shake(self):
    board = (f'____\n____\n____\n____')
    alphabet_string = string.ascii_uppercase
    alphabet_list = list(alphabet_string)
    for i in range(len(board)):
      board = (board.replace('_', (random.choice(alphabet_list)), 1))
      
    print(board)

case = BoggleBoard()

case.shake()
  

#Mayan Nubering System