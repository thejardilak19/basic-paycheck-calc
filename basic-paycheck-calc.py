#project done just for fun

print('Welcome. What would you like to do?')
info = input('1 : Calculate wages\n2 : Perform a simple tax bracket analysis'
             '\n')

hourly_wage = input('How much are you paid an hour?\n:')
overtime_wage = input('How much are you paid an hour on overtime?\n:')
hourly_wage = float(hourly_wage)
overtime_wage = float(overtime_wage)


reg_hours = input('How many regular hours worked?\n:')
ot_hours = input('How many overtime hours?\n:')

reg_hours = float(reg_hours)
ot_hours = float(ot_hours)
total = 0
reg_pay = (reg_hours * hourly_wage)
ot_pay = (ot_hours * overtime_wage)

total = total + reg_pay + ot_pay
after_tax = total * 0.8549
taken = total - after_tax

after_tax = round(after_tax, 2)
taken = round(taken, 2)

print('After tax, you\'re getting:')
print('$' + str(after_tax))
print('You were shafted for:')
print('$' + str(taken))

tax_analysis = input('Would you like to perform a tax analysis, on how much you\'re projected to make in a year, including what tax bracket you\'re in? \n(y/n):')
elif tax_analysis == 'n'
