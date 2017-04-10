Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> turtle.Sc
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    turtle.Sc
AttributeError: module 'turtle' has no attribute 'Sc'
>>> turtle.Screen()
<turtle._Screen object at 0x0337FF50>
>>> 
=============================== RESTART: Shell ===============================
>>> import turtle
>>> turtle.Screen()
<turtle._Screen object at 0x02756CB0>
>>> wn = turtle.Screen()
>>> t1 = turtle.Turtle()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    t1 = turtle.Turtle()
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 3816, in __init__
    visible=visible)
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2557, in __init__
    self._update()
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2660, in _update
    self._update_data()
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2646, in _update_data
    self.screen._incrementudc()
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 1292, in _incrementudc
    raise Terminator
turtle.Terminator
>>> t1=turtle.Turtle()
>>> t1,forward(100)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    t1,forward(100)
NameError: name 'forward' is not defined
>>> t1.forward(100)
>>> t1.backward(100)
>>> t1.forward
<bound method TNavigator.forward of <turtle.Turtle object at 0x03229570>>
>>> t1.forward(100)
>>> t1.left(90)
>>> t1.forward(100)
>>> t1.left(90)
>>> t1.forward(100)
>>> t1.fo
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    t1.fo
AttributeError: 'Turtle' object has no attribute 'fo'
>>> t1.forward
<bound method TNavigator.forward of <turtle.Turtle object at 0x03229570>>
>>> t1.left(90)
>>> t1.forward(100)
>>> t1.circle
<bound method TNavigator.circle of <turtle.Turtle object at 0x03229570>>
>>> t1.circle(100)
>>> t1.circle
<bound method TNavigator.circle of <turtle.Turtle object at 0x03229570>>
(
>>> t1.circle(95)
>>> t1.circle(99)
>>> t1.circle(98)
>>> t1.circle(97)
t1.circle(95)
>>> t1.circle(96)
>>> t1.circle(94)
>>> t1.circle(93)
>>> t1.circle(92)
>>> t1.circle(91)
>>> t1.circle(90)
>>> t1.right(30)
>>> t1.right(10)
>>> t1.circle(50)
>>> t1.right(90)
>>> t1.right(70)
>>> t1.left(10)
>>> t1.left(10)
>>> t1.circle(50)
>>> t1.circle(50)
>>> wn
<turtle._Screen object at 0x031BF210>
>>> type(wn)
<class 'turtle._Screen'>
>>> type(t1)
<class 'turtle.Turtle'>
>>> wn.setup(500.500)
>>> wn.setup(500.500)
>>> wn.setup(500.100)
>>> wn.setup(500.200)
>>> wn.screensize(500.500)
>>> wn.setup(100.100)
>>> wn.setup(500.100)
>>> wn.setup(100.500)
>>> wn.setup(500.500.0.0\)
	 
SyntaxError: invalid syntax
>>> wn.setup(500.500.0.0)
SyntaxError: invalid syntax
>>> wn.setuo(500,100)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    wn.setuo(500,100)
AttributeError: '_Screen' object has no attribute 'setuo'
>>> wn.setup(500,100)
>>> wn.setup(500,500)
>>> wn.setup(500,500,0,0)
>>> t1.fd(100)
>>> t1.left(180)
>>> t1.fd(200)
>>> t1.lt(90)
>>> t1.rt(90)
>>> wn.setup(500,500,3,3)
>>> wn.setup(1000,1000)
>>> wn.setup(700,700)
>>> t1.rt(90)
>>> ti.lt(180)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    ti.lt(180)
NameError: name 'ti' is not defined
>>> t1.lt(180)
>>> t1.fd(100)
>>> t1.lt(90)
>>> t1.rt(180)
>>> t1.fd(100)
>>> t1.rt(90)
>>> t1.fd(200)
>>> t1.lt(90)
>>> t1.fd(100)
>>> t1.lt(90)
>>> t1.fd(100)
>>> t1.pencolor()
'black'
>>> t1.pencolor(blue)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    t1.pencolor(blue)
NameError: name 'blue' is not defined
>>> t1.pencolor("Blue")
>>> t1.forward(100)
>>> t1.pencolor("emelaldeu")
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    t1.pencolor("emelaldeu")
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2252, in pencolor
    color = self._colorstr(args)
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2696, in _colorstr
    return self.screen._colorstr(args)
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 1158, in _colorstr
    raise TurtleGraphicsError("bad color string: %s" % str(color))
turtle.TurtleGraphicsError: bad color string: emelaldeu
>>> t1.pencolor("Emelaldeu")
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    t1.pencolor("Emelaldeu")
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2252, in pencolor
    color = self._colorstr(args)
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2696, in _colorstr
    return self.screen._colorstr(args)
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 1158, in _colorstr
    raise TurtleGraphicsError("bad color string: %s" % str(color))
turtle.TurtleGraphicsError: bad color string: Emelaldeu
>>> t1.pencolor((0,0,0))
>>> t1.pencolor((0,100,200))
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    t1.pencolor((0,100,200))
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2252, in pencolor
    color = self._colorstr(args)
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2696, in _colorstr
    return self.screen._colorstr(args)
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 1166, in _colorstr
    raise TurtleGraphicsError("bad color sequence: %s" % str(color))
turtle.TurtleGraphicsError: bad color sequence: (0, 100, 200)
>>> t1.pencolor((0,1,1))
>>> t1.pencolor((1,0,0))
>>> t1.pencolor((1,1,1))
>>> t1.pencolor((1,0,1))
>>> wn.colormode(255)
>>> t1.pencolor(()0,200,100)
SyntaxError: invalid syntax
>>> t1.pencolor((0,200,100))
>>> t1.pencolor("Grey")
>>> t1.pencolor((0.5,0.5,0.5))
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    t1.pencolor((0.5,0.5,0.5))
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2252, in pencolor
    color = self._colorstr(args)
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2696, in _colorstr
    return self.screen._colorstr(args)
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 1167, in _colorstr
    return "#%02x%02x%02x" % (r, g, b)
TypeError: %x format: an integer is required, not float
>>> wn.colormode(1.0)
>>> t1.pencolor("Black")
>>> wn.colormode(255)
>>> t1.pencolor((100,100,100))
>>> t1.fd(100)
>>> t1.shape("turtle")
>>> t1.lt(90)
>>> t1.fd(100)
>>> wn.addshape("C:\Users\400T6B\Downloads\rocketshop.gif")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> wn.addshape("C:\\Users\\400T6B\\Downloads\\rocketship.gif")
>>> t1.shape("rocketship")
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    t1.shape("rocketship")
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2776, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named rocketship
>>> t1.shape("C:\\Users\\400T6B\\Downloads\\rocketship.gif")
>>> t1.lt(90)
>>> t1.fd(20)
>>> t1.rt(90)
>>> t1.fd(100)
>>> t1.fd(200)
>>> t1.fd(100)
>>> t1.lt(90)
>>> t1.circle(100)
>>> wn.addshape("C:\Users\400T6B\Downloads\rose.png")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> wn.addshape("C:\\Users\\400T6B\\Downloads\\rose.png")
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    wn.addshape("C:\\Users\\400T6B\\Downloads\\rose.png")
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 1136, in register_shape
    + "Use  help(register_shape)" )
turtle.TurtleGraphicsError: Bad arguments for register_shape.
Use  help(register_shape)
>>> t1.shape("C:\\Users\\400T6B\\Downloads\\rose.png")
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    t1.shape("C:\\Users\\400T6B\\Downloads\\rose.png")
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2776, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named C:\Users\400T6B\Downloads\rose.png
>>> 
