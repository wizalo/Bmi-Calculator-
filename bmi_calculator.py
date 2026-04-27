w = float(input("weight(kg) :  "))
h = float(input("Height(cm) :  "))

bmi = w/(h/100)**2

print ("Weight",int(w),"kg")
print ("Height",int(h),"cm")
print ("BMI",(f"{bmi:.2f}"))

if not (bmi >= 18.5):
    print("You are Underweight")
elif  bmi < 25.0 :
    print("You are Standard weight")
elif bmi < 30.0 :
    print("You are Overweight")     
elif bmi < 35.0 :
    print("You are Obese class I")
elif bmi < 40.0 :
    print("You are Obese class II")     
elif bmi >= 40 :
    print("You are Obese class III")