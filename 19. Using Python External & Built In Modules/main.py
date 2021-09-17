#we will discuss how can we use different modules in python

import math
a= math.cos(45)
print(a)           #This will print the cos of 45

#randit
import random      #another module
b= random.randint(0,3)   #this will print any random number between 0 and 3
print(b)

#random module inside a random
c=random.random()*10    #print any number between 0 and 10 and also it will print floating value between 0 and 1 because we use random inside a random
print(c)

#choice inside a random module
# selecting any beloved khalifah
list=["Abu Bakar","Omer","Usman","Ali"]
khalifa=random.choice(list)    #it will select any name from the list randomly
print(khalifa)

