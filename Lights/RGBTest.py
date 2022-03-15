import gpiozero as gz
import time as t

led = gz.RGBLED(17,22,24)
motionSens = gz.MotionSensor(27)

while True:
	if motionSens.motion_detected:
		led.color = (0,0,1)
	else:
		led.color = (1,1,0)