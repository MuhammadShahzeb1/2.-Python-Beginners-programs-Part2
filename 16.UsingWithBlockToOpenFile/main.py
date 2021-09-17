#In this program we will cover How to open and close files using WithBlock

#With automatically open and close file when we use with block we dont need to close file its automatically closing after execuions

with open("Shahzeb.txt","r+") as f:  # syntax  with open ("na,e of file","operation") as Varaible(_file handler)name
    f.write("I am servant of Muhammad SAAW\n")
    print(f.readline())

#the above with block does the same work as given below code .
"""
f=open("Shahzeb.txt","r+")
f.write("I am Muhammad Shahzeb")
print(f.readline())
f.close()
"""

