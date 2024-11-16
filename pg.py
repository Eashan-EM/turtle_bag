from termcolor import colored

class playground():
  ABS = 0
  REL = 1
  UP = 0
  RIGHT = 1
  DOWN = 2
  LEFT = 3

  direc = UP
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
  def perspective(self, pers, direc):
    self.pers = pers
    if pers==self.ABS:
      self.direc = UP
    elif pers==self.REL:
      self.direc = direc
  def __formatDirec(self, direc):
    if direc==0:
      direc = (-1, 0)
    elif direc==1:
      direc = (0, 1)
    elif direc==2:
      direc = (1, 0)
    elif direc==3:
      direc = (0, -1)
    return direc
  def obs(self, pos, direc, dis=1):
    direc = self.__formatDirec(direc)
    for i in range(0, dis):
      self.area[pos[0]][pos[1]] = 1
      pos = (pos[0]+direc[0], pos[1]+direc[1])
  def setEnd(self, pos):
    self.area[pos[0]][pos[1]] = 2
  def move(self, dis, direc):
    direc = (direc+self.direc)%4
    if self.pers==self.REL:
      self.direc = direc
    direc = self.__formatDirec(direc)
    for i in range(0, dis):
      pos = self.turtlePos
      temp = (pos[0]+direc[0], pos[1]+direc[1])
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
