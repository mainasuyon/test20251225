import pyxel

msize = 15
pyxel.init(128, 128)

pyxel.cls(7)

pyxel.mouse(True)


pyxel.rect(msize,msize+msize*9-1,9*msize,3,0)


pyxel.show()

