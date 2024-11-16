from pg import playground

x = 6
y = 7
dis = 8
pg = playground([36, 36])
"""
pg.obs((x, y), pg.DOWN, dis)
pg.obs((x+dis, y), pg.RIGHT, dis)
pg.obs((x, y+dis), pg.DOWN, dis+1)
"""
pg.setPos((10, 12))
pg.setEnd((0, 12))
pg.perspective(pg.REL, pg.RIGHT)
for i in range(0, 20):
  msg = pg.move(i+1, pg.RIGHT)
  if msg=="OBS_FOUND":
    break

pg.draw()
