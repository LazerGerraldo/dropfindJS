# working on replacing the singular didget with a 0 in front for correct directory ordering

# example array of photo names
x = ['Folder\Folder_Name\Example12\B06_00_5_37_142467.jpg', 'Example12\B06_00_0_36_675800.jpg','Example12\B06_00_10_37_609133.jpg','Example12\B06_00_11_37_702467.jpg','Example12\B06_00_12_37_795800.jpg','Example12\B06_00_13_37_889133.jpg','Example12\B06_00_14_37_982467.jpg','Example12\B06_00_1_36_769133.jpg']


print(x)

# takes in a directory string and adds a 0 where nessary for sorting 
def addZero(str):
    z = str.split('\\')             # split the directory into folders and photo name 
    y = z[len(z) - 1].split('_')[2] # split to the third set of ID character that should start at 0 and increase by 1

    if len(y) <= 1:                 # if the photo ID only has 1 didgit, add a 0 before. Ex. _5 becomes _05
        print('adding 0 before singular digit')
        str = str.replace('_' + y, '_0' + y)

    return str

for a in x:
    print(addZero(a))

