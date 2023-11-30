def on_received_number(receivedNumber):
    global v
    v = receivedNumber
radio.on_received_number(on_received_number)

def manualControl():
    if v == 1 and distance > 20:
        TPBot.set_travel_speed(TPBot.DriveDirection.FORWARD, 100)
    elif v == 2:
        TPBot.set_travel_speed(TPBot.DriveDirection.BACKWARD, 50)
    elif v == 3:
        TPBot.set_travel_speed(TPBot.DriveDirection.LEFT, 40)
    elif v == 4:
        TPBot.set_travel_speed(TPBot.DriveDirection.RIGHT, 40)
    elif v == 6:
        TPBot.set_servo(TPBot.ServoTypeList.S360, TPBot.ServoList.S1, 270)
    elif v == 7:
        TPBot.set_servo(TPBot.ServoTypeList.S360, TPBot.ServoList.S1, 180)
    else:
        TPBot.stop_car()
def lineFollow():
    if TPBot.track_line(TPBot.TrackingState.L_R_LINE) and distance > 12:
        TPBot.set_wheels(20, 20)
    elif TPBot.track_line(TPBot.TrackingState.L_UNLINE_R_LINE):
        TPBot.set_wheels(40, 10)
    elif TPBot.track_line(TPBot.TrackingState.L_LINE_R_UNLINE):
        TPBot.set_wheels(10, 40)
    else:
        TPBot.stop_car()
distance = 0
v = 0
mode = 0
radio.set_group(1)
TPBot.headlight_color(0xff0000)
basic.show_icon(IconNames.TORTOISE)

def on_forever():
    global distance, mode
    distance = TPBot.sonar_return(TPBot.SonarUnit.CENTIMETERS)
    if v == 9:
        mode = 0
    elif v == 10:
        mode = 1
    if mode == 0:
        manualControl()
    else:
        lineFollow()
    if input.acceleration(Dimension.X) < -250:
        basic.show_leds("""
            . . # . .
            . # . . .
            # # # # #
            . # . . .
            . . # . .
            """)
    elif input.acceleration(Dimension.X) > 250:
        basic.show_leds("""
            . . # . .
            . . . # .
            # # # # #
            . . . # .
            . . # . .
            """)
basic.forever(on_forever)
