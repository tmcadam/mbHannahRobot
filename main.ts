radio.onReceivedNumber(function (receivedNumber) {
    v = receivedNumber
})
let distance = 0
let v = 0
radio.setGroup(1)
TPBot.headlightColor(0xff0000)
basic.showIcon(IconNames.Tortoise)
basic.forever(function () {
    distance = TPBot.sonarReturn(TPBot.SonarUnit.Centimeters)
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
    }
})
