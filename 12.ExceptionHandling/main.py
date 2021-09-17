# we will discuss try and catch in exception handling
#mostly ued this concept on web whioe conectiong to internet or connection to DB

print("Enter num 1")
num1 = input()
print("Enter num 2")               # we will intentionally input the string instead of number
num2 = input()

# intentionally commented for execution of next statement
# print("The sum of these two numbers is",
#           int(num1)+int(num2))      # now for execution both values should be integer but we put them as number so it gives us an error
#
# print("My name is Muhammad Shahzeb")   #will not be executed further beacuse stops at line 10 due to error
#

#But we want to print our name in any condition even the above code is giving errors
#so for this purpose to control such errors we use exception handling try cathch blocks:

#now in try we ask the interprater to try this block of code if it deos not execute take this as exception and jumps to the next code.

try:
    print("The sum of these two numbers is",
          int(num1)+int(num2))
except Exception as e:
    print(e)                        #this will take above error as a exception and jumps to the next statement or code and print error as a string


print("My name is Muhammad Shahzeb")


