# I Joaquin Tolentino, 000771944, certify that this work is my own effort and that I have not allowed anyone else to copy from it.

import random

# At the beginning of the program, the computer randomly creates a price for an item
amount = random.randint(0,20) + round(random.randint(0,100)/100, 2)
print(amount)

# Asks the user how much they would like to pay
# Assume that it has to be more than the variable amount
payment = float(input("How much would you like to pay? (Must be more than the amount)"))

change = payment - amount

if change > 0:
    #print(change)
    # Convert the variable change(float) to an int data type,
    # also multiply it by 100 then  round it to two decimal places before converting
    change = int( round(change * 100, 3))
    dollars = 0
    quarters = 0
    dimes = 0
    nickels = 0
    #print(change)

    dollars = change // 100
    change = change % 100

    #print(dollars)
    #print(change)

    if change > 0:
        quarters = change // 25
        change = change % 25

        dimes = change // 10
        change = change % 10

        nickels = change // 5
        change = change % 5
        #print(nickels)
        #print(change)

        # This formula allows the program to round up or down the remaining change (pennies),
        # if it will round up to a nickel or not
        nickels = nickels + int(round( (change * 2) / 100, 1) * 10)
        #print(nickels)

        print( "You got %d dollars, %d quarters, %d dimes, and %d nickels back in change" % ( dollars, quarters, dimes, nickels))

    else:
        print( "You got %d dollars, %d quarters, %d dimes, and %d nickels back in change" % ( dollars, quarters, dimes, nickels))

else:
    print("No change owed")

