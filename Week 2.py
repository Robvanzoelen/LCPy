traveling_distance = input("How far do you have to travel? (KM)")
walking_speed = input("How fast do you walk? (KM/h)")
biking_speed = input("How fast do you bike? (KM/h)")
driving_speed = input("How fast do you drive? (KM/h)")

traveling_distance_int = int(traveling_distance)
walking_speed_int = int(walking_speed)
biking_speed_int = int(biking_speed)
driving_speed_int = int(driving_speed)

traveling_time_walk = int(traveling_distance_int/walking_speed_int)
traveling_time_bike = int(traveling_distance_int/biking_speed_int)
traveling_time_car = int(traveling_distance_int/driving_speed_int)

traveling_time_walk_rem = traveling_time_walk%60
traveling_time_bike_rem = traveling_time_bike%60
traveling_time_car_rem = traveling_time_car%60

print("Your traveling time by walk is", traveling_time_walk, "hours and", traveling_time_walk_rem, "minutes")
print("Your traveling time by bike is", traveling_time_bike, "hours and", traveling_time_bike_rem, "minutes")
print("Your traveling time by car is", traveling_time_car, "hours and", traveling_time_car_rem, "minutes")