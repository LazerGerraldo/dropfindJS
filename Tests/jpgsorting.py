import re

# takes in photo name splits the last 6 chars takes the int of that
# A00_00_0.jpg, uses _0.jpg, and returns the integer 0
def sortAF(a):
    return int(re.search(r'\d+', a[len(z)-6:]).group())

x = 'abc_1.jpg'
a = ['A00_00_11.jpg','A00_00_0.jpg','A00_00_14.jpg','A00_00_10.jpg', 'A00_00_1.jpg', 'B00_00_1.jpg', 'A01_00_1.jpg']
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
w = 'J001494_F04_00_5xVIS_0.10s_20211207183412.jpg'

# print(a)
z = 'A00_00_1.jpg'
# counts on first 7 char before the photo number
# print(z)
# print(z[7:])
# print(int(re.search(r'\d+', z[7:]).group()))

# uses last 6 char in photo id for sorting
# print(z)
# print(z[len(z)-6:])
# print(int(re.search(r'\d+', z[len(z)-6:]).group()))

a.sort(key=lambda f: int(re.search(r'\d+', f[len(f)-6:]).group()))

# a.sort(key=sortAF)
print(a)