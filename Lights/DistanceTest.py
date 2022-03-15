import gpiozero as gz
import time as t

sensor = gz.DistanceSensor(echo=26, trigger=19, partial = True)
print('Sensor Found')
print(sensor)

sensor.wait_for_in_range
print(sensor.trigger)
while True:
    print(sensor.value)
    t.sleep(1)