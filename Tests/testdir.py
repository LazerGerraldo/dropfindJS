# trying to figure out why the odering of photos gets scrambled after cropping in autofocus.py

import glob
import os

print('Named with wildcard *:')
flist=sorted(glob.glob('Example12/*.jpg'))

for name in flist:
    print(name)