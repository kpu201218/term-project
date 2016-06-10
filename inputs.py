from xmlParse import Data
import time
import calendar
import sendmail



def Search():

    menu = 0

    print("------------메뉴-------------")
    print("1. 날짜별")
    print("2. 영화제목")
    print("3. 회사이름")
    print("------------------------------")

    while(menu < 1 or menu > 3):
        menu = int(input("메뉴를 선택하세요:  "))
        print('\n\n')

    TEST(menu)



def TEST(menu):

    data = Data()
    timebuf = []
    callenderdict = {'Jan': 1, 'Fab': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}

    test=[a for a in range(8)]
    Year = 9999
    Month = 1
    Date = 1
    movieNm=None
    companyNm=None
    Yearcheck = False
    Monthcheck = False

    if menu == data.DATEINFO:
        timebuf = time.ctime().split()

        test=input("날짜를 8자로 입력해주세요:    ")

        while int(test)<10000000 or int(test)>=100000000:
            test=input("자리수가 다릅니다. 날짜를 8자로 입력해주세요:    ")

        Year=test[0]+test[1]+test[2]+test[3]
        Month=test[4]+test[5]
        Date=test[6]+test[7]


    if menu == data.DATEINFO:
        timebuf = time.ctime().split()
        while int(Year) > int(timebuf[4]) or int(Year)<1000:
            Year = int(input("년도를 입력하세요 :  "))
            if int(Year) == int(timebuf[4]):
                Yearcheck = True
            else:
                Yearcheck = False
            if int(Year) > int(timebuf[4]) or int(Year)<1000:
                print("년도를 잘못입력되었습니다.\n")
                TEST(menu)


        while ((Yearcheck == False and (int(Month) > 12 or int(Month) < 1)) or (Yearcheck == True and int(Month) > int(callenderdict[timebuf[1]]))) :
            if int(Month) == callenderdict[timebuf[1]] and Yearcheck == True:
                Monthcheck = True
            else:
                Monthcheck = False

            if Yearcheck == False and (int(Month) > 12 or int(Month) < 1):
                print("달을 잘못입력되었습니니다.\n")
                TEST(menu)

            elif Yearcheck == True and int(Month) > int(callenderdict[timebuf[1]]):
                print("이미 지나간 날짜만 검색할 수 있습니다.\n")
                TEST(menu)


        while (Yearcheck and Monthcheck and (int(Date) >= int(timebuf[2])) or int(Date) > calendar.monthrange(int(Year), int(Month))[1]):
            if int(Date) > calendar.monthrange(int(Year), int(Month))[1]:
                print("날짜가 잘못입력되었습니다.\n")
                TEST(menu)
            if Yearcheck and Monthcheck and int(Date) >= int(timebuf[2]):
                print("이미 지나간 날짜만 검색할 수 있습니다.\n")
                TEST(menu)
        data.Year = str(Year)
        data.Month = str(Month)
        data.Date = str(Date)
        data.targetDt = data.Year + data.Month + data.Date


    elif menu == data.MOVIEINFO:
        movieNm=str(input("영화를 입력하세요 :  "))
        data.movieNm=movieNm

    elif menu == data.COMPANYINFO:
        companyNm=str(input("영화사를 입력하세요 :  "))
        data.companyNm=companyNm


    data.parse(menu)
    filename = data.printInfo(menu)

    print('\n\n')
    sendmail.Send(menu,companyNm,movieNm,Year,Month,Date, filename)
    Search()



    


if __name__ == "__main__":
    TEST(menu)


