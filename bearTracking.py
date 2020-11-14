def bearTracker():
    BEGIN_PRODUCING_CUB_AT = 4
    AVEREGE_AGE = 20
    CURRENT_YEAR_CUBS = 2
    totalTrackedBears = 0
    print "This is Bear Cub Estimation Program"
    runOrQuit = input("It estimates the number of cubs that a female bear will produce over a lifetime. Please enter ROAR if you want to run the program or STOP to quit: ")
    while runOrQuit == "ROAR": 
        bearName = input("Enter the Bear Name: ")
        bearAge = int(input("Enter the age of the bear in years: "))
        year = bearAge
        previousCycleCub = 0
        sumOfAllCubs = 2
        print "Year   Previous Cycle Cub   Current Year Cubs     Sum of all Cubs"
        while year <= 20:
            if year < BEGIN_PRODUCING_CUB_AT:
                year = BEGIN_PRODUCING_CUB_AT
            print year, previousCycleCub, CURRENT_YEAR_CUBS, sumOfAllCubs
            year = year + 2
            previousCycleCub = previousCycleCub + CURRENT_YEAR_CUBS
            sumOfAllCubs = sumOfAllCubs + CURRENT_YEAR_CUBS
        print bearName, "will have a total of ", sumOfAllCubs, "cubs over her remaining lifetime of 20 years."
        totalTrackedBears = totalTrackedBears + sumOfAllCubs
        runOrQuit = input("Please enter ROAR if you want to run the program or STOP to quit.")
    print "The sum of all cubs for all Bears tracked is ", totalTrackedBears


if __name__ == "__main__":
    print "Bear Tracking program with python's method ... "
    bearTracker()








