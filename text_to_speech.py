# a short script to demo text to speech

import pyttsx3
engine = pyttsx3.init()
newVoiceRate = 70
engine.setProperty('rate',newVoiceRate)
engine.say('Hello everyone in CS 1063, this is a python example of text to speech generation')
engine.runAndWait()