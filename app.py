from pg import playground

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
