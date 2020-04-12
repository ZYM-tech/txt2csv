import csv
csvFile = open("/Users/zhangyiming/PycharmProjects/手写数字识别/20160401.csv",'w',newline='',encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("/Users/zhangyiming/PycharmProjects/手写数字识别/20160401.txt",'r',encoding='utf-8')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()