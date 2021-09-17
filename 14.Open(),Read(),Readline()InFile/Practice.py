#we will discuss sbout the file
#open,read,readline etc

f=open("MShahzeb")#this open function will the file    syntax f = open()  f is a file pointer for openning to perform operations
# f=open("MShahzeb" ,"r")    read default
# f=open("MShahzeb","rt")   read text defaull
# f=open("MShahzeb","rb")    read binary this will remove spaces etc

content=f.read()     #now we make anoother variable called content from which  further apply operations
print(content)

# content=f.read(8)     #now it will print the first 3 chahracters in file  syntax read(no of characyers you want to print string slicing concept)
# print(content)        #comment out above if want to print out fist 3 values?character

#if we want to print every character  line by line we can use for statement

for line in content:
    print(line)                #print each chahracter on one line

#to print out every complete line
# print(f.readline()) #but this directly assigned to file pointer so print out new line every time as value updated
# #to execute printline commented the above function
# print(f.readline())      #new line

#if we want to print all lines in a list than we can use readlines() function
print(f.readlines())       #it will return empty list if above is not commented out  because once it read it dumps all chaharacters
f.close()          #always close files after completing function

#when we fetch any character from file it basically use Cut(delete from origralspurce) Function




