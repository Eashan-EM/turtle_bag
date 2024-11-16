from termcolor import colored

class playground():
  ABS = 0
  REL = 1
  UP = (-1, 0)
  RIGHT = (0, 1)
  DOWN = (1, 0)
  LEFT = (-1, 0)

  pers = ABS
  area = []
  direction = RIGHT
  turtlePos = (0, 0)
  boxArea = []
  def __init__(self, pos):
    self.area = pos
  def turtle_pos(self, pos):
    turtlePos = pos
  def perspective(self, pers):
    self.pers = pers
  def obs(self, pos):
    self.boxArea.append(pos)
  def start(self, pos):
    self.turtlePos = pos
  def move(self, dis, angle):
    temp = (self.turtlePos[0]+angle[0]*dis, self.turtlePos[1]+angle[1]*dis)
    if not (temp in self.boxArea):
      self.turtlePos = temp
    else:
      return "OBS_FOUND"
  def escaped(self):
    if (self.turtlePos[0]<1 or self.turtlePos[0]>=6) or (self.turtlePos[1]<1 or self.turtlePos[1]>=6):
      return True
    return False
  def draw(self):
    for i in range(0, self.area[0]):
      for j in range(0, self.area[1]):
        if (i, j) in self.boxArea:
          print(colored('= ', 'yellow'), end='')
        elif (i, j)==self.turtlePos:
          print(colored('@ ', 'green'), end='')
        else:
          print('# ', end="")
      print()
