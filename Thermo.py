import time
from smbus2 import SMBus
from mlx90614 import MLX90614

bus = SMBus(1)
sensor = MLX90614(bus, address=0x5A)
def CaptTemp():
    start = time.time()
    while ((time.time()-start)<5):
        print("Ambient Temperature :", sensor.get_ambient())
        print("Object Temperature :", sensor.get_object_1())
        time.sleep(1)
    bus.close()

