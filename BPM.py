from pulsesensor import Pulsesensor
import time

p = Pulsesensor()
p.startAsyncBPM()
def CaptBPM():
    start = time.time()
    try:
        while ((time.time()-start)<10):
            bpm = p.BPM
            if bpm > 0:
                print("BPM: %d" % bpm)
            else:
                print("No Heartbeat found")
            time.sleep(1)
    except:
        p.stopAsyncBPM()
        
        