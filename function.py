import os
import re
import shutil

searchPathInput = ''
searchPath = '/Users/benjamin/' + searchPathInput

os.chdir(searchPath)

#os.chdir('/Users/benjamin/Downloads')

files = os.listdir()

path = ''
#path = '/Users/benjamin/Documents/Files'

patternInput = ''
pattern = '.*_' + patternInput

for file in files:
    file_path = os.path.join(os.getcwd(), file)
    
    if re.search(pattern, file):
        new_file_path = os.path.join(path, patternInput, file)
        shutil.move(file_path, new_file_path)
        outputText = file + ' has been moved to ' + new_file_path
        
    else:
        outputText = 'No matching file found'
    
        
        
            
            
            

