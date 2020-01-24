# Write a program that for a given hour and minutes values calculates an
# angle in degree between the hour and the minute hands. Check whether
# the minute hand overlapping the hour hand at a given time.
degreeToMin = 60


def minToDegree(h, m):
    if (m < 0 or h < 0 or m > 60 or h > 12):
        print("Wrong Input")
    if h == 12:
        h = 0
    if m == 60:
        m = 0
    hour_angle = 0.5 * (h*60+m)
    min_angle = 6*m
    angle = abs(hour_angle-min_angle)

    angle = min(360-angle, angle)
    return int(angle)


h = int(input("Enter Hour(1-12): "))
m = int(input("Enter Minute(0-59): "))

clockAngle = minToDegree(h, m)
if clockAngle == 0:
    print("Hour and min are overlapped.")
else:
    print(f"Angle:{clockAngle} Degree")
