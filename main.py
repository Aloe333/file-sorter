import os
import re
import shutil

os.chdir('/Users/benjamin/Downloads')

files = os.listdir()

path = '/Users/benjamin/Documents/Files'

pattern_phys = '.*_2F'
pattern_math = '.*_2M'
pattern_bum = '.*_BUM'
pattern_obr = '*._OBR'

for file in files:
    file_path = os.path.join(os.getcwd(), file)
    
    if re.search(pattern_phys, file):
        new_file_path = os.path.join(path, 'School', '2F', file)
        shutil.move(file_path, new_file_path)
        print(file + ' has been moved to ' + new_file_path)
    
    elif re.search(pattern_math, file):
        new_file_path = os.path.join(path, 'School', '2M', file)
        shutil.move(file_path, new_file_path)
        print(file + ' has been moved to ' + new_file_path)
        
    elif re.search(pattern_bum, file):
        new_file_path = os.path.join(path, 'School', 'BUM', file)
        shutil.move(file_path, new_file_path)
        print(file + ' has been moved to ' + new_file_path)
        
        
            
            
            

