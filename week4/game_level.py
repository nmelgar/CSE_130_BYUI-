allowed_time = 120
current_time = 0
time_left = allowed_time - current_time
hit_wall = False
hit_obstacle = False
extra_life = 0
extra_time = True
fuel = 0

if time_left == 0:
    print("Time is over. Level terminated!")

elif extra_time == True:
    time_left += 20

elif hit_wall == True or hit_obstacle == True:
    if extra_life > 0:
        print("Keep playing!")
        extra_life -= 1
    else:
        print("Level terminated!")

elif fuel == 0:
    print("Empty fuel. Level terminated!")
