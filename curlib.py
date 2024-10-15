#
# curses library class
#

import curses as cs

class lcurs():
    stdscr=None
    lastkey=''
    dstwin=None
    stdscrY=None
    stdscrX=None
    atrText=None
    stock_stdscr=None
    dspLocY=0
    dspLocX=0
    winscr=[]
    padscr=[]
    color1=None
    color2=None
    def __init__(self):
        self.stdscr=cs.initscr()
        cs.start_color()
        cs.init_pair(1,cs.COLOR_BLUE,cs.COLOR_YELLOW)
        self.color1=cs.color_pair(1)
        cs.init_pair(2,cs.COLOR_YELLOW,cs.COLOR_GREEN)
        self.color2=cs.color_pair(2)
        cs.noecho()
        cs.cbreak()
        self.stdscr.keypad(True)
        self.stdscrY, self.stdscrX = self.stdscr.getmaxyx()
        self.stock_stdscr=self.stdscr
    #
    def dspString(self,x,y,s):
        self.dspLoxX=x
        self.dsoLocY=y
        if self.atrText==None:
            self.stdscr.addstr(y,x,s)
        else:
            self.stdscr.addstr(y,x,s,self.atrText)
    #
    def getKey(self):
        self.lastkey=self.stdscr.getkey()
        return self.lastkey
    #
    def getString(self,x,y,nlen):
        self.dspLoxX=x
        self.dsoLocY=y
        cs.echo()
        str=self.stdscr.getstr(y,x,nlen)
        cs.noecho()
        return str
    #
    def refresh(self):
        self.stdscr.refresh()
    #
    def edwin(self):
        cs.endwin()
    #
    def setTextatr(self,prm):
        self.atrText=prm
    #
    def addNewWin(self,akey,sx,sy,wx,wy):
        win=cs.newwin(wy,wx,sy,sx)
        self.winscr.append([akey,win,sx,sy,wx,wy])
        return win
    #
    def addNewPad(self,akey,wx,wy):
        pad=cs.newpad(wy,wx)
        self.padscr.append([akey,pad,wx,wy])
        return pad
    #
    def padRefresh(self,winkey,pad,x,y):
        ret=None
        for w in self.winscr:
            if w[0]==winkey:
                tx,ty,wx,wy=w[2:6]
                pad.refresh(y,x,ty,tx,ty+wy-1,tx+wx-1)
    #
    def setDefault(self,win):
        self.stdscr=win
    #
    def resetDefault(self):
        self.stdscr=self.stock_stdscr
    #
    def clearWindow(self):
        self.stdscr.clear()
        self.stdscr.refresh()
    #
    # getWindow
    def getWindow(self,key):
        ret=None
        for w in self.winscr:
            if w[0]==key:
                ret=w[1]
        return ret
    #
    def getPad(self,key):
        ret=None
        for p in self.padscr:
            if p[0]==key:
                ret=p[1]
        return ret

if __name__=="__main__":
    lcs=lcurs()
    str=lcs.getString(5,10,10)
    lcs.dspString(5,11,str)
    c=lcs.getKey()
    win=lcs.addNewWin('key1',0,3,20,6)
    lcs.setDefault(win)
    lcs.refresh()
    str=lcs.getString(8,3,10)
    lcs.setTextatr(lcs.color2)
    lcs.dspString(8,4,str)
    c=lcs.getKey()
    lcs.setTextatr(None)
    pad=lcs.addNewPad('pkey1',100,50)
    lcs.setDefault(pad)
    lcs.dspString(5,1,'Test Pad 1 !!')
    lcs.dspString(5,2,'Test Pad 2 !!')
    lcs.padRefresh('key1',pad,0,0)
    c=lcs.getKey()
    lcs.resetDefault()
    lcs.refresh()
    c=lcs.getKey()
    lcs.clearWindow()
    c=lcs.getKey()
    lcs.edwin()

