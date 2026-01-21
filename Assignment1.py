Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Welcome")
Welcome
>>> print("Rajesh Kumar \nFlat No. 101,Sunshine Apartment \nMG Road,Sector 15 \nRajkot, \nPincode:360004 \nIndia.")
Rajesh Kumar 
Flat No. 101,Sunshine Apartment 
MG Road,Sector 15 
Rajkot, 
Pincode:360004 
India.
>>> a=150
>>> b=120.50
>>> print(a+b)
270.5
>>> print(a-b)
29.5
>>> print(a*b)
18075.0
>>> print(a/b)
1.2448132780082988
>>> r=float(input("Enter radius: "))
Enter radius: 150
>>> area=3.14*r*r
>>> circumference=2*3.14*r
>>> print("Area Of Circle =",area)
Area Of Circle = 70650.0
>>> print("Circumference Of Circle =",Circumference)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print("Circumference Of Circle =",Circumference)
NameError: name 'Circumference' is not defined
>>>  print("Circumference Of Circle =",Circumference)
 
SyntaxError: unexpected indent
>>> print("Circumference of Circle =",circumference)
Circumference of Circle = 942.0
>>> p=float(input("Enter Principal:"))
Enter Principal:200
>>> r=float(input("Enter Rate of Interest: "))
Enter Rate of Interest: 20
>>> t=float(input("Enter Time(years): "))
Enter Time(years): 2
>>> SI = (p*r*t)/100
>>> print("Simple Interest =",SI)
Simple Interest = 80.0
>>> length=float(input("Enter length: "))
Enter length: 50
>>> width=float(input("Enter width: "))
Enter width: 25
>>> perimeter=2*(length+width)
>>> print("Perimeter of Rectangle =",perimeter)
Perimeter of Rectangle = 150.0
>>> length=float(input("Enter length: "))
Enter length: 150
>>> width=float(input("Enter width: "))
Enter width: 50
>>> area = length*width
>>> perimeter=2*(length+width)
>>> print("Area of Rectangle =",area)
Area of Rectangle = 7500.0
>>> print("Perimeter of Rectangle =",perimeter)
Perimeter of Rectangle = 400.0
>>> a=float(input("Enter side a: "))
Enter side a: 15
>>> b=float(input("Enter side b: "))
Enter side b: 20
>>> c=float(input("Enter side c: "))
Enter side c: 25
>>> perimeter = a+b+c
>>> print("Perimeter of Triangle =",perimeter)
Perimeter of Triangle = 60.0
>>> side=float(input("Enter side: "))
Enter side: 150
>>> area=side*side
>>> perimeter=4*side
>>> print("Area of Square =",area)
Area of Square = 22500.0
>>> print("Perimeter of Square =",perimeter)
Perimeter of Square = 600.0
>>> side=float(input("Enter side: "))
Enter side: 100
>>> perimeter=4*side
>>> print("Perimeter of Square =",perimeter)
Perimeter of Square = 400.0
>>> 