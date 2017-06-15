import turtle
win = turtle.Screen()
t1 = turtle.Turtle()

def isInTrap(x,y,x1,y1,x2,y2):
  minx=min(x1,x2)
  maxx=max(x1,x2)
  miny=min(y1,y2)
  maxy=max(y1,y2)
  if ((minx<x and x<maxx) and (miny<y and y<maxy)):
    return True
  else:
    return False

def drawRectWithFill(x1,y1,x2,y2,color):
  t1.goto(x1,y1)
  t1.fillcolor(color)
  t1.begin_fill()
  t1.goto(x2,y1)
  t1.goto(x2,y2)
  t1.goto(x1,y2)
  t1.goto(x1,y1)
  t1.end_fill()

def checkTrap(x,y):
  if isInTrap(x,y,-200,-200,200,200):
    print "in trap"
    drawRectWithFill(0,0,20,20,"RED")

def keyup():
  pt = t1.pos()
  print("up", pt)
  t1.write(pt)
  t1.forward(50)
  checkTrap(pt[0],pt[1])
  
def keyleft():
  t1.left(45)
def keyright():
  t1.right(45)
def keydown():
  pt = t1.pos()
  t1.back(50)
  checkTrap(pt[0],pt[1])

def quit():
  win.bye()

def addKeys():
  win.onkey(keyup,"Up")
  win.onkey(keyleft,"Left")
  win.onkey(keyright,"Right")
  win.onkey(keydown,"Down")
  win.onkey(quit,"q")

def mousegoto(x,y):
  t1.goto(x,y)
  checkTrap(x,y)

def addMouse():
  win.onclick(mousegoto)

def gamePlay():
  addKeys()
  addMouse()
  win.listen()
  turtle.mainloop()

win.bgpic("mymaze.gif")
gamePlay()