import sys

text = input('Change file names Y/N? ')

print(str(text.lower))
if (str(text.lower) == 'y'):
    print('changing file names')
else:
    print(text)