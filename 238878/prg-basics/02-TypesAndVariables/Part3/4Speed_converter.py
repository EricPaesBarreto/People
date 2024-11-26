###
# A program that, for a given speed in km/h,
# prints the speed in m/s
#
speed_kmh = input('Speed in kmh: ')
a = 5/18
speed_ms = int (speed_kmh) * a
print(speed_kmh, "km/h = ", speed_ms, "m/s")