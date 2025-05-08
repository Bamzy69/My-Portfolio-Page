payPerHour=0
contractHours=0
hoursWorked=0
extraHoursWorked=0

payPerHour=float(input("Enter your pay per hour: "))
contractHours=float(input("Enter the contracted hours: "))
hoursWorked=float(input("Enterovertime hours worked: "))
extraHoursWorked=float(input("Enter extra hours worked(double time): "))

overtimePay = hoursWorked * (payPerHour * 1.5)
doubletimePay = extraHoursWorked * (payPerHour * 2)
regularPay = contractHours * payPerHour
totalpay = regularPay + overtimePay + doubletimePay

if hoursWorked <=0:
    totalPay = regularPay
else:
     totalPay = regularPay + overtimePay + doubletimePay
        
if extraHoursWorked <= 0: 
    totalPay = overtimePay + regularPay
else:
    totalpay = regularPay + overtimePay + doubletimePay
            
if hoursWorked > 0 and extraHoursWorked > 0:
    totalpay = regularPay + overtimePay + doubletimePay

    print('Regular pay is: $',round(regularPay,2))
    print('Total pay is: $',round(totalPay,2))