#a collection of instructions
#a collections of code
def function1():
    print("ahhhh")
    print("ahhhh 1")
print("this is outside the function")
function1()

#a mapping
#input or an argument
def function2(x):
    return 2* x
a= function2(3)
#a return value or output
print(a)
b=function2(4)
print(b)
c=function2(5)
print(c)

def function3 (x, y):
    return x+ y
e= function3(1, 2)
print(e)

def function4(x):
    print (x)
    print ("still in this function")
    return 3*x
f = function4 (4)
print (f)

def function5(some_argument):
    print(some_argument)
    print("weee")
f=function5(4)

#BMI calculator
name1 ="YK"
height_m1=2
weight_kg1=90

name2 = "YK's sister"
height_m2 = 1.8
weight_kg2= 70

name3 = "YK's brother"
height_m3 = 2.5
weight_kg3 = 160

def bmi_calculator( name, height_m, weight_kg):
    bmi = weight_kg / (height_m **2)
    print ("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + " is not overweight"
    else:
        return name + "is overweight"
result1 = bmi_calculator (name1, height_m1, weight_kg1)
result2 = bmi_calculator(name2, height_m2, weight_kg2)
result3 = bmi_calculator(name3, height_m3, weight_kg3)

print(result1)
print(result2)
print(result3)

#Convert miles into km

miles1= 40
miles2= 100

def convert ( miles):
   return 1.6 * miles
convert1 = convert(miles1)
convert2 = convert( miles2)
print(convert1)
print(convert2)








