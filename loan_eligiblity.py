age =int(input("enter age:"))
income =int(input("enter income:"))
loan =int(input("enter loan:"))
cibil =int(input("enter cibl:"))

if not (21 <= age <= 60):
    raeason = "rejected due to low age!!"
elif income < 25000:
    raeason = "rejected due to low income!!"
elif loan > 0.5:
    raeason = "rejected due to lone criteria!!"
elif cibil < 700:
    raeason = "rejected due to low cibil score!!"
else:
    raeason = "accepted!!"

print(raeason)
