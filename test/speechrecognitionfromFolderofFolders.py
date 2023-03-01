import subprocess
#if this subprocess works it would be good for silence segmenting as well
import os
import csv
from os import listdir
from os.path import isfile, join
import speech_recognition as sr
from random import randint
from time import sleep

r = sr.Recognizer() #initialize instance


print("put in path")
main_folder = input()
print('Enter the CSV file absolute path that you want to write to.')
csv_path = input()
# sub_folders = [f for f in listdir(main_folder) if isfile(join(main_folder, f))]
sub_folders = [x[0] for x in os.walk(main_folder)] #deals with DS
sub_folders = sorted(sub_folders)

print(sub_folders)

for sub_folder in sub_folders:
    files_in_subfolder = [f for f in listdir(sub_folder) if isfile(join(sub_folder, f))]
    print(sub_folder)
    files_in_subfolder = sorted(files_in_subfolder)
    print(files_in_subfolder)
    # print("files_in_subfolder: " + files_in_subfolder)
    # subfolder =
    for file in files_in_subfolder:
        absolute_file = sub_folder + "/" + file
        print("file: " + file)
        print("absolute file path: " + absolute_file)
        # new_folder = sub_folder[21:]
        # print("new folder: " + new_folder)
        # new_file_path = new_folder + '/' + file
        # print('new file path: ' + new_file_path)
        csv_entry_to_export = []
        csv_entry_to_export.append(absolute_file)
        print(csv_entry_to_export)
        audio_file = sr.AudioFile(absolute_file)
        print(audio_file)
        with audio_file as source:
            audio = r.record(source)
            text_from_audio_file = r.recognize_google(audio, language="ko", show_all=True) #requires these to read japanese
            text_from_audio_file = str(text_from_audio_file) #converts dict to text
            print("text from audio file: " + text_from_audio_file)
            csv_entry_to_export.append(text_from_audio_file)
            with open(csv_path, 'a', encoding='utf-8', errors='ignore') as new_file:
                  wr = csv.writer(new_file, quoting=csv.QUOTE_ALL)
                  wr.writerow(csv_entry_to_export)
                  print(csv_entry_to_export)
                  sleep(randint(4,6))
