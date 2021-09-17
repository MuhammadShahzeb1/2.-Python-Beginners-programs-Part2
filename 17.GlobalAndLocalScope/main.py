# we will discuss about the global and local varaible and scopes

#global variable : is the variable that places outside the Function or Class
#local variable : is the variable that places inside the function or Class


gv1=12   #global variable as its outside the function
def func1():
    lv= 90       #local variable as its inside the function
    print(lv)

print(gv1)      #will print global variable
func1()       #print local variable


#Accessing Global variable inside function:

gv2=13
def func2():
    #gv2=gv2+45       #   This will not add 45 to the global variable because Python doesnt give permission to access global variable inside local variable(function)
    # Now if i want to chnge the global variable than i have to put global to acess it
    global gv2  # syntax global variable name
    gv2 = gv2 + 4
    print(gv2)  # will print global variable

func2()


#Accessing global/local variable in nested function (function inside a function)

x = 89
def shabby():
    x = 20
    def zeeshu():
        global x                        #if we access global variable inside a nested function than it will jump outside the both or main loop to check global variable
        x = 88
    # print("before calling zeeshu()", x)
    zeeshu()
    print("after calling zeeshu()", x)

shabby()
print(x)
