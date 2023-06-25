import csv
import os, glob
from pathlib import Path
from pydub import AudioSegment

path = r'C:\Users\huang\OneDrive\Desktop\coding stuff\resp_data\exp\files\Respiratory_Sound_Database\audio_and_txt_files'

# opens all the text files found at path dir
for filename in glob.glob(os.path.join(path, '*.txt')):

    # removes .txt ending from filename
    raw_file_name = Path(filename).stem

    # name of wav file to be exported
    wav_file_name = raw_file_name + ".wav"

    # corresponding wav file from text file
    old_audio = AudioSegment.from_wav(r'files\Respiratory_Sound_Database\audio_and_txt_files' + '\\' + wav_file_name)

    # export path
    export_path = r'C:\Users\huang\OneDrive\Desktop\coding stuff\resp_data\exp\output' + '\\' + raw_file_name

    # opens text file
    with open(os.path.join(os.getcwd(), filename), 'r') as tsv:
        index = 1
        for line in csv.reader(tsv, dialect="excel-tab"):
            start = line[0]
            end = line[1]

            # print(index)
            # print("start: " + start)
            # print("end: " +  end)

            # start and end of clip in milliseconds
            t1 = float(start) * 1000 
            t2 = float(end) * 1000

            newAudio = old_audio[t1:t2]

            # export wav file
            #newAudio.export('newSong' + str(index) + '.wav', format="wav")
            newAudio.export(export_path + "\\" + raw_file_name + "_V" + str(index) + ".wav", format="wav")

            index += 1