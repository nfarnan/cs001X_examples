MINUTES_PER_HOUR = 60

# get distance from user
distance = input("How far to go still (in miles)? ")
distance = float(distance)

# get speed from user
speed = int(float(input("How fast are you going (mph)? ")))

# calculate time left as distance / speed
time_left = distance / speed

hours = int(time_left // 1)

# approach 1
#minutes = (time_left - hours) * MINUTES_PER_HOUR

# approach 2
#minutes = (time_left % 1) * MINUTES_PER_HOUR
#minutes = format(minutes, ".0f")

# approach 2a (compacted)
#minutes = format(((time_left % 1) * MINUTES_PER_HOUR), ".0f")
minutes = format((time_left % 1) * MINUTES_PER_HOUR, ".0f")

# approach 3
#minutes = int((time_left % 1) * MINUTES_PER_HOUR)

# output time left to user
print()
print("You have", hours, "hours and", minutes, "minutes left")

