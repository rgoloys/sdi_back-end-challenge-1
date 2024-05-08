#Car Rental Problem

#-----   Default Size & Cost    -----#
# Size      Seat Capacity   Cost
# Small     5               5,000
# Medium    10              8,000
# Large     15              12,000


# Get user input
Seat = int(input("Please input seat number: "))
print()
if Seat <= 0:
    print("Please input a whole number and not less than or equal 0")
else:
    print("Leave a black if you want to use by default")
    print()  # Prints a blank line
    try:
        InputSmallSize = int(input("Please Input Small Size Car Seating Capacity: "))
    except ValueError:
        print("Default value is 5")
        InputSmallSize = 5
    try:
        InputMediumSize = int(input("Please Input Medium Size Car Seating Capacity: "))
    except ValueError:
        print("Default value is 10")
        InputMediumSize = 10
    try:
        InputLargeSize = int(input("Please Input Large Size Car Seating Capacity: "))
    except ValueError:
        print("Default value is 15")
        InputLargeSize = 15

    print()
    print()

    try:
        SmallCost = int(input("Please Input Cost for Small Car Seating Capacity: "))
    except ValueError:
        print("Default value is 5000")
        SmallCost = 5000
    try:
        MediumCost = int(input("Please Input Cost for Medium Car Seating Capacity: "))
    except ValueError:
        print("Default value is 8000")
        MediumCost = 8000
    try:
        LargeCost = int(input("Please Input Cost for Large Car Seating Capacity: "))
    except ValueError:
        print("Default value is 12000")
        LargeCost = 12000




    if Seat <= InputSmallSize:    #check if user input is valid for Small Size Seat Capacity
        print()
        print("Inputted Seat Number is: " + str(Seat))
        print("S x 1")
        print("Total = PHP " + str(SmallCost))
    elif Seat <= InputMediumSize:    #check if user input is valid for Medium Size Seat Capacity
        print()
        print("Inputted Seat Number is: " + str(Seat))
        print("M x 1")
        print("Total = PHP " + str(MediumCost))
    elif Seat <= InputLargeSize:     #check if user input is valid for Large Size Seat Capacity
        print()
        print("Inputted Seat Number is: " + str(Seat))
        print("L x 1")
        print("Total = PHP " + str(LargeCost))


    # check for the optimized cost if user input is exceeded to the large seat capacity
    else:
        remainderM = Seat % InputMediumSize   # check if user input is divisible by Medium Size
        remainderL = Seat % InputLargeSize    # check if user input is divisible by Large Size

        # VALIDATION USING THE REMAINDER OF MEDIUM AND LARGE SIZE TO DETERMINE THE OPTIMIZED COST(CHEAPEST)
        if remainderM <= InputMediumSize and not remainderM >= InputLargeSize and not remainderM == 0:
            dividend = Seat / InputMediumSize
            round_dividend = round(dividend)
            cost = round_dividend * MediumCost
            totalCost = round(cost)
            print()
            print("Inputted Seat Number is: " + str(Seat))
            print("M x " + str(round_dividend))
            print("Total = PHP " + str(totalCost))

        elif remainderM >= InputMediumSize and not remainderM <= InputLargeSize and not remainderM == 0:
            dividend = Seat / InputLargeSize
            rounded_dividend = round(dividend)
            cost = rounded_dividend * LargeCost
            totalCost = round(cost)
            print()
            print("Inputted Seat Number is: " + str(Seat))
            print("L x " + str(rounded_dividend))
            print("Total = PHP " + str(totalCost))

        elif remainderM == 0 and remainderL == 0:
            dividend = Seat / InputLargeSize
            rounded_dividend = round(dividend)
            cost = rounded_dividend * LargeCost
            totalCost = round(cost)
            print()
            print("Inputted Seat Number is: " + str(Seat))
            print("L x " + str(rounded_dividend))
            print("Total = PHP " + str(totalCost))

        elif remainderM == 0 and not remainderL == 0:
            dividend = Seat / InputMediumSize
            rounded_dividend = round(dividend)
            cost = rounded_dividend * MediumCost
            totalCost = round(cost)
            print()
            print("Inputted Seat Number is: " + str(Seat))
            print("M x " + str(rounded_dividend))
            print("Total = PHP " + str(totalCost))