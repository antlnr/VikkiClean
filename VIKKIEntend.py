# https://www.mathweb.fr/euclide/2020/09/22/reconnaissance-voix-python/

from VIKKIParleDef import *
from  MCC import *
from BPM import *
from Thermo import *

from tkinter import W
from numpy import rec
from speech_recognition import Recognizer, Microphone



def rec_voc():
    recognizer = Recognizer()
    # On enregistre le son
    with Microphone() as source:
        print("Réglage du bruit ambiant... Patientez...")
        recognizer.adjust_for_ambient_noise(source)
        print("Vous pouvez parler...")
        recorded_audio = recognizer.listen(source, timeout=20)
        print("Enregistrement terminé !")

    # Reconnaissance de l'audio
    try:
        print("Reconnaissance du texte...")
        text = recognizer.recognize_google(recorded_audio, language="fr-FR")
        print("Vous avez dit : {}".format(text))

        return (text)

    except Exception as ex:
        print(ex)


def come_to_me():
    # ! Prioritié 2 !
    print("J'arrive !")
    Action()
    return 0


def mesure_bpm():
    # !! Prioritié 1 !!
    print("prise de BPM en cours")
    bpm_values = CaptBPM()
    bpm_moy = round(numpy.mean(bpm_values))
    print("BPM moyen : %d" %bpm_moy)
    # utiliser HRV
    return bpm_moy


def mesure_temp():
    # !! Prioritié 1 !!
    print("prise de température en cours")
    temp_values = CaptTemp()
    temp_moy = round(numpy.mean(temp_values))
    print("Température corporelle moyenne : %d" %temp_moy)
    return temp_moy


def who_are_you():
    return 0




def vikkiReagit():

    record = rec_voc()  # lance la reconaissance vocale, les phrases seront stockés dans Record en string en minuscule

    if (record == None):  # Si le Record est vide/Rien n'a été dit ou compris
        record = ""
       

    elif ("viens" in record.lower()):  # Si "Viens" fait parti des phrases entendu

        ActionVoc(record, language)
        come_to_me()

    elif (("cœur" in record.lower()) or ("battement" in record.lower()) or ("bpm" in record.lower()) or (
            "fréquence cardiaque" in record.lower())):  # Si "Coeur/Battement/BPM" fait parti des phrases entendu

        BPMVoc(record, language)
        time.sleep(3)
        BPMVocResultat(record, language, mesure_bpm())
        time.sleep(5)

    elif ("température" in record.lower()):
        TempVoc(record, language)
        time.sleep(3)
        TempVocResultat(record, language, mesure_temp())
        time.sleep(5)
        
    elif (("présente-toi" in record.lower())):
        PresentationVoc(record, language)
    
    elif (("stop" in record.lower())):
        print("stop")
        StopVoc(record, language)
        quit()

    else:
        print("Vikki a entendu : ", record.lower())
        NonVoc(record, language)