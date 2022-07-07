# taking input for the program to work with

hourly_wage = input('How much are you paid an hour?\n~')
ot_wage = input('How much are you paid an hour during overtime?\n~')
reg_hours = input('How many regular hours did you work so far?\n~')
ot_hours = input('How many overtime hours did you work so far?\n~')
print('Do you know your tax rate? If yes, type in decimal format.')
tax_rate = input('If not, look at a recent paycheck. Divide your takehome pay by gross pay.\n~')

# converting the numbers to something the program can work with
hourly_wage = float(hourly_wage)
ot_wage = float(ot_wage)
reg_hours = float(reg_hours)
ot_hours = float(ot_hours)
tax_rate = float(tax_rate)

# doing the math

reg_pay = hourly_wage * reg_hours
ot_pay = ot_wage * ot_hours

gross = reg_pay + ot_pay
net = gross * tax_rate

# declaring tax brackets for 2022
# 10% = $0 to $10,275
# 12% = @10,275 to $41,775
# 22% = $41,775 to $89,075
# 24% = $89,075 to $170,050
# 32% = $170,050 to $215,950
# 35% = $215,950 to $539,500
# 37% = $539,500 and higher

print('Your hours should get you:\n${0:.2f}'.format(gross))
print('This is how much you\'ll actually get:\n${0:.2f}'.format(net))
taken = gross - net
print('This is how much was taken out:\n${0:.2f}'.format(taken))

yearly_projected = net * 26

if 0 < yearly_projected < 10275:
    print('You should be in the 10% tax bracket')
elif 10275 < yearly_projected < 41775:
    print('You should be in the 12% tax bracket')
elif 41775 < yearly_projected < 89075:
    print('You should be in the 22% tax bracket')
elif 89075 < yearly_projected < 170050:
    print('You should be in the 24% tax bracket')
elif 170050 < yearly_projected < 215950:
    print('You should be in the 32% tax bracket')
elif 215950 < yearly_projected:
    print('You make too much to really care anyway')
