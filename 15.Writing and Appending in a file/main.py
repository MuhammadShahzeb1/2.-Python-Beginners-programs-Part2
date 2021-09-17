#in this program we will discuss how to write and append to a file

#creating a file
f=open("Shahzeb.txt","w")     #for creating a new file and writjng into it we use open function and w keywrods already discsuss in intro
f.write("I am Muhammad Shahzeb \n")   #now by using file pointer we can use file write function andstartr writing inside the file
f.write("I love reading Quran\n")

"""
what no to do 
we can not read a file without opening again with r keyword 
like by just writing 
f.read() or f.readlines() after f=open("filename","w")
if we want to open a file we should apply read function first which is  f=open("filename","r")

"""


#reading or showing whats written inside a file
f=open("Shahzeb.txt","r")    #for this we use r to read after opening file again
print(f.read())               #will print what we already write inside a file

#if i keepwriting the same name of file it will delete old data from a file and update it

f.close()
