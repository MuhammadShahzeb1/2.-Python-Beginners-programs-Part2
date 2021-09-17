# here we will discuss some more on python files function

f=open("SHahzeb.txt","w")
f.writelines("I am Muhammad Shhzeb\n")
f.writelines("I am cuurently studying in Software Engineering")

f=open("SHahzeb.txt","r+")
print(f.read())

#Will tell how many chcracters are in files
print(f.tell())  #will print total number in a file


#pointing a cursor on given character
f.seek(23)   #will point cursor on 23rd character
print(f.readline())   #print onward from 23rd character


f.close()