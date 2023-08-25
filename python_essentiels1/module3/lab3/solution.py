income = float(input("Enter the annual income: "))

if income <= 85528:
    tax = income*18/100 - 556.02
else :
    tax = 14839.02 + (income-85528)*32/100


if tax < 0:
    tax=0.0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
