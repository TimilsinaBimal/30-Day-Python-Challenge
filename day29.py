# write a python program to takes the user for a distance(in meters) and
# the time was taken(as three numbers: hours, minutes and seconds) and
# display the speed in miles per hour.

distancem = int(input("Enter the distance in meter: "))
h, m, s = input(
    "Enter time in (hours,minutes,seconds) Separated by comma(,) : ").split(',')
h, m, s = int(h), int(m), int(s)


def time_in_hour(h, m, s):
    return h + m/60 + (s/60)/60


def distance_in_mile(distancem):
    return distancem * 0.0006213712


speed = round(distance_in_mile(distancem) / time_in_hour(h, m, s), 4)
print(f"The speed is {speed} miles per hour")
