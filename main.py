def NEW():
    maqueenPlusV2.led_rainbow(DigitalPin.P15, 1, 360)
    US = maqueenPlusV2.read_ultrasonic(DigitalPin.P13, DigitalPin.P14)
    while maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_M) == 1 and maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_L1) == 1 and maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_R1) == 1:
            while maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_L2) == 1 or maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_R2) == 1:
                maqueenPlusV2.control_motor_stop(maqueenPlusV2.MyEnumMotor.ALL_MOTOR)
                pass
    while maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_M) == 0 and maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_L1) == 0 and maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_R1) == 0:
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.ALL_MOTOR, maqueenPlusV2.MyEnumDir.BACKWARD, 50)
        if maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_M) == 1 or maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_L1) == 1 or maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_R1) == 1:
            break
        pass
    if US<=5.5:
        maqueenPlusV2.control_motor_stop(maqueenPlusV2.MyEnumMotor.ALL_MOTOR)
        pass
    else:
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.ALL_MOTOR, maqueenPlusV2.MyEnumDir.FORWARD, 255)
    while maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_R1) == 1:
        if maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_R1) == 0 and maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_M) == 1:
            maqueenPlusV2.control_motor_stop(maqueenPlusV2.MyEnumMotor.RIGHT_MOTOR)
            break
        else:
            maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.RIGHT_MOTOR, maqueenPlusV2.MyEnumDir.FORWARD, 1/100)
            pass
    while maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_L1) == 1:
        if maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_L1) == 0 and maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_M) == 1:
            maqueenPlusV2.control_motor_stop(maqueenPlusV2.MyEnumMotor.LEFT_MOTOR)
            break
        else:
            maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.LEFT_MOTOR, maqueenPlusV2.MyEnumDir.FORWARD, 1/100)
            pass
basic.forever(NEW)