from termcolor import colored

class playground():
  ABS = 0
  REL = 1
  UP = (-1, 0)
  RIGHT = (0, 1)
  DOWN = (1, 0)
  LEFT = (0, -1)

  pers = ABS
  area = []
  turtlePos = (0, 0)
  def __init__(self, pos):
    for i in range(0, pos[0]):
      self.area.append([])
      for j in range(0, pos[1]):
        self.area[i].append(0)
  def setPos(self, pos):
    self.turtlePos = pos
    self.area[pos[0]][pos[1]] = 3
  def getPos(self):
    return self.turtlePos
  def perspective(self, pers):
    self.pers = pers
  def obs(self, pos):
    self.area[pos[0]][pos[1]] = 1
  def setEnd(self, pos):
    self.area[pos[0]][pos[1]] = 2
  def move(self, angle):
    pos = self.turtlePos
    temp = (pos[0]+angle[0], pos[1]+angle[1])
    if not (self.area[temp[0]][temp[1]]==1 or self.area[temp[0]][temp[1]]==2):
      self.area[pos[0]][pos[1]] = 4
      self.turtlePos = temp
      self.area[temp[0]][temp[1]] = 3
    else:
      return "OBS_FOUND"
  def draw(self):
    for i in range(0, len(self.area)):
      for j in range(0, len(self.area[0])):
        if self.area[i][j] == 0:
          print('# ', end='')
        elif self.area[i][j] == 1:
          print(colored('= ', 'yellow'), end='')
        elif self.area[i][j] == 2:
          print(colored('# ', 'red'), end='')
        elif self.area[i][j] == 3:
          print(colored('@ ', 'green'), end='')
        elif self.area[i][j] == 4:
          print(colored('# ', 'green'), end='')
      print()