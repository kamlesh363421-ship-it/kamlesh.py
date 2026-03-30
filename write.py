"""1.write()
f=open("one.txt","w")
f.write("Hello student\n")
f.write("Welcome to python dile handling.")
f.write("learning is fun!\n")
f.close()"""

"""2.writelines
f=open("topics.tex","w")
line=[
"python programing\n",
"error handling\n",
"file handling\n",    
]
f.writelines(line)
f.close()"""

#3.apend()
f=open("topics.tex","w")
line=[
"python programing\n",
"error handling\n",
"file handling\n",    
]
f.writelines(line)
f.close()