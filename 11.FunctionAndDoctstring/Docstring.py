
#Now we will discuss Docstring inside a functions
#the prupose of docstring is to give identity to the function or sometimes when we have hundreds of function it helps us to recognise that for what purpose we have created this

def square(a):
    """ This function will print out the square of a number  """
    a=float(input("enter number"))
    ans=a*a
    print(ans)
    return ans

print(square.__doc__)   #will printout the docstirng inside the function
