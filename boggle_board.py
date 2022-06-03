import string
import random

class BoggleBoard:
  
  def __init__(self):
    print(f'_ _ _ _\n_ _ _ _\n_ _ _ _\n_ _ _ _')

  def shake(self):
    board = (f'_ _ _ _\n_ _ _ _\n_ _ _ _\n_ _ _ _')
    alphabet_string = string.ascii_uppercase
    alphabet_list = list(alphabet_string)
    for i in range(len(board)):
      board = (board.replace('_', (random.choice(alphabet_list)), 1))
    board = board.replace('Q', 'Qu')
    print(board)

case = BoggleBoard()

case.shake()