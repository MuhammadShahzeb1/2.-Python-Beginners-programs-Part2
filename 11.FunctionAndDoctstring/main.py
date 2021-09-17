# in this program we will discuss about function

#the basic use of functions is that we use that chunk of code repeatidly by just calling it instead of writing whole code again
#thee are some built in functions as well

#built in function
a=4
b=3
c=sum((a,b))    #so this is the built in function    We have to put tuple or list inside sum function
print(c)

#now we will dicuss User functions
def func():
    print("hi ou are inside the function")
print(func())  # will retrun none value after execution

func() # we can print many times instead of printing again and again
func()

# Now if we want to store our function value in any variable than we have to use return

# function without return value
def function(a, b):
    avg = (a + b) / 2
    print(avg)


function(13, 15)  # calling a function without return
v = function(12, 45)
print(v)  # will print none


# the above print None because we can not set the return value that what function has to return while executing


# function with return value

def function1(a, b, c):
    avg2 = (a + b + c) / 3
    print(avg2)
    return avg2


m = function1(9, 6, 9)
print(m)  # will print avg of 3 numbers  so basically we understand that return used to store the value of function in any variable etc.
