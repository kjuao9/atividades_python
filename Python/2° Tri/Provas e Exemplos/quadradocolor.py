Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t = turtle.Turtle()
>>> cores = ["red","yellow","blue","green"]
>>> cores
['red', 'yellow', 'blue', 'green']
>>> cores[0]
'red'
>>> cores[1]
'yellow'
>>> cores[2]
'blue'
>>> cores[3]
'green'
>>> for x in range(100):
	t.pencolor(cores[x%4])
	t.forward(x)
	t.left(91)

	
>>> 
>>> t.home
<bound method TNavigator.home of <turtle.Turtle object at 0x7fe188214390>>
>>> t.home()
>>> t.clear()
>>> for x in range(1000):
	t.pencolor(cores[x%4])
	t.forward(x)
	t.left(91)
