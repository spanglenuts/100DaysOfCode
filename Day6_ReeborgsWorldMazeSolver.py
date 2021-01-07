#Run in Reeborgs World Maze https://reeborg.ca/

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()
    
while not at_goal():
    if wall_on_right() and front_is_clear():
        move()
    elif wall_on_right() and wall_in_front():
        turn_left()
    elif wall_in_front() and right_is_clear():
        turn_right()
        move()
    elif front_is_clear and right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()        
