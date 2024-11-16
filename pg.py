from termcolor import colored

class playground():
  ABS = 0
  REL = 1
  UP = 0
  RIGHT = 1
  DOWN = 2
  LEFT = 3

  pers = ABS
  area = []
  direction = RIGHT
  turtlePos = []
  boxOri = []
  boxArea = []
  def __init__(self, pos):
    self.area = pos
  def turtle_pos(self, pos):
    turtlePos = pos
  def perspective(self, pers):
    self.pers = pers
  def box(self, ori, pos):
    self.boxOri = ori
    self.boxArea = pos
  def move(self):
    return 0
  def draw(self):
    for i in range(0, self.area[0]):
      for j in range(0, self.area[1]):
        if (j>=self.boxOri[0] and j<self.boxOri[0]+self.boxArea[0]) and (i==self.boxOri[1] or i==self.boxOri[1]+self.boxArea[1]):
          print(colored('= ', 'yellow'), end='')
        else:
          print('# ', end="")
      print()
