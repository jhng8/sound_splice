import os

count = 0
for root_dir, cur_dir, files in os.walk(r'C:\Users\huang\OneDrive\Desktop\coding stuff\resp_data\exp\output'):
    count += len(files)
print('file count:', count)