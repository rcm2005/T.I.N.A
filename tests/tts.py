import pyttsx3
import pyttsx4

engine = pyttsx4.init()

voices = engine.getProperty('voices')
engine.setProperty("voice", voices[-1].id)


# engine = pyttsx3.init()
engine.say("olá, eu sou a Tina, em que posso ajudar ?")
engine.runAndWait()

# engine = pyttsx4.init()
# engine.say('olá, eu sou a Tina, em que posso ajudar ?')
# engine.runAndWait()

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# for voice in voices:
#    engine.setProperty('voice', voice.id)
#    engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()