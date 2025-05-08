drinkBill=0
foodBill=0
drinkBill = float(input("Enter the drink bill here: "))
foodBill = float(input("Enter the food bill here: "))

totalBeforeTax = foodBill + drinkBill
tax = totalBeforeTax * 0.062
totalAfterTax = totalBeforeTax + tax
tip = totalAfterTax * 0.15
totalAfterTip = totalAfterTax + tip

print('The total for food and drink is: ', round(totalBeforeTax,2))
print('The total after tax is: ', round(totalAfterTax,2))
print('The total after tip is: ', round(totalAfterTip,2))