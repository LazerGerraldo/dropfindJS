# trying to figure out why the odering of photos gets scrambled after cropping in autofocus.py
# renames photos in a directory by adding a 0 before 

import glob
import re

testdir = 'C:/Users/jamie/OneDrive/Shared_Files_Jan_Sci/Autofocus Images/J000972_AF_Temp/*.jpg'
# testdir = 'C:/Users/jamie/OneDrive/Shared_Files_Jan_Sci/Autofocus Images/ChrisTest/Compare3/*.jpg'
namelist = ['J001494_F04_00_5xVIS_0.10s_20211207183412.jpg',
            'J001494_F04_00_5xVIS_0.10s_20211207183342.jpg',
            'J001494_F04_00_5xVIS_0.10s_20211207183612.jpg',
            'J001494_F04_00_5xVIS_0.10s_20211207183624.jpg',
            'J001494_F04_00_5xVIS_0.10s_20211207183412.jpg',
            'J001494_F04_00_5xVIS_0.10s_20211207183430.jpg',
            'J001494_F04_00_5xVIS_0.10s_20211207183446.jpg',
            'J001494_F04_00_5xVIS_0.10s_20211207183501.jpg',
            'J001494_F04_00_5xVIS_0.10s_20211207183509.jpg',
            'J001494_F04_00_5xVIS_0.10s_20211207183528.jpg',
            'J001494_F04_00_5xVIS_0.10s_20211207183540.jpg',
            'J001494_F04_00_5xVIS_0.10s_20211207183554.jpg',
            'J001494_F04_00_5xVIS_0.10s_20211207183603.jpg']

flist=glob.glob(testdir)

# takes in a directory string and adds a 0 where nessary for sorting 
def addZero(str):
    z = str.split('\\')             # split the directory into folders and photo name 
    # y = z[len(z) - 1].split('_')[2] # split to the third set of ID character that should start at 0 and increase by 1
    # if (len(y) <= 1):  # if the photo ID only has 1 nonzero didgit, add a 0 before. Ex. _5 becomes _05
    #     # print('adding 0 before singular digit')
    #     # print(y + ' is less than 1 length')
    #     # print(str)
    #     str = str.replace('_' + y + '_', '_0' + y + '_')
    #     # print(str)

    
    y = z[len(z) - 1].split('_') # split photo id into array of strings
    print(y)
    for breaks in y: # created to add a 0 in front of any single digits in the broke up photo name regardless of photo index location
        if (len(breaks) <= 1):  # if the photo ID only has 1  nonzero didgit, add a 0 before. Ex. _5 becomes _05
            # print('adding 0 before singular digit')
            breaks = '0' + breaks
            break
    
    print(y)
    # a = '_'
    a = '_'.join(y)
    print('Joined string ' + a)
    return a

templist = []

# print('updating names')
# for name in flist:  # add zeros to file names)
#     print(name)
#     templist.append(addZero(name))
#     # os.rename(name, addZero(name)) # change file name 


for x in namelist:     # print new list of names
    print(x)

# lsorted = sorted(namelist, key=lambda x: int(os.path.splitext(x)[0]))

# flist.sort(key=lambda f: int(re.sub('\D', '', f)))
# flist.sort(key=lambda x: (x[2:]))
# flist.sort(key=lambda f: int(filter(str.isdigit, f)))
# x = 'abc_1.jpg'
# y = len(x)
# z = x[y - 5:y]
# print(z)

testdir.sort(key=lambda f: int(re.search(r'\d+', f[7:]).group()))

# print('sorting names')
for y in testdir:
    print(y)