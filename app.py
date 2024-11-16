from pg import playground

pg = playground([10, 10])
for i in range(1, 6):
  pg.obs((1, i))
  pg.obs((6, i))
  pg.obs((i, 1))
  pg.obs((i, 6))
pg.obs((6, 6))
pg.start((2, 2))
pg.draw()
while not pg.escaped():
  msg = pg.move(1, pg.RIGHT)
  if msg=="OBS_FOUND":
    break
  pg.draw()
