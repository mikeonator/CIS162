# Week 2 - CIS162 - MAudi - Graphic File Exercise

import matplotlib.pyplot as plot

# set up your lists
numlist = [2790, 2026, 281, 2599]
namelist = ['Transfer Programs', 'Career & Technical Education Programs',
            'Associate of General Studies', 'Non-Degree Seeking']
colorlist = ['blue', 'green', 'yellow', 'red']
# offset each slice of the pie from the center
explodelist = [0.1, 0.05, 0, 0.08]

# make the pie charts
# 2 decimal places
plot.pie(numlist, labels=namelist, autopct='%.2f%%', colors=colorlist,  # autopct - '%[flags][width][.precision]type%'
         explode=explodelist, startangle=180)
plot.axis('equal')
plot.savefig('COCCEnrollmentByProgram1.png')
plot.close()

# no decimal places
plot.pie(numlist, labels=namelist, autopct='%.0f%%', colors=colorlist,  # autopct - '%[flags][width][.precision]type%'
         explode=explodelist, startangle=180)
plot.axis('equal')
plot.savefig('COCCEnrollmentByProgram2.png')
plot.close()

# 1 decimal place
plot.pie(numlist, labels=namelist, autopct='%.1f%%', colors=colorlist,  # autopct - '%[flags][width][.precision]type%'
         explode=explodelist, startangle=180)
plot.axis('equal')
plot.savefig('COCCEnrollmentByProgram3.png')
plot.close()
