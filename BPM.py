from pulsesensor import Pulsesensor
import time
import numpy


# module du tts

p = Pulsesensor()
p.startAsyncBPM()


def get_rmssd_from_ibi_values():
    return "rmssd"


def get_sdnn_from_ibi_values():
    return "rmssd"


def CaptBPM():
    
    start = time.time()

    bpm_values = []
    ibi_values = []
    bpm_moyen = 0
    try:
        while ((time.time()-start)<3):
            bpm = p.BPM
            ibi = p.ibi
            bpm_values.append(bpm)
            ibi_values.append(ibi)
            
            #if len(ibi_values) > 15:
                #process ibi values to compute hrv metrics
                #rmssd = get_rmssd_from_ibi_values()
            if bpm > 0:
                print("IBI : %d" % ibi)
                print("BPM: %d" % bpm)
            else:
                print("No Heartbeat found")
            time.sleep(1)
 
         
    except:
        p.stopAsyncBPM()
    
    return bpm_values
  
#CaptBPM()
#bpm_moy = numpy.mean(bpm_values)
#print(bpm_moy)       
