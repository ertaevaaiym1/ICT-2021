'''Exercise1: Tax and Tip'''
paid = int(input("Enter the amount to be paid: "))
tip = 1.8 * paid
tax = 0.1 * paid
total = paid + tip + tax
x = round(total, 2)
print(x)

'''Enter the amount to be paid: 10
29.0'''

'''Exercise2: Sum of the First n Positive Integers'''
n = int(input("Enter a positive number: "))
sum = n * (n + 1)/2
print(sum)

'''Enter a positive number: 10
55.0'''

'''Exercise3: Widgets and Gizmos'''
numOfWidgets = int(input("Enter your number of widgets: "))
numofGizmos = int(input("Enter your number of Gizmos: "))

weightOfWidgets = numOfWidgets * 75
weightOfGizmos = numofGizmos * 112

totalWeight = weightOfGizmos + weightOfWidgets             
x = str(totalWeight)
print (x)


'''Enter your number of widgets: 10
Enter your number of Gizmos: 10
1870'''


'''Exercise4: Compound Interest'''
sum1 = int(input("Enter amount of money in the first year: " ))
Year1 = sum1 * 0.04
print(Year1)
sum2 = int(input("Enter amount of money in the second year: " ))
Year2 = sum2 * 0.04
print(Year2)
sum3 = int(input("Enter amount of money in the third year: "))
Year3 = sum3 * 0.04
print(Year3)
total = Year1 + Year2+ Year3
print(round(total, 2))

'''Enter amount of money in the first year: 2021
80.84
Enter amount of money in the second year: 2022
80.88
Enter amount of money in the third year: 2023
80.92
242.64'''



'''Exercise5: Fuel Efﬁciency'''
miles_per_gallon = int(input("Enter the number of fuel use in America"))
liters_kilometres = int(input("Enter the number of fuel use in Canada "))
mpg_to_lk = (100 * 3.785411784)/(1.609344 * miles_per_gallon)
print(mpg_to_lk)


'''Enter the number of fuel use in America: 500
Enter the number of fuel use in Canada: 500
0.4704291666666666'''

'''Exercise6: Distance Units'''
cm = int(input("Enter the number in centimetres: "))
m = cm / 100
print(m)
km = cm / 100000
print(km)
mi = cm * 0.0000062137119223667
print(mi)


'''Enter the number in centimetres: 500
5.0
0.005
0.0031068559611833503'''

'''Exercise7: Area and Volume'''
import math
r = int(input("Enter the radius: "))
pi = 3.14159265359
area = pi * r**2
print(area)
volume = (4*pi*r**3)/3
print(volume)

'''Enter the radius: 56
9852.03456165824
735618.5806038153'''