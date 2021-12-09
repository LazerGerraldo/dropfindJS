#saves input array 'vals' values to csv file named by input 'filename'

import csv
from os import write

sourceDir = ''
# stdProcessed = [8.125, 4.87, 6.25, 8.37, 9.84]
stdProcessed = [([22.49238861]),
 ([22.50870176]),
  ([22.80204149]),
   ([23.37823473]),
    ([23.92276118]),
     ([23.67763345]),
      ([23.52874076]),
       ([22.88798851]),
        ([22.86674918]),
         ([23.23593417]),
          ([23.21802298]),
           ([23.14552401]),
            ([23.13690641]),
             ([23.19942645])]
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

# new csvFile method to replace current one in autofocus.py
# pass standard deviation value and image name will write that to a csv file
def csvFile(imagename, stdval, csvfilename):
    with open(csvfilename, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(imagename, stdval)
        # for x in range(len(swriterows(imagename, stdval)imagename)):
            # writer.writerow([x, imagename[x], stdval[x][0]])


# old csvFile method in autofocus.py hoped to change the csv formatting with the new above method
# def csvFile(vals, filename):
#     excl = open(sourceDir + filename, 'w')
#     excl.write('Standard Deviation\n')
#     # for x in vals:
#     #     excl.write(str(x)+'\n')
#     for x in vals:
#         for y in x:
#             excl.write(str(y)+'\n')

#     excl.close()


csvFile(namelist, stdProcessed,  'csvwrite.csv')