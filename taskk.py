Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> p=int(input("enter principal:"))
enter principal:150
>>> r=int(input("enter rate:"))
enter rate:5
>>> t=int(input("enter time:"))
enter time:3
>>> si=(p*r*t)/100
>>> print("simple interest=",si)
simple interest= 22.5
>>> a=int(input("enter first number:"))
enter first number:45
>>> b=int(input("enter second number:"))
enter second number:35
>>> print("maximum number is:",max(a,b))
maximum number is: 45
>>> print(1\n2\n3\n4\n5)
SyntaxError: unexpected character after line continuation character
>>>  print(1,2,3,4,5)
 
SyntaxError: unexpected indent
>>> print(1,2,3,4,5)
1 2 3 4 5
>>> s=input("enter a string:")
enter a string:5
>>> print("length of string=",len(s))
length of string= 1
>>> msg="welcome user"
>>> print(msg)
welcome user
>>> s=input("enter a string:")
enter a string:7
>>> print("first charcter:",s[0])
first charcter: 7
>>> s=input("enter a string:")
enter a string:45
>>> print("last character:",s[-1])
last character: 5
>>> num=int(input("enter a number:"))
enter a number:33
>>> if num >0:
	print("positive number")
	else:
		
SyntaxError: invalid syntax
>>> a=int(input("enter first number:"))
enter first number:45
>>> b=int(input("enter second number:"))
enter second number:33
>>> c=int(input("enter third number"))
enter third number:18
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    c=int(input("enter third number"))
ValueError: invalid literal for int() with base 10: ':18'
>>> enter third number18
SyntaxError: invalid syntax
>>> n=int(input("enter a number:"))
enter a number:93
>>> print("square=",n*n)
square= 8649
>>> 