# module du tts
from gtts import gTTS

from pydub import AudioSegment
from pydub.playback import play
import playsound
import platform
import os

### UTILISER playsound 1.2.2 !!!!!!!!!!!!!!!!

# ce que VIKKI nous dit
# inputText = 'VIKKI, prends ma température et mon pouls'
textToSay = ''
language = 'fr'

def vikkiParle (inputText, language):

################### Présentation ###################

    if " présentation " in (" " + inputText + " "):
        # entourer d'espaces permet de comparer la présence d'un mot plutot que juste un morceau de mot

        textToSay = 'Bonjour, je suis VIKKI.'

        presentation = gTTS(text=textToSay, lang=language, slow=False)  # slow = false évite que le tts soit mou du genou
        presentation.save('presentation.mp3')  # sauvegarde de la parole en mp3

        if (platform.system() == "Windows"):  # sur win
            playsound.playsound("presentation.mp3")

        else:  # sur linux
            os.system('open presentation.mp3')

        print("Présentation en cours")

    elif " présente-toi " in (" " + inputText + " "):

        textToSay = 'Bonjour, je suis VIKKI.'

        presentation = gTTS(text=textToSay, lang=language, slow=False)  # slow = false évite que le tts soit mou du genou
        presentation.save('presentation.mp3')  # sauvegarde de la parole en mp3

        if (platform.system() == "Windows"):  # sur win
            playsound.playsound("presentation.mp3")

        else:  # sur linux
            os.system('open presentation.mp3')

        print("Présentation en cours")

################### Prise de Fréquence Cardiaque ###################

    elif " BPM " in (" " + inputText + " "):
        # entourer d'espaces permet de comparer la présence d'un mot plutot que juste un morceau de mot

        textToSay = 'Initialisation du capteur cardiaque.'

        priseBPM = gTTS(text=textToSay, lang=language, slow=False)  # slow = false évite que le tts soit mou du genou
        priseBPM.save("priseBPM.mp3")  # sauvegarde de la parole en mp3

        if platform.system() == "Windows":  # sur win
            playsound.playsound("priseBPM.mp3")

        else:  # sur linux
            os.system("open priseBPM.mp3")


    elif " pouls " in (" " + inputText + " "):
        # entourer d'espaces permet de comparer la présence d'un mot plutot que juste un morceau de mot

        textToSay = 'Initialisation du capteur cardiaque.'

        priseBPM = gTTS(text=textToSay, lang=language, slow=False)  # slow = false évite que le tts soit mou du genou
        priseBPM.save("priseBPM.mp3")  # sauvegarde de la parole en mp3

        if platform.system() == "Windows":  # sur win
            playsound.playsound("priseBPM.mp3")

        else:  # sur linux
            os.system("open priseBPM.mp3")


    elif " fréquence cardiaque " in (" " + inputText + " "):
        # entourer d'espaces permet de comparer la présence d'un mot plutot que juste un morceau de mot

        textToSay = 'Initialisation du capteur cardiaque.'

        priseBPM = gTTS(text=textToSay, lang=language, slow=False)  # slow = false évite que le tts soit mou du genou
        priseBPM.save("priseBPM.mp3")  # sauvegarde de la parole en mp3

        print("Initialisation du capteur cardiaque")

        if platform.system() == "Windows":  # sur win
            playsound.playsound("priseBPM.mp3")

        else:  # sur linux
            os.system("open priseBPM.mp3")


################### Prise de Température ###################

    elif " température " in (" " + inputText + " "):
        # entourer d'espaces permet de comparer la présence d'un mot plutot que juste un morceau de mot

        textToSay = 'Initialisation de la prise de température.'

        priseTemp = gTTS(text=textToSay, lang=language, slow=False)  # slow = false évite que le tts soit mou du genou
        priseTemp.save("priseTemp.mp3")  # sauvegarde de la parole en mp3

        print("Prise de la température")

        if platform.system() == "Windows":  # sur win
            playsound.playsound("priseTemp.mp3")

        else:  # sur linux
            os.system("open priseTemp.mp3")


################### Commande non reconnue ###################

    else:

        textToSay = 'Désolé, je n\'ai pas compris.'

        pakompri = gTTS(text=textToSay, lang=language, slow=False)  # slow = false évite que le tts soit mou du genou
        pakompri.save("incomprehension.mp3")  # sauvegarde de la parole en mp3

        print("g pakompri")

        if platform.system() == "Windows":  # sur win
            playsound.playsound("incomprehension.mp3")

        else:  # sur linux
            os.system("open incomprehension.mp3")


################### Commande non reconnue ###################

    if " viens " in (" " + inputText + " "):
        # entourer d'espaces permet de comparer la présence d'un mot plutot que juste un morceau de mot

        textToSay = 'Ok, j\'arrive !'

        presentation = gTTS(text=textToSay, lang=language, slow=False)  # slow = false évite que le tts soit mou du genou
        presentation.save('presentation.mp3')  # sauvegarde de la parole en mp3

        print("j'arrive bégé")

        if (platform.system() == "Windows"):  # sur win
            playsound.playsound("presentation.mp3")

        else:  # sur linux
            os.system('open presentation.mp3')


    elif " rejoins-moi " in (" " + inputText + " "):

        textToSay = 'Ok, j\'arrive !'

        presentation = gTTS(text=textToSay, lang=language, slow=False)  # slow = false évite que le tts soit mou du genou
        presentation.save('presentation.mp3')  # sauvegarde de la parole en mp3

        print("j'arrive bégé")

        if (platform.system() == "Windows"):  # sur win
            playsound.playsound("presentation.mp3")

        else:  # sur linux
            os.system('open presentation.mp3')


    elif " ici " in (" " + inputText + " "):

        textToSay = 'Ok, j\'arrive !'

        presentation = gTTS(text=textToSay, lang=language, slow=False)  # slow = false évite que le tts soit mou du genou
        presentation.save('presentation.mp3')  # sauvegarde de la parole en mp3

        print("j'arrive bégé")

        if (platform.system() == "Windows"):  # sur win
            playsound.playsound("presentation.mp3")

        else:  # sur linux
            os.system('open presentation.mp3')