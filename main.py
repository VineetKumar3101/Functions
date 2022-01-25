print("\n-----------------------------------------------------")

print("syntax of Function")

"""def Functionname(Arguments):
    Function Body
    [return statement]  optional"""

print("\n-----------------------------------------------------")

#to print a star

def printstar(n):
    for i in range(n):
        print("*",end=' ')
print(printstar(10))


print("\n-----------------------------------------------------")

# to print sum
def sum(a,b):
    return a+b
print(sum(6,7))

print("\n-----------------------------------------------------")

#Factorial
def facti(z):
    fact=1
    for i in range(2,z+1):
        fact=fact*i
    return fact
print("The Factorial is = ",facti(9))


s=facti(9)+facti(10)
print("The Factorial is = ", s)

print("\n-----------------------------------------------------")

print("DEFAULT ARGUMENTS")

print("\n-----------------------------------------------------")

#default Argument with a fixed value

def facti(z=3):
    fact=1
    for i in range(2,z+1):
        fact=fact*i
    return fact
print("The Factorial is = ",facti(10))

print("\n-----------------------------------------------------")

print(" KEYWORD ARGUMENTS ")

print("\n-----------------------------------------------------")

#name and student

def d(n,m):
    print("Student name = ",n)
    print("Marks = ",m)

print(d("Vineet",99.5))

#keywordargument

print(d(m=90,n="Anshu"))


print("\n-----------------------------------------------------")

print(" VARIABLE LENGTH ARGUMENTS ")

print("\n-----------------------------------------------------")

#Argument to do sum of n numbers

def s(a,*b):
    res=a
    print(a)
    print(b)
    for i in b:
        res=res+i
    return res


print(s(9,8,7,6,6,78,85,2,7,8,6,3232,4,5,3,2,21,12,2,2,2,1,2,2,2))

print("\n-----------------------------------------------------")