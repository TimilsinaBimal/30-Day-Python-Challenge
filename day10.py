# SalesPerson Rita Drives 2052 miles in 6 days
# stopping at 2 towns each day. How many Kilometers
# does she average between stops?

totalDistanceTravelled = 2052
totalDaysTravelled = 6
totalStoppedEachDay = 2
mileToKm = 1.60934
averageStopped = totalDistanceTravelled / \
    (totalDaysTravelled * totalStoppedEachDay)
averageStoppedInKm = averageStopped * mileToKm
print(f"Average between Stops : {averageStoppedInKm} ")
