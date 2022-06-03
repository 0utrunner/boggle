import string
import random

class BoggleBoard:
  
  def __init__(self):
    print(f'_ _ _ _\n_ _ _ _\n_ _ _ _\n_ _ _ _')

  def shake(self):
    board = (f'_ _ _ _\n_ _ _ _\n_ _ _ _\n_ _ _ _')
    # die = [['A','A','E','E','G','N'],['E','L','R','T','T','Y'],['A','O','O','T','T','W'],['A','B','B','J','O','O'],['E','H','R','T','V','W'],['C','I','M','O','T','U'],['D','I','S','T','T','Y'],['E','I','O','S','S','T'],['D','E','L','R','V','Y'],['A','C','H','O','P','S'],['H','I','M','N','Qu','U'],['E','E','I','N','S','U'],['E','E','G','H','N','W'],['A','F','F','K','P','S'],['H','L','N','N','R','Z'],['D','E','I','L','R','X']]
    alphabet_string = string.ascii_uppercase
    alphabet_list = list(alphabet_string)
    for i in range(len(board)):
      board = (board.replace('_', (random.choice(alphabet_list)), 1))
    board = board.replace('Q', 'Qu')
    print(board)

case = BoggleBoard()

case.shake()



