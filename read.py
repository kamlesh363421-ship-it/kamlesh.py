"""1. Read()
f=open("one.txt","r")
data=f.read()
print("File content:",data)
f.close()"""

"""2.readline()
f=open("one.txt","r")
line1=f.readline()
line2=f.readline()
line3=f.readline()
print("line1:",line1)
print("line2:",line2)
print("line3:",line3)
f.close()"""

"""3.readlines()
f=open("one.txt","r")
lines=f.readlines()
print("list of lines:",lines)
print("number of lines:",len(lines))
f.close()"""

"""4.strip()
f=open("one.txt","r")
lines=f.readlines()
print(lines[1].strip())
f.close()"""

#5.char()
f=open("one.txt","r")
data=f.read(10)
print("first part:",data)
f.close()