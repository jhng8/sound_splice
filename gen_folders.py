import csv
import os, glob
from pathlib import Path

path = r'C:\Users\huang\OneDrive\Desktop\coding stuff\resp_data\exp\files\Respiratory_Sound_Database\audio_and_txt_files'

parent_dir = r"C:\Users\huang\OneDrive\Desktop\coding stuff\resp_data\exp\output"

mode = 0o666

for filename in glob.glob(os.path.join(path, '*.txt')):

    raw_file_name = Path(filename).stem
    wav_file_name = raw_file_name + ".wav"
    # print(text_file_name)
    # print(wav_file_name)

    directory = raw_file_name

    with open(os.path.join(os.getcwd(), filename), 'r') as tsv:
        
        # Path
        path = os.path.join(parent_dir, directory)

        os.mkdir(path, mode)
        print("Directory '% s' created" % directory)
  
