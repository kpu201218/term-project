from xmlParse import Data
import time
import calendar

def main():
    data = Data()
    timebuf = []
    callenderdict = {'Jan': 1, 'Fab': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}


    while(1):
        menu = 0
        Year = 9999
        Month = 9999
        Date = 9999
        Yearcheck = False
        Monthcheck = False
    


    
        print("------------메뉴-------------")
        print("1. 날짜별")
        print("2. 영화제목")
        print("3. 회사이름")
        print("------------------------------")

        while(menu < 1 or menu > 3):
            menu = int(input("메뉴를 선택하세요:  "))
            print('\n\n')
        if menu == data.DATEINFO:
            timebuf = time.ctime().split()
            while int(Year) > int(timebuf[4]):
                Year = int(input("년도를 입력하세요 :  "))
                if int(Year) == int(timebuf[4]):
                    Yearcheck = True
                else:
                    Yearcheck = False

                if int(Year) > int(timebuf[4]):
                    print("년도를 잘못입력되었습습니다.\n")
    

            
            while ((Yearcheck == False and (int(Month) > 12 or int(Month) < 1)) or (Yearcheck == True and int(Month) > int(callenderdict[timebuf[1]]))) :
                Month = int(input("달을 입력하세요 :  "))
                if int(Month) == callenderdict[timebuf[1]] and Yearcheck == True:
                    Monthcheck = True
                else:
                    Monthcheck = False 
                if Month < 10:
                    Month = '0' + str(Month)
                else:
                    Month = str(Month)

                if Yearcheck == False and (int(Month) > 12 or int(Month) < 1):
                    print("달을 잘못입력되었습니니다.\n")
                elif Yearcheck == True and int(Month) > int(callenderdict[timebuf[1]]):
                    print("이미 지나간 날짜만 검색할 수 있습니다.\n")
                

                
            while (Yearcheck and Monthcheck and (int(Date) >= int(timebuf[2])) or int(Date) > calendar.monthrange(int(Year), int(Month))[1]):
                Date = (input("일을 입력하세요 :  "))
                if int(Date) > calendar.monthrange(int(Year), int(Month))[1]:
                    print("날짜가 잘못입력되었습니다.\n")
                if Yearcheck and Monthcheck and int(Date) >= int(timebuf[2]):
                    print("이미 지나가 날짜만 검색할 수 있습니다.\n")

                
                if int(Date) < 10:
                    Date = '0' + str(Date)

            
            data.Year = str(Year)
            data.Month = str(Month)
            data.Date = str(Date)
            data.targetDt = data.Year + data.Month + data.Date
    
        data.parse(menu)
        data.printInfo(menu)
        print('\n\n')

    



if __name__ == "__main__":
    main()

