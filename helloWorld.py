print ("hello world")
print ("Lets start working")
x=3
print(x)

v1= "first string"
v2="second string"

temp=v1
v1=v2
v2=temp
print(v1)
print (v2)

a="this tutorial was awesome"
print(a)

y=1
b=2
if y<b:
    print ("y is less than b")
    print("a is definetly less than b")
print ("not sure if y is less than b")

c=5
d=4
if c<d:
    print("c is less than d")
else:
    print("c is NOT less than d")
print ("outside the if block")

e=9
f=8
if e<f:
    print("e is less than f")
elif e==f:
    print("e is equal to f")
elif e>f+10:
    print ("e is greater than f by more than 10")
else:
    print("e is greater than f")

g=7
h=8
if g<h:
    print("g is less than h")
else:
    if g==h:
        print("g is equal to h")
    else:
        print("g is greater than h")

name = "Mike"
height_m = 2
weight_kg =90

bmi = weight_kg / (height_m **2)
print ("bmi: ")
print (bmi)
if bmi < 25:
    print(name)
    print("is not overweight")
else:
    print(name)
    print("is overweight")




