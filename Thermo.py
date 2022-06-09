import time
from smbus2 import SMBus
from mlx90614 import MLX90614

bus = SMBus(1)
sensor = MLX90614(bus, address=0x5A)
def CaptTemp():
    start = time.time()
    temp_values = []
    while ((time.time()-start)<5):
        print("Ambient Temperature :", sensor.get_ambient())
        print("Object Temperature :", sensor.get_object_1())
        temp_values.append(sensor.get_ambient())
        time.sleep(1)
    bus.close()
    
    return temp_values

