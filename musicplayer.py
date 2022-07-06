from playsound import playsound

print("no. of avaiable songs\n1.rockabye\n2.godzilla\n3.gangster")

order = input('enter the music which you want to play')

if "rockabye" in order:
    playsound('C:\\Users\\hp\\Downloads\\rockabye.mp3')

elif "godzilla" in order:
    playsound('C:\\Users\\hp\\Downloads\\godzilla.mp3')

elif "gangster" in order:
    playsound('C:\\Users\\hp\\Downloads\\gangster.mp3')

   