#1. Basic keyword Argument

def simple_interest(p:float,t:float,r:float):
    si=(p*t*r)/100
    print("simple interest:",si)

simple_interest(p=10000,t=2.5,r=3.5)