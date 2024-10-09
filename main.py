# Programmers: Harry Li, Cameron Combariza
# Course:  CS151 sec 06
# Due Date: 10//2024
# Lab Assignment: Mobile Subscription Fees
# Problem Statement: Write a program to determine how much a customer owes their mobile phone provider based on their subscription package and amount of data used.
# Data In: plan chosen and the price and amount of data they need Additionally
# Data Out: The total cost based on the user input for that month

#Output a brief description about what the program does
print('This program is meant to output your total cost based on your plan and how many additional data you need for one month.')

#Create needed variables
additional_cost = 0
total_cost = 0
initial_cost = 0

#Prompt user to input the package green, blue, or purple and set it to all lowercase
package = str(input('Enter your package: '))

#if user doesnt enter a valid input, prompt user to enter a valid input
while package.lower() != 'green' and package.lower() != 'blue' and package.lower() != 'purple':
    package = str(input('Enter a valid package, green, blue or purple: '))

#Prompt user to input if they have a coupon when they chose green package
if package.lower() == 'green':
    coupon = str(input('Do you have a coupon: '))
    #if user doesnt enter a valid input, prompt user to enter a valid input
    while coupon.lower() != 'yes' and coupon.lower() != 'no':
        coupon = str(input('Please enter yes or no: '))

#if package doesn't equal purple prompt user to input if they want additional data and see if the input entered is a digit or if they enter a decimal round up to the next whole number
if package.lower() != 'purple':
    additional_data = float(input('How many additional data you need for one month: '))
    more_data = additional_data % 1
    if more_data > 0:
        additional_data = additional_data // 1
        additional_data += 1
    while  additional_data < 0:
        additional_data = float(input('Please enter an amount equal to or more than 0: '))
        more_data = additional_data % 1
        if more_data > 0:
            additional_data = additional_data // 1
            additional_data += 1
#Set the values for the variables based on the plan chosen
if package.lower() == 'green' and coupon.lower() == 'yes':
    initial_cost = 49.99
    additional_cost = 15
    total_cost = initial_cost + (additional_cost * additional_data)
    if total_cost >= 75:
        total_cost -= 20
elif package.lower() == 'green':
    initial_cost = 49.99
    additional_cost = 15
    total_cost = initial_cost + (additional_cost * additional_data)
elif package.lower() == 'blue':
    initial_cost = 70
    additional_cost = 10
    total_cost = initial_cost + (additional_cost * additional_data)
else:
    total_cost = 99.95
print (f'your total cost is: {total_cost:.2f}')
