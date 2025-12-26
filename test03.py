import pyxel

class App:
    global msize
    msize = 11
    global ymax
    global xmax
    aaa = []
    bbb = []

    def __init__(self):
        pyxel.init(msize*11, msize*11)
        self.number = 0
        pyxel.mouse(True)

        ## 問題ファイルを読み込む
        with open('test04.txt') as f:
            inputline = f.readlines()

            self.ymax = int(inputline[0])
            self.xmax = int(inputline[0])
            ymax = self.ymax
            xmax = self.xmax
            for p in range(1,ymax+1):
                tmpline = inputline[p].split()
                j = p - 1
                for i in range(0,xmax):
                    if tmpline[i] == '.' :
                        self.aaa.append(0)
                    else :
                        self.aaa.append(int(tmpline[i]))

            ## 作業用配列
            for j in range(ymax):
                for i in range(xmax):
                    self.bbb.append(self.aaa[j*xmax+i])

        pyxel.run(self.update, self.draw)

    def update(self):
        ymax = self.ymax
        xmax = self.xmax
        ### 左クリックでbbbを加算、右クリックで減算。0-9の範囲。
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            j = int(( pyxel.mouse_y - msize) / msize )
            i = int(( pyxel.mouse_x - msize) / msize )
            if self.aaa[j*xmax+i] == 0 :
                self.bbb[j*xmax+i] += 1
                if self.bbb[j*xmax+i] == 10 :
                    self.bbb[j*xmax+i] = 0
        if pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT):
            j = int(( pyxel.mouse_y - msize) / msize )
            i = int(( pyxel.mouse_x - msize) / msize )
            if self.aaa[j*xmax+i] == 0 :
                self.bbb[j*xmax+i] -= 1
                if self.bbb[j*xmax+i] == -1 :
                    self.bbb[j*xmax+i] = 9



    def draw(self):
        pyxel.cls(7)

        ymax = self.ymax
        xmax = self.xmax

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
        for j in range(ymax):
            for i in range(xmax):
                if self.aaa[j*xmax+i] > 0 :
                    pyxel.text(int(msize*1.5+i*msize),int(msize*1.5+j*msize),str(self.aaa[j*xmax+i]),0)

        ## 作業中の数字を配置する
        for j in range(ymax):
            for i in range(xmax):
                if self.aaa[j*xmax+i] == 0 and self.bbb[j*xmax+i] > 0 :
                    pyxel.text(int(msize*1.5+i*msize),int(msize*1.5+j*msize),str(self.bbb[j*xmax+i]),3)



App()


