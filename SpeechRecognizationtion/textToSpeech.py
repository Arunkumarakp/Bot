
import pyttsx


def text_to_speech(data):
	engine = pyttsx.init()
	engine.setProperty('rate', 180)
	engine.say(data)
	engine.runAndWait()

