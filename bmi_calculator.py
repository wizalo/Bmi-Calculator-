

w = float(input("weight(kg) :  "))
h = float(input("Height(cm) :  "))

bmi = w/(h/100)**2


print ("Weight",int(w),"kg")
print ("Height",int(h),"cm")
print ("BMI",bmi)

if not (bmi >= 18.5):
    print("You are Underweight")
elif  18.5 < bmi <= 24.9:
    print("You are Standard weight")
elif 25 <= bmi <= 29.9:
    print("You are Overweight")     
elif 30 <= bmi <= 34.9:
    print("You are Obese class I")
elif 35 <= bmi <= 39.9:
    print("You are Obese class II")     
elif bmi >= 40:
    print("You are Obese class III")