import datetime

with open('/Users/admin/Desktop/Java/Hoc/SpringMVC/CollaborativeFiltering/CronTab/dateInfo.txt', 'a') as outFile:
    outFile.write('\n' + str(datetime.datetime.now()))