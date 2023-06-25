import csv
from pydub import AudioSegment
import os

with open("101_1b1_Al_sc_Meditron.txt") as tsv:

    index = 1

    for line in csv.reader(tsv, dialect="excel-tab"):
        start = line[0]
        end = line[1]

        print(index)
        print("start: " + start)
        print("end: " +  end)

        t1 = float(start) * 1000 #Works in milliseconds
        t2 = float(end) * 1000

        old_audio = AudioSegment.from_wav("101_1b1_Al_sc_Meditron.wav")
        newAudio = old_audio[t1:t2]

        #newAudio.export('newSong' + str(index) + '.wav', format="wav")
        newAudio.export(r"C:\Users\huang\OneDrive\Desktop\coding stuff\resp_data\exp\output\101_1b1_Al_sc_Meditron" + "\\" + str(index), format="wav")

        index += 1