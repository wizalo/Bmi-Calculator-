

w = float(input("weight(kg) :  "))
h = float(input("Height(cm) :  "))

bmi = w/(h/100)**2


print ("Weight",int(w),"kg")
print ("Height",int(h),"cm")
print ("BMI",bmi)

if not (bmi >= 18.5):
    print ("You are Underweight")
if bmi >= 18.6 and bmi <= 24.9:
    print ("You are Normal weight")
if bmi >= 25.0 and bmi < 29.9:
    print ("You are overweight")  
if bmi >= 30.0 and bmi < 34.9:
    print ("You are Obesity class I") 
if bmi >= 35.0 and bmi < 39.9:
    print ("You are Obesity class II")  
if bmi >= 40.0:
    print ("You are Obesity class III")
