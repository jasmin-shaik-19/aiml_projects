# ------file open and then write the file ----------------------
"""
f=open("demo.txt","w")
print(f.write("jasmin\n"))
l=["python\n","java\n","c\n"]
f.writelines(l)
"""
#------------to read the file -----------------

#f=open("demo.txt","r")
#print(f.read())
#print(f.read(2))
#print(f.readline())
#print(f.readlines())

#---------properties of a file -------------------
"""
print(f.name)
print(f.mode)
print(f.readable())
print(f.writable())
f.close()
print(f.closed)
"""
#----------file open and then read the file --------------------------
"""
f=open("demo.txt","r")
print(f.read())

#----------- file open and then append the file ------------------------

f=open("demo.txt","a")
var=f.write(" hello")
print(var)

#-----------exclusive file will create a new file and returns error if file exists ---------------

f=open("demo.txt","x")

f.close()
"""

#---------------- with statement or bllock -----------------

with open("demo.txt","w") as f:
    f.write("hello")
print(f.closed)