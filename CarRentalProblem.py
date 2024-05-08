#Car Rental Problem

#-----        Table         -----#
# Size      Seat Capacity   Cost
# Small     5               5,000
# Medium    10              8,000
# Large     15              12,000

#Set variables for Seat Capacity per Size
SizeSmall = 5
SizeMedium = 10
SizeLarge = 15


#Set variables for Cost per Size
CostSmall = 5000
CostMedium = 8000
CostLarge = 12000

# Get user input
Seat = int(input("Please input seat number: "))


if Seat <= SizeSmall:       #check if user input is valid for Small Size Seat Capacity
    print("S x 1")
    print("Total = PHP " + str(CostSmall))
elif Seat <= SizeMedium:    #check if user input is valid for Medium Size Seat Capacity
    print("M x 1")
    print("Total = PHP " + str(CostMedium))
elif Seat <= SizeLarge:     #check if user input is valid for Large Size Seat Capacity
    print("L x 1")
    print("Total = PHP " + str(CostLarge))


# check for the optimized cost if user input is exceeded to the large seat capacity
else:
    remainderM = Seat % SizeMedium   # check if user input is divisible by Medium Size
    remainderL = Seat % SizeLarge    # check if user input is divisible by Large Size

    # VALIDATION USING THE REMAINDER OF MEDIUM AND LARGE SIZE TO DETERMINE THE OPTIMIZED COST(CHEAPEST)
    if remainderM <= SizeMedium and not remainderM >= SizeLarge and not remainderM == 0:
        dividend = Seat / SizeMedium
        round_dividend = round(dividend)
        cost = round_dividend * CostMedium
        totalCost = round(cost)
        print("M x " + str(round_dividend))
        print("Total = PHP " + str(totalCost))

    elif remainderM >= SizeMedium and not remainderM <= SizeLarge and not remainderM == 0:
        dividend = Seat / SizeLarge
        rounded_dividend = round(dividend)
        cost = rounded_dividend * CostLarge
        totalCost = round(cost)
        print("L x " + str(rounded_dividend))
        print("Total = PHP " + str(totalCost))

    elif remainderM == 0 and remainderL == 0:
        dividend = Seat / SizeLarge
        rounded_dividend = round(dividend)
        cost = rounded_dividend * CostLarge
        totalCost = round(cost)
        print("L x " + str(rounded_dividend))
        print("Total = PHP " + str(totalCost))

    elif remainderM == 0 and not remainderL == 0:
        dividend = Seat / SizeMedium
        rounded_dividend = round(dividend)
        cost = rounded_dividend * CostMedium
        totalCost = round(cost)
        print("M x " + str(rounded_dividend))
        print("Total = PHP " + str(totalCost))