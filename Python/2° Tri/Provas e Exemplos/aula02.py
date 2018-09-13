Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> print("o valor de x eh: ",x)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    print("o valor de x eh: ",x)
NameError: name 'x' is not defined
>>> print('o valor de x eh: ' x)
SyntaxError: invalid syntax
>>> print('o valor de x eh: 'x)
SyntaxError: invalid syntax
>>> x = 10
>>> print(x)
10
>>> print('O valor de x eh: ',x)
O valor de x eh:  10
>>> 
