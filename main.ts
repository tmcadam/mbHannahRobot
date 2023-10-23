let distance = 0
basic.forever(function () {
    let v = 0
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
    	
    } else if (false) {
    	
    } else {
    	
    }
})
