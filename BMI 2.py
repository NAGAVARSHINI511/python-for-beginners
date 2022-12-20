
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi=round(weight/(height**2))
if bmi<=18.5:
    print(f"Your BMI is {bmi}, you are under weight. ") #bmi iss body mass index of a person
elif bmi<=25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi<=30:
    print(f"Your BMI is {bmi}, you are slightly over weight.")
elif bmi<=35:
    print(f"Your BMI is {bmi}, you are obese.")
elif bmi<=35:
    print(f"Your BMI is {bmi}, you are clinicakky obese.")
