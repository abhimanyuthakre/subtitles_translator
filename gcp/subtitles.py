# -*- coding: utf-8 -*-
### The comments with 3 # represents the code for Google Cloud Translate API. 
### Currently this code is using the library provided by "googletrans". 
import io
import os
from googletrans import Translator
###from google.cloud import translate

inputs = input("Enter languages!" + "\n")
s = inputs.split(" ")
filename = input("Enter filename without extension!" + "\n")
if inputs == "all":
	s = ['af','sq','am','ar','hy','az','eu','bn','bs',
		 'bg','ca','ceb','zh-CN','zh-TW','co','hr','cs',
		 'da','nl','eo','et','fi','fr','fy','gl','ka','de',
		 'el','gu','ht','ha','haw','iw','hi','hmn','hu',
		 'is','ig','id','ga','it','ja','jw','kn','kk','km',
		 'ko','ku','lo','lv','lt','lb','mk','mg','ms','ml',
		 'mt','mi','mr','mn','ne','no','ny','ps','fa','pl',
		 'pt','pa','ro','ru','sm','gd','sr','st','sn','sd',
		 'si','sk','sl','so','es','sw','sv','tl','tg','ta',
		 'te','th','tr','uk','ur','uz','vi','cy','xh','yi',
		 'yo','zu', 'en']

translator = Translator(service_urls=['translate.google.com'])

def translate_text(text, target):
	"""Translates text into the target language.

	Target must be an ISO 639-1 language code.
	See https://g.co/cloud/translate/v2/translate-reference#supported_languages
	"""
	###translate_client = translate.Client()

	# Text can also be a sequence of strings, in which case this method
	# will return a sequence of results for each text.
	###result = translate_client.translate(text, target_language=target)

	###return result['translatedText']

	result = translator.translate(text, target)
	return result.text

for lang in s:
	with io.open(filename + "_" + lang + ".srt",'wb') as hi:
		with io.open(filename + ".srt",'r') as file:
			contents = file.readlines()
			contents[0] = "1\n"
			for i in range(len(contents)):	
				if contents[i][0].isdigit():
					hi.write(contents[i].encode())
				else:
					receive = translate_text(contents[i], lang)			 
					hi.write((receive + "\n").encode())
