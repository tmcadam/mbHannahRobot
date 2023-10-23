v = 0
radio.set_group(1)
TPBot.headlight_color(0xff0000)

def on_forever():
    if v == 1 and TPBot.sonar_judge(TPBot.Sonarjudge.GREATER, 30):
        TPBot.set_travel_speed(TPBot.DriveDirection.FORWARD, 50)
    elif v == 2:
        TPBot.set_travel_speed(TPBot.DriveDirection.BACKWARD, 50)
    elif v == 3:
        TPBot.set_travel_speed(TPBot.DriveDirection.LEFT, 50)
    elif v == 4:
        TPBot.set_travel_speed(TPBot.DriveDirection.RIGHT, 50)
    elif v == 0:
        TPBot.stop_car()
basic.forever(on_forever)

def on_received_number(receivedNumber):
    global v
    v = receivedNumber
radio.on_received_number(on_received_number)
