# The number of red blood corpuscles in one
# the cubic milimeter is about 5,000,000 and the
# number of white blood corpuscles in one cubic
# the milimetre is about 8,000. What, then, is the ratio
# of white blood corpuscles to red blood corpuscles?
# Aspect Ratio should be as an int value?

redCorpuscles = 6
whiteCorpuscles = 4


def greatestCommonFactor(redC, whiteC):
    return whiteC if (redC == 0) else greatestCommonFactor(whiteC % redC, redC)


factor = greatestCommonFactor(redCorpuscles, whiteCorpuscles)
whiteRatio = int(whiteCorpuscles/factor)
redRatio = int(redCorpuscles/factor)

print(
    f"The ratio to the white blood corpuscles to red blood corpuscles is {whiteRatio} : {redRatio}")
