#activity4
name=(input("Enter name"))
h=float(input("Enter ur height in cm"))
w=float(input("Enter ur weight in kg"))
bmi= w/(h/100)**2
print(name,"your bmi is",bmi)

if bmi <= 18.4 :
    print(name, "you r underweight")
elif bmi <= 24.5 :
    print(name, "You are healthy")
elif bmi <= 29.9 :
    print(name, "You r overweight")
elif bmi <= 34.9 :
    print(name, "you u severely overweight")
elif bmi <= 39.9 :
    print(name, "you r obese")
else:
    print(name, "you r severely obese")