import datetime
from gtts import gTTS
from playsound import playsound
if __name__ == "__main__":
 while(1):
  currentDT = datetime.datetime.now()
  ct = currentDT.strftime("%H:%M")
  if (ct == "15:26"):
    myText = "Hello sir I have remainder for you"
    language = 'en'
    f1 = open('textFile/routine', "r")
    f2 = open('textFile/remainder', "r")
    f3 =  open('textFile/todaysRemainder', "w")

    tdate = datetime.datetime.now()
    td = tdate.strftime("%Y-%m-%d")
    print(td)
    l1 = f2.readlines()

    for k in l1:
        w = ""
        firstprt = k.split(" ")
        print(firstprt)
        tdr = firstprt[0]
        if(td == tdr):
            w=firstprt[1]
            for p in range(2, len(firstprt)):
               w = w +" " +firstprt[p]
               print(w)
            f3.writelines(w)
        else:
             break

    f1.close()
    f2.close()
    f3.close()

    f1 = open('textFile/routine', "r")
    f2 = open('textFile/todaysRemainder', "r")
    f3 = open('textFile/daily', "w")
    m = 0
    n = 0
    l1 = f1.readlines()
    l2 = f2.readlines()
    len1 = len(l1)
    len2 = len(l2)
    while (1):
        if (m == len1):
            if (n == len2):
                f3.close()
                break
            else:
                f3.writelines(l2[n])
                n = n + 1
        elif (n == len2):
            if (m == len1):
                f3.close()
                break
            else:
                f3.writelines(l1[m])
                m = m + 1

        elif (m != len1 and n != len2):
            firstprt1 = l1[m].split(" ")
            print(firstprt1)
            trt = firstprt1[0]
            t = trt.split(":")
            min1 = int(t[0]) * 60 + int(t[1])
            print(min1)

            firstprt2 = l2[n].split(" ")
            print(firstprt2)
            tdrt = firstprt2[0]
            t1 = tdrt.split(":")
            min2 = int(t1[0]) * 60 + int(t1[1])
            print(min2)

            if (min1 < min2):
                f3.writelines(l1[m])
                m = m + 1
            elif (min1 > min2):
                f3.writelines(l2[n])
                n = n + 1
            else:
                f3.writelines(l1[m])
                m = m + 1
                f3.writelines(l2[n])
                n = n + 1
        elif (m != len1 and n == len2):
            f3.writelines(l1[m])
            m = m + 1
        elif (n != len2 and m == len1):
            f3.writelines(l2[n])
            n = n + 1

    f1.close()
    f2.close()

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
         myObj = gTTS(text=myText,lang=language,slow=True)
         myObj.save("daily.mp3")
         playsound("daily.mp3")
    f.close()





