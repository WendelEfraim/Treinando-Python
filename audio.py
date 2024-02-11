import pyttsx3
engine = pyttsx3.init()
engine.say("Boas vindas ao seu computador. Oque temos para hoje Wendel? Podemos jogar, ou até mesmo programar algo a mais, que tal me ensinar mais alguma coisa?")
engine.runAndWait()

voice = engine.getProperty('voices')

# for voice in voices:
#     print(voice.name)