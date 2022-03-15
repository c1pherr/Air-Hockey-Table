import gpiozero as gz
import time as t

led = gz.RGBLED(17, 22, 24)
pir = gz.MotionSensor(10)

while True:
	if pir.motion_detected:
		print('+')
		t.sleep(1)
	else:
		print('-')
		t.sleep(1)
	

