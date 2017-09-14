import textToSpeech as ts
import sys
import os
def check_response(data):
	print data
	if data.lower() in ['hi','hello']:
		data = 'Hi hello'
	
	elif data.lower() == 'thanks':
		data = 'welcome'
	elif data.lower() == 'take photo':
		data = 'Take Photo'
		os.system('python snapshot.py')
	elif data.lower() == 'bye':
		ts.text_to_speech('Good bye')
		sys.exit()
	elif data.lower() == 'time please':
		from datetime import datetime
		data = datetime.now().strftime('%H hours %M minutes')	
	else:
		data = "you said: " + data	
	ts.text_to_speech(data)
	print data
