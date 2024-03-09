
import pyttsx3

if __name__ == '__main__':
    print("Welcome  CyberVoice!! Created By @Deepansh")
    engine = pyttsx3.init()
    while True:
        x = input("Enter what you want to speak: ")
        if x == 'q':
           break
        engine.say(x)
        engine.runAndWait()
       