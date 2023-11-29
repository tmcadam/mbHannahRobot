radio.onReceivedNumber(function (receivedNumber) {
    v = receivedNumber
})
function manualControl () {
    if (v == 1 && distance > 20) {
        TPBot.setTravelSpeed(TPBot.DriveDirection.Forward, 100)
    } else if (v == 2) {
        TPBot.setTravelSpeed(TPBot.DriveDirection.Backward, 100)
    } else if (v == 3) {
        TPBot.setTravelSpeed(TPBot.DriveDirection.Left, 30)
    } else if (v == 4) {
        TPBot.setTravelSpeed(TPBot.DriveDirection.Right, 30)
    } else if (v == 5) {
        TPBot.headlightRGB(randint(0, 255), randint(0, 255), randint(0, 255))
    } else if (v == 6) {
        TPBot.setServo(TPBot.ServoTypeList.S360, TPBot.ServoList.S1, 180)
    } else if (v == 7) {
        TPBot.setServo(TPBot.ServoTypeList.S360, TPBot.ServoList.S1, 270)
    } else {
        TPBot.stopCar()
    }
}
function lineFollow () {
    if (TPBot.trackLine(TPBot.TrackingState.L_R_line) && distance > 20) {
        TPBot.setWheels(20, 20)
    } else if (TPBot.trackLine(TPBot.TrackingState.L_unline_R_line)) {
        TPBot.setWheels(40, 0)
    } else if (TPBot.trackLine(TPBot.TrackingState.L_line_R_unline)) {
        TPBot.setWheels(0, 40)
    } else {
        TPBot.stopCar()
    }
}
let distance = 0
let v = 0
let mode = 0
radio.setGroup(1)
TPBot.headlightColor(0xff0000)
basic.showIcon(IconNames.Tortoise)
basic.forever(function () {
    distance = TPBot.sonarReturn(TPBot.SonarUnit.Centimeters)
    if (v == 9) {
        mode = 0
    } else if (v == 10) {
        mode = 1
    }
    if (mode == 0) {
        manualControl()
    } else {
        lineFollow()
    }
})
