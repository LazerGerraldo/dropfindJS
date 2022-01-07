# testing sorting of images based on the timestamp or
#  final set of numbers in the *.jpg

import glob
import re

sourceDir = 'C:/Users/jamie/OneDrive/Shared_Files_Jan_Sci/Autofocus Images/J000972_AF_Temp/Set1/*.jpg'            # photo source folder end in '/'
flist=glob.glob(sourceDir)

print('unsorted list')
for x in flist:
    print(x)
#----------DO NOT DELETE--------------------------------------------------------------    
flist.sort(key=lambda f: int(re.search(r'\d+', f[len(f)-6:]).group()))
#----------DO NOT DELETE--------------------------------------------------------------
print('sorted list')
for y in flist:
    print(y)
