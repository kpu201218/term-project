from xmlParse import Data
import time
import calendar
import sendmail



def search():

    menu = 0

    print("------------메뉴-------------")
    print("1. 날짜별")
    print("2. 영화제목")
    print("3. 회사이름")
    print("------------------------------")

    while(menu < 1 or menu > 3):
        menu = int(input("메뉴를 선택하세요:  "))
        print('\n\n')

    inputdata(menu)



def inputdata(menu):

    data = Data()
    timebuf = []
    callenderdict = {'Jan': 1, 'Fab': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}

    datelist=[a for a in range(8)]
    Year = 9999
    Month = 1
    Date = 1
    movieNm=None
    companyNm=None
    Yearcheck = False
    Monthcheck = False
    error = 0

    if menu == data.DATEINFO and error == 0:
        timebuf = time.ctime().split()

        while(1):
            datelist=input("날짜를 8자로 입력해주세요:    ")

            for check in datelist:
                if check >= '0' and check <= '9':
                    pass
                else:
                    error = 1
                    print("숫자로 입력해주세요")
                    break
                    
            if error == 0:
                while int(datelist)<10000000 or int(datelist)>=100000000:
                    datelist=input("자리수가 다릅니다. 날짜를 8자로 입력해주세요:    ")
                break
            else:
                error = 0

        Year=datelist[0]+datelist[1]+datelist[2]+datelist[3]
        Month=datelist[4]+datelist[5]
        Date=datelist[6]+datelist[7]


    if menu == data.DATEINFO and error == 0:
        timebuf = time.ctime().split()
        if int(Year) == int(timebuf[4]):
            Yearcheck = True
        else:
            Yearcheck = False
        if int(Year) > int(timebuf[4]) or int(Year)<1000:
            print("년도가 잘못 입력되었습니다.\n")
            error = 1



        if int(Month) == callenderdict[timebuf[1]] and Yearcheck == True:
            Monthcheck = True
        else:
            Monthcheck = False

        if Yearcheck == False and (int(Month) > 12 or int(Month) < 1) and error == 0:
            print("달이 잘못 입력되었습니다.\n")
            error = 1

        elif error == 0 and Yearcheck == True and int(Month) > int(callenderdict[timebuf[1]]):
            print("이미 지나간 날짜만 검색할 수 있습니다.\n")
            error = 1



        if error == 0 and int(Date) > calendar.monthrange(int(Year), int(Month))[1]:
            print("날짜가 잘못 입력되었습니다.\n")
            error = 1
        if error == 0 and Yearcheck and Monthcheck and int(Date) >= int(timebuf[2]):
            print("이미 지나간 날짜만 검색할 수 있습니다.\n")
            error = 1
            
        if error == 0:
            data.Year = str(Year)
            data.Month = str(Month)
            data.Date = str(Date)
            data.targetDt = data.Year + data.Month + data.Date


    elif menu == data.MOVIEINFO and error == 0:
        movieNm=str(input("영화를 입력하세요 :  "))
        data.movieNm=movieNm

    elif menu == data.COMPANYINFO and error == 0:
        companyNm=str(input("영화사를 입력하세요 :  "))
        data.companyNm=companyNm

    if error == 0:
        data.parse(menu)
        filename = data.printInfo(menu)

        print('\n\n')
        sendmail.send(menu,companyNm,movieNm,Year,Month,Date, filename)


    del(data)

    if error == 1:
        inputdata(menu)
    



if __name__ == "__main__":
    datelist(menu)


