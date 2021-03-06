# module du tts
from gtts import gTTS
from BPM import *
from pydub import AudioSegment
from pydub.playback import play
import numpy
import playsound
import platform
import os
global bpm_values
### UTILISER playsound 1.2.2 !!!!!!!!!!!!!!!!

# ce que VIKKI nous dit
# inputText = 'VIKKI, prends ma température et mon pouls'
textToSay = ''
language = 'fr'


################### VIKKI se présente  ###################
def PresentationVoc(inputText, language):
    textToSay = 'Bonjour, je suis VIKKI.'

    presentation = gTTS(text=textToSay, lang=language, slow=False)  # slow = false évite que le tts soit mou du genou
    presentation.save('presentation.mp3')  # sauvegarde de la parole en mp3

    if (platform.system() == "Windows"):  # sur win
        playsound.playsound("presentation.mp3")

    else:  # sur linux
        os.system('open presentation.mp3')

    print("Présentation en cours")
    
    
################### Prise de Fréquence cardiaque ###################
def BPMVoc(inputText, language):
    textToSay = 'Initialisation du capteur cardiaque.'

    priseBPM = gTTS(text=textToSay, lang=language, slow=False)  # slow = false évite que le tts soit mou du genou
    priseBPM.save("priseBPM.mp3")  # sauvegarde de la parole en mp3

    if platform.system() == "Windows":  # sur win
        playsound.playsound("priseBPM.mp3")

    else:  # sur linux
        os.system("open priseBPM.mp3")

def BPMVocResultat(inputText, language, bpm_moy):

    textToSay = ('Vous avez un bpm moyen de : %d battement par minutes' % bpm_moy)
    
    priseBPM = gTTS(text=textToSay, lang=language, slow=False)  # slow = false évite que le tts soit mou du genou
    priseBPM.save("moyenBPM.mp3")  # sauvegarde de la parole en mp3

    if platform.system() == "Windows":  # sur win
        playsound.playsound("moyenBPM.mp3")

    else:  # sur linux
        os.system("open moyenBPM.mp3")
    
################### Prise de Température ###################
def TempVoc(inputText, language):
    
        textToSay = 'Initialisation de la prise de température.'

        priseTemp = gTTS(text=textToSay, lang=language, slow=False)  # slow = false évite que le tts soit mou du genou
        priseTemp.save("priseTemp.mp3")  # sauvegarde de la parole en mp3

        print("Prise de la température")

        if platform.system() == "Windows":  # sur win
            playsound.playsound("priseTemp.mp3")

        else:  # sur linux
            os.system("open priseTemp.mp3")
            
def TempVocResultat(record, language, temp_moy):
    textToSay = ('Vous avez une température corporelle moyenne de : %d degrés Celcius' % temp_moy)
    
    priseBPM = gTTS(text=textToSay, lang=language, slow=False)  # slow = false évite que le tts soit mou du genou
    priseBPM.save("moyenTemp.mp3")  # sauvegarde de la parole en mp3

    if platform.system() == "Windows":  # sur win
        playsound.playsound("moyenTemp.mp3")

    else:  # sur linux
        os.system("open moyenTemp.mp3")
################### VIKKI bouge ###################            
def ActionVoc(inputText, language):
        textToSay = 'Ok, ne bougez pas j\'arrive !'

        action = gTTS(text=textToSay, lang=language, slow=False)  # slow = false évite que le tts soit mou du genou
        action.save('actionvoc.mp3')  # sauvegarde de la parole en mp3

        print("j'arrive !")

        if (platform.system() == "Windows"):  # sur win
            playsound.playsound("actionvoc.mp3")

        else:  # sur linux
            os.system('open actionvoc.mp3')
            
            
################### Arrêt d'urgence ###################
def StopVoc(inputText, language):
        textToSay = 'OK, je m\'arrête.'

        stop = gTTS(text=textToSay, lang=language, slow=False)  # slow = false évite que le tts soit mou du genou
        stop.save("stopvoc.mp3")  # sauvegarde de la parole en mp3

        print("je vais m'arreter")

        if platform.system() == "Windows":  # sur win
            playsound.playsound("stopvoc.mp3")

        else:  # sur linux
            os.system("open stopvoc.mp3")

################### VIKKI n'a pas compris ###################
def NonVoc(inputText, language):
        textToSay = 'Désolé, je n\'ai pas compris.'

        pakompri = gTTS(text=textToSay, lang=language, slow=False)  # slow = false évite que le tts soit mou du genou
        pakompri.save("incomprehension.mp3")  # sauvegarde de la parole en mp3

        print("g pakompri")

        if platform.system() == "Windows":  # sur win
            playsound.playsound("incomprehension.mp3")

        else:  # sur linux
            os.system("open incomprehension.mp3")
            
            