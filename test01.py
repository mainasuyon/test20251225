import pyxel

msize = 15
pyxel.init(msize*11, msize*11)

pyxel.cls(7)

pyxel.mouse(True)

## 縦線をひく
pyxel.rect(msize+msize*0-1,msize,3,9*msize,0)
pyxel.line(msize+msize*1,  msize,msize+msize,msize+9*msize,0)
pyxel.line(msize+msize*2,  msize,msize+msize*2,msize+9*msize,0)
pyxel.rect(msize+msize*3-1,msize,3,9*msize,0)
pyxel.line(msize+msize*4,  msize,msize+msize*4,msize+9*msize,0)
pyxel.line(msize+msize*5,  msize,msize+msize*5,msize+9*msize,0)
pyxel.rect(msize+msize*6-1,msize,3,9*msize,0)
pyxel.line(msize+msize*7,  msize,msize+msize*7,msize+9*msize,0)
pyxel.line(msize+msize*8,  msize,msize+msize*8,msize+9*msize,0)
pyxel.rect(msize+msize*9-1,msize,3,9*msize,0)
## 横線を引く
pyxel.rect(msize,msize+msize*0-1,9*msize,3,0)
pyxel.line(msize,msize+msize*1,  msize+msize*9,msize+msize*1,0)
pyxel.line(msize,msize+msize*2,  msize+msize*9,msize+msize*2,0)
pyxel.rect(msize,msize+msize*3-1,9*msize,3,0)
pyxel.line(msize,msize+msize*4,  msize+msize*9,msize+msize*4,0)
pyxel.line(msize,msize+msize*5,  msize+msize*9,msize+msize*5,0)
pyxel.rect(msize,msize+msize*6-1,9*msize,3,0)
pyxel.line(msize,msize+msize*7,  msize+msize*9,msize+msize*7,0)
pyxel.line(msize,msize+msize*8,  msize+msize*9,msize+msize*8,0)
pyxel.rect(msize,msize+msize*9-1,9*msize,3,0)

## 表出数字を配置する
pyxel.text(int(msize+msize*0.5),int(msize+msize*0.5),'1',0)

pyxel.show()

