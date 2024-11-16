from pg import playground

<<<<<<< HEAD
pg = playground([15, 15])
for i in range(3, 11):
  pg.obs((11, i))
  pg.obs((i, 3))
  pg.obs((i, 11))
pg.obs((11, 11))
pg.start((8, 5))
pg.draw()
while not pg.escaped():
  msg = pg.move(1, pg.UP)
  if msg=="OBS_FOUND":
    break
  print()
  pg.draw()
=======
min = 3
max = 13
pg = playground([24, 24])
"""
for i in range(min, max):
  pg.obs((max, i))
  pg.obs((i, min))
  pg.obs((i, max))
pg.obs((max, max))
"""
pg.setPos((12, 12))
#pg.setEnd((0, 3))
for i in range(1, 12):
  for j in range(0, i):
    if i%4==1:
      pg.move(pg.UP)
    elif i%4==2:
      pg.move(pg.RIGHT)
    elif i%4==3:
      pg.move(pg.DOWN)
    elif i%4==0:
      pg.move(pg.LEFT)
pg.draw()
>>>>>>> 30e67230a3370e9e31544c1c8e43e1abccd4dba6
