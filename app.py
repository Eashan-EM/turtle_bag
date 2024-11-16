from pg import playground

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