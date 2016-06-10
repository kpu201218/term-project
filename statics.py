import xml.etree.ElementTree as etree

def getfilelist():

    f = open('Database(Date).txt', 'r')
    data = f.read()
    countline = 0
    filelist = []

    for char in data:
        if char == '.':
            countline += 1
    f.close()


    f = open('Database(Date).txt', 'r')
    for i in range(countline):
        datalist = []
        filename = ''
        datalist += f.readline()

        for char in datalist:
            if char != '\n':
                filename += char

        filelist += [filename]
        
    f.close()
    makerank(filelist)
    filelist = []



def makerank(flist):
    ranklist = []
    rlist = []
    namelist = []
    sumlist = []
    

    for i in flist:
        tree = etree.parse(i)
        root = tree.getroot()
        for boxOfficeResult in root.iter("boxOfficeResult"):
            for dailyBoxOffice in boxOfficeResult.iter("dailyBoxOffice"):
                rlist += [[dailyBoxOffice.findtext('movieNm'),int(dailyBoxOffice.findtext('salesAcc'))]]


    for k in rlist:
        if k[0] in namelist:
            sumcount = 0
            for j in sumlist:
                if j[0] == k[0]:
                    sumlist[sumcount][0] = k[0]
                    sumlist[sumcount][1] += k[1]
                    break
                sumcount += 1
        else:
            namelist += [k[0]]
            sumlist += [[k[0], k[1]]]


    d1count = 0
    d2count = 0
    for data1 in sumlist:
        for data2 in sumlist:
            if data1[1] > data2[1]:
                temp = sumlist[d1count]
                sumlist[d1count] = sumlist[d2count]
                sumlist[d2count] = temp
            d2count += 1
        d1count += 1
        d2count = 0

    ranklist = sumlist

    count = 0
    print('\n총 매출 통계 순위\n')
    for data in ranklist:
        count += 1
        if count < 11:
            print('매출 %d위 영화 : %s\n%s원\n' %(count, data[0], data[1]))

    print('\n\n')
        
        
        
