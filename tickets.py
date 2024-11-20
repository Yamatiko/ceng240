# A group of people wants to make a little trip to another city by train and also calculate the total ticket price because ticket prices are different with respect to age. In this question, you will write a program that reads the ages of the each person in the group and calculate the total ticket price and then print it. Please note that the people count is unknown and input includes all the ages in one line seperated by one space.
# Ticket prices with respect to ages are as follows:
# - 0-10  →  30
# - 11-25  →  60
# - 26-60  →  90
# - 60<  →  50

total = 0
ages = eval(input())

for x in ages :
    x=int(x)
    if 0 < x <=10 :
        total += 30 
    elif 11 <= x <= 25 :
        total += 60 
    elif 26 <= x <= 60 :
        total += 90
    elif 60 < x  :
        total += 50

print(total) 