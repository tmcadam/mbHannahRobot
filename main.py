def on_received_number(receivedNumber):
    global v
    v = receivedNumber
radio.on_received_number(on_received_number)

distance = 0
v = 0
radio.set_group(1)
TPBot.headlight_rgb(randint(0, 255), randint(0, 255), randint(0, 255))
basic.show_icon(IconNames.TORTOISE)

def on_forever():
    global distance
    distance = TPBot.sonar_return(TPBot.SonarUnit.CENTIMETERS)
    if v == 1 and distance > 20:
        TPBot.set_travel_speed(TPBot.DriveDirection.FORWARD, 100)
    elif v == 2:
        TPBot.set_travel_speed(TPBot.DriveDirection.BACKWARD, 100)
    elif v == 3:
        TPBot.set_travel_speed(TPBot.DriveDirection.LEFT, 30)
    elif v == 4:
        TPBot.set_travel_speed(TPBot.DriveDirection.RIGHT, 30)
    elif v == 5:
        TPBot.headlight_rgb(randint(0, 255), randint(0, 255), randint(0, 255))
    elif v == 6:
        pass
    elif False:
        pass
    else:
        pass
basic.forever(on_forever)
