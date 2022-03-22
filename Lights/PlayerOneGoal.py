import time*
import gpiozero as gz
import threading as t

led = gz.RGBLED(17, 22, 24)
P1Sensor = gz.MotionSensor(10)

def setLights(player):
	

def findGoal(pir, led):
	while True:
		if pir.motion_detected:
			return pir.pin
		
def goalLights(pin):
	if pin == P1Sensor.pin:
		led.color = P2Colors
	elif pin == P2Sensor:
		led.color = P1Colors
