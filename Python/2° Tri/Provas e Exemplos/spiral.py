
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t = turtle.Turtle()
>>> 
for x in range(1000):
	t.pencolor(cores[x%4])
	t.forward(x*2)
	t.left(91)

	
Traceback (most recent call last):
  File "<pyshell#3>", line 3, in <module>
    t.pencolor(cores[x%4])
NameError: name 'cores' is not defined
>>> for x in range(1000):
	t.pencolor(cores[x%4])
	t.forward(x*2)
	t.left(91)

	
Traceback (most recent call last):
  File "<pyshell#5>", line 2, in <module>
    t.pencolor(cores[x%4])
NameError: name 'cores' is not defined
>>> cores("red","blue","yellow","green")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    cores("red","blue","yellow","green")
NameError: name 'cores' is not defined
>>> cores = ("red","blue","yellow","green")
>>> for x in range(1000):
	t.pencolor(cores[x%4])
	t.forward(x*2)
	t.left(91)

	
Traceback (most recent call last):
  File "<pyshell#9>", line 3, in <module>
    t.forward(x*2)
  File "/usr/lib/python3.5/turtle.py", line 1637, in forward
    self._go(distance)
  File "/usr/lib/python3.5/turtle.py", line 1605, in _go
    self._goto(ende)
  File "/usr/lib/python3.5/turtle.py", line 3178, in _goto
    self._pencolor, self._pensize, top)
  File "/usr/lib/python3.5/turtle.py", line 545, in _drawline
    self.cv.coords(lineitem, *cl)
  File "<string>", line 1, in coords
  File "/usr/lib/python3.5/tkinter/__init__.py", line 2312, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".140116348639328"
t.ho0me
turtle.bgcolor("black")
>>> 
>>> import turtle
>>> t = turtle.Turtle
>>> colors = ("red","blue","yellow","green")
>>> t = turtle.Turtle()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    t = turtle.Turtle()
  File "/usr/lib/python3.5/turtle.py", line 3816, in __init__
    visible=visible)
  File "/usr/lib/python3.5/turtle.py", line 2557, in __init__
    self._update()
  File "/usr/lib/python3.5/turtle.py", line 2660, in _update
    self._update_data()
  File "/usr/lib/python3.5/turtle.py", line 2646, in _update_data
    self.screen._incrementudc()
  File "/usr/lib/python3.5/turtle.py", line 1292, in _incrementudc
    raise Terminator
turtle.Terminator
>>> turtle.gbcolor("black")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    turtle.gbcolor("black")
AttributeError: module 'turtle' has no attribute 'gbcolor'
>>> turtle.bgcolor("dark")
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    turtle.bgcolor("dark")
  File "<string>", line 8, in bgcolor
  File "/usr/lib/python3.5/turtle.py", line 1237, in bgcolor
    color = self._colorstr(args)
  File "/usr/lib/python3.5/turtle.py", line 1158, in _colorstr
    raise TurtleGraphicsError("bad color string: %s" % str(color))
turtle.TurtleGraphicsError: bad color string: dark
>>> turtle.bgcolor("black")
>>> for x in range(100):
	t.pencolor(cores[x%4])
	t.circle(x)
	t.left(91)

	
Traceback (most recent call last):
  File "<pyshell#19>", line 2, in <module>
    t.pencolor(cores[x%4])
  File "/usr/lib/python3.5/turtle.py", line 2257, in pencolor
    return self._color(self._pencolor)
AttributeError: 'str' object has no attribute '_color'
>>> import turtle
>>> t = turtle.Turtle()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    t = turtle.Turtle()
  File "/usr/lib/python3.5/turtle.py", line 3816, in __init__
    visible=visible)
  File "/usr/lib/python3.5/turtle.py", line 2557, in __init__
    self._update()
  File "/usr/lib/python3.5/turtle.py", line 2660, in _update
    self._update_data()
  File "/usr/lib/python3.5/turtle.py", line 2646, in _update_data
    self.screen._incrementudc()
  File "/usr/lib/python3.5/turtle.py", line 1292, in _incrementudc
    raise Terminator
turtle.Terminator
>>> turtle.bgcolor("black")
>>> colors = ("red","blue","yellow","green")
>>> for x in range(100):
	t.pencolor(cores[x%4])
	t.forward(x)
	t.left(90)

	
Traceback (most recent call last):
  File "<pyshell#25>", line 2, in <module>
    t.pencolor(cores[x%4])
  File "/usr/lib/python3.5/turtle.py", line 2257, in pencolor
    return self._color(self._pencolor)
AttributeError: 'str' object has no attribute '_color'
>>> for x in range(100):
	t.pencolor(colors[x%4])
	t.forward(x)
	t.left(90)

	
Traceback (most recent call last):
  File "<pyshell#27>", line 2, in <module>
    t.pencolor(colors[x%4])
  File "/usr/lib/python3.5/turtle.py", line 2257, in pencolor
    return self._color(self._pencolor)
AttributeError: 'str' object has no attribute '_color'
>>> for x in range(1000):
	t.pencolor(colors[x%4])
	t.forward(x)
	t.left(91)

	
Traceback (most recent call last):
  File "<pyshell#29>", line 2, in <module>
    t.pencolor(colors[x%4])
  File "/usr/lib/python3.5/turtle.py", line 2257, in pencolor
    return self._color(self._pencolor)
AttributeError: 'str' object has no attribute '_color'
>>> for x in range(1000):
	t.pencolor(cores[x%4])
	t.forward(x)
	t.left(91)
KeyboardInterrupt
>>> for x in range(1000):
	t.pencolor("colors"[x%4])
	t.forward(x)
	t.left(90)

	
Traceback (most recent call last):
  File "<pyshell#31>", line 2, in <module>
    t.pencolor("colors"[x%4])
  File "/usr/lib/python3.5/turtle.py", line 2257, in pencolor
    return self._color(self._pencolor)
AttributeError: 'str' object has no attribute '_color'
>>> 
for x in range(100)
	t.forward(x)
	t.left(90)
	
SyntaxError: invalid syntax
>>> for x in range(1000):	
	t.forward(x)
	t.left(91)

	
Traceback (most recent call last):
  File "<pyshell#34>", line 2, in <module>
    t.forward(x)
TypeError: forward() missing 1 required positional argument: 'distance'
>>> for x in range(1000):
	t.forward(100)
	t.left(90)

	
Traceback (most recent call last):
  File "<pyshell#36>", line 2, in <module>
    t.forward(100)
TypeError: forward() missing 1 required positional argument: 'distance'
>>> 
=============================== RESTART: Shell ===============================
>>> cores = ["red","yellow","blue","green"]
>>> import turtle
>>> 
t = turtle.Turtle()
>>> turtle.speed("fast")
>>> for x in range(1000):
	t.pencolor(cores[x%4])
	t.forward(x)
	t.left(90)
