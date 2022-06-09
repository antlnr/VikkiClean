import RPi.GPIO as GPIO          
import time

in1 = 24
in2 = 23
enA = 25

in3 = 6
in4 = 5
enB = 26

temp1=1

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
pA=GPIO.PWM(enA,1000)
pB=GPIO.PWM(enB,1000)

pA.start(100)
pB.start(100)

def tout_droit():
    print("j'avance")
    #Les 4 roues avancent
    
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    
    return

def recule():
    print("bip bip je recule")
    #Les 4 roues avancent
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in1,GPIO.LOW)
    
    GPIO.output(in4,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
  
    return

def tourne_droite():
    print("je tourne à droite")
    #Côté droit recule, côté gauche avance
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    
    GPIO.output(in4,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)

    return

def tourne_gauche():
    #Côté droit avance, côté gauche recule
    print("je tourne à gauche")

    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in1,GPIO.LOW)
    
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

    return

def stop():
    print("Je m'arrête !")
    #les 4 roues s'arrêtent

    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    return

def Action():
    tout_droit()
    time.sleep(5)
    recule()
    time.sleep(5)
    tourne_droite()
    time.sleep(5)
    tourne_gauche()
    time.sleep(5)
    stop()
    GPIO.cleanup()

def clean():
    tout_droit()
    GPIO.cleanup()
     