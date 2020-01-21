MINUTES_PER_HOUR = 60

# get current speed from user (mi/hour)
speed = input("What is your current speed (mph)? ")
speed = float(speed)

# get current distance left from user (mi)
distance = float(input("What is the distance left (mi)? "))

# calcuate time left (in hours) as distance / speed
time_left = distance / speed

hours = int(time_left)

#not working
#minutes = (distance % speed) * 60

minutes = int((time_left % 1.0) * MINUTES_PER_HOUR)

# output time left to user
print("\nYou have", hours, "hours and", minutes, "minutes left")
