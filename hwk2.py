# welcome statement

welcome = '''
Automobile Fuel Cost Calculator

This program may help you decide which car makes
sense for you based on your budget. You will be asked
to enter the MPG for the car you have in mind, the
average number of miles you expect to drive each month,
and the cost per gallon for the fuel.

The program will then calculate the monthly fuel cost.
'''

print(welcome)
# user adds miles per gallon
miles_per_gallon = input('Please enter the miles per gallon:')
miles_per_gallon = float(miles_per_gallon)

# user enters average miles driven per month
miles_per_month = input('Please enter the average number of miles driven per month:')
miles_per_month = float(miles_per_month)

# user enters the current price per gallon
price_per_gallon = input('Please enter the cost of fuel per gallon:')
price_per_gallon = float(price_per_gallon)

fuel_used = miles_per_month / miles_per_gallon
total_cost = fuel_used * price_per_gallon

print('Given price of fuel at ${:.2f}/gallon and {} miles/month traveled:'.format(price_per_gallon, miles_per_month))

print('Gallons of fuel used each month: {0:.1f}'.format(fuel_used))
print('Monthly cost of fuel: ${0:.2f}'.format(total_cost))
