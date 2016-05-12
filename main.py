import urllib.request
import xml.etree.ElementTree as etree

def main():

   
    key = '25c645dd98b8860db1cf3d56076d3b03'
    Year = '2016'
    Month = '05'
    Date = '01'
    targetDt = Year + Month + Date
    url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?key=%s&targetDt=%s" % (key, targetDt) 

    data = urllib.request.urlopen(url).read()

    filename = "sample2.xml"
    f = open(filename, "wb") 
    f.write(data)
    f.close()

    #파싱하기
    tree = etree.parse(filename)
    root = tree.getroot()

    for boxOfficeResult in root.iter("boxOfficeResult"):
        for dailyBoxOffice in boxOfficeResult.iter("dailyBoxOffice"):
            print('--------------------------------------------------------------')
            print('영화 제목\t:' + dailyBoxOffice.findtext('movieNm'))
            print('개봉 날짜\t:' + dailyBoxOffice.findtext('openDt'))
            print('일일 매출\t :' + dailyBoxOffice.findtext('salesAmt'))
            print('매출 총액 대비 비율\t :' + dailyBoxOffice.findtext('salesShare'))
            print('매출 증감\t :' + dailyBoxOffice.findtext('salesInten'))
            print('매출 증감 비율\t :' + dailyBoxOffice.findtext('salesChange'))
            print('누적 매출\t  :' + dailyBoxOffice.findtext('salesAcc'))
            print('오늘의 관객수\t :' + dailyBoxOffice.findtext('audiCnt'))
            print('관객수 증감\t :' + dailyBoxOffice.findtext('audiInten'))
            print('관객수 증감 비율\t :' + dailyBoxOffice.findtext('audiChange'))
            print('누적 관객수\t :' + dailyBoxOffice.findtext('audiAcc'))
            print('오늘 상영한 스크린수\t :' + dailyBoxOffice.findtext('scrnCnt'))
            print('오늘 상영 횟수\t :' + dailyBoxOffice.findtext('showCnt'))
            print('--------------------------------------------------------------')


            
if __name__ == "__main__":
    main()
