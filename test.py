import datetime
import os
from pygame import mixer
from gtts import gTTS
from playsound import playsound
#def playme(myText):

if __name__ == '__main__':
    myText = "Hello sir I have remainder for you"
    language = 'en'


    f = open('textFile/daily', "r")


    lines = f.readlines();
    for i in lines:
         thisline =  i.split(" ");
         out = ""
         while (1):
           currentDT = datetime.datetime.now()
           ct = currentDT.strftime("%H:%M")
           if (ct == thisline[0]):
               break;
         for j in range(1, len(thisline)):
           out = out + " " + thisline[j];
         myText = myText+" "+out;
         #playme(myText)
         myObj = gTTS(text=myText, lang=language, slow=True)

         myObj.save('daily.mp3')
         mixer.init()
         mixer.music.load('daily.mp3')
         mixer.music.play()
         os.remove('daily.mp3')

    f.close()
