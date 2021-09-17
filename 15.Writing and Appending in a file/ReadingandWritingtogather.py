# here we will discuss how can we read and write using same method

#it will read and write in a same time instead of opening again and again

f=open("Shahzeb.txt","r+")   #r+ is used to read and write togather
print(f.read())
f.write("I want to become a Muttaqi and DataScientist\n")
f.writelines("and a Storyteller")


f.close()