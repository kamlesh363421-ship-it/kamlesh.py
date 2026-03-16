"""1.Basic positional argument

def add(a,b):
    print("a=",a)
    print("b=",b)
    return a+b
result = add(2,5)
print("sum=",result)"""

"""2.student information

def studentinfo(name,roll,marks):
    print("name:",name)
    print("rollno:",roll)
    print("marks:",marks)
    
studentinfo("ck",45,99)"""

#3.simple interest

def simple_interest(p,r,n):
    si=(p*r*n)/100
    print("simple interest:",si)
simple_interest(10000,2,2)
simple_interest(50000,1.2,3)
    