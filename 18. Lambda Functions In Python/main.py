#we will discuss about the lambda function

#
# def add(x,y):
#     return x+y
#
# print(add(3,4))

# SO basically lambda shorten the function and make it one liner

add= lambda x,y:x+y
print(add(8,90))

#
# def a_first(a):
#     a[1]
# a=[[21,34],[90,89],[78,45]]
# a.sort(key= a_first(a))
# print(a)

a=[[21,34],[90,89],[78,45]]
a.sort(key= lambda x:x[1])   #implementation    instead using of function we directly use lambda in a code
print(a)

