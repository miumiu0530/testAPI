#coding: utf8
import speech_recognition as sr
import csv
from itertools import islice
import os
from os import listdir
from os.path import isfile, join

r = sr.Recognizer()
print("input the path of the directory files you want to transcribe")
path = input()
print('Enter the CSV file absolute path that you want to write to.')
csv_path = input()

files = [f for f in listdir(path) if isfile(join(path, f))]

for file in files:
    file = str(file)
    file = path + "/" + file
    print(file)
    csv_entry_to_export = []
    csv_entry_to_export.append(file)
    print(csv_entry_to_export)
    audio_file = sr.AudioFile(file)
    print(audio_file)
    with audio_file as source:
        audio = r.record(source)
        text_from_audio_file = r.recognize_google(audio, language="ja", show_all=True)
        text_from_audio_file = str(text_from_audio_file)
        print(text_from_audio_file)
        csv_entry_to_export.append(text_from_audio_file)
        with open(csv_path, 'a', encoding='utf-8', errors='ignore') as new_file:
              wr = csv.writer(new_file, quoting=csv.QUOTE_ALL)
              wr.writerow(csv_entry_to_export)
              print(csv_entry_to_export)
