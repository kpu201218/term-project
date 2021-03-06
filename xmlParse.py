import urllib.request
from urllib.parse  import quote
import xml.etree.ElementTree as etree



class Data:
    NONESELECTED = 0
    DATEINFO = 1
    MOVIEINFO = 2
    COMPANYINFO = 3

    def __init__(self):
        self.key = '25c645dd98b8860db1cf3d56076d3b03'
        self.Year = '9999'
        self.Month = '9999'
        self.Date = '9999'
        self.targetDt = None
        self.movieNm= None
        self.companyNm= None
        self.select_menu = self.NONESELECTED
        self.filename = None
        self.datafilename = None
        self.url = None
        self.tree = None
        self.root = None

    def parse(self, menu):
        self.select_menu = menu
        if self.select_menu == self.DATEINFO:
            self.url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?key=%s&targetDt=%s" % (self.key, self.targetDt)
            data = urllib.request.urlopen(self.url).read()
            self.filename = self.targetDt + ".xml"
            self.datafilename = self.filename
        elif self.select_menu == self.MOVIEINFO:
            self.url="http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.xml?key=%s&movieNm="%self.key + quote('%s'%self.movieNm)
            data = urllib.request.urlopen(self.url).read()
            self.filename = self.movieNm + ".xml"
        elif self.select_menu == self.COMPANYINFO:
            self.url="http://kobis.or.kr/kobisopenapi/webservice/rest/company/searchCompanyList.xml?key=%s&companyNm="%self.key + quote('%s'%self.companyNm)
            data = urllib.request.urlopen(self.url).read()
            self.filename = self.companyNm + ".xml"
        f = open(self.filename, "wb")
        f.write(data)
        f.close()
        if self.datafilename != None:
            f = open('Database(Date).txt', 'a')
            f.write(self.datafilename + '\n')
            f.close
            self.datafilename = None
        self.tree = etree.parse(self.filename)
        self.root = self.tree.getroot()
            
    def printInfo(self, menu):
        self.select_menu = menu
        if self.select_menu == self.DATEINFO:
            for boxOfficeResult in self.root.iter("boxOfficeResult"):
                for dailyBoxOffice in boxOfficeResult.iter("dailyBoxOffice"):
                    f = open(self.targetDt+'(Day).txt','a')
                    self.filename = self.targetDt+'(Day).txt'
                    f.write('영화 제목\t'+dailyBoxOffice.findtext('movieNm')+"\n"+'개봉 날짜\t'+dailyBoxOffice.findtext('openDt')+"\n"
                            +'일일 매출\t'+dailyBoxOffice.findtext('salesAmt')+"\n"+'매출 총액 대비 비율\t'+dailyBoxOffice.findtext('salesShare')+"\n"
                            '매출 증감\t'+dailyBoxOffice.findtext('salesInten')+"\n"+'매출 증감 비율\t'+dailyBoxOffice.findtext('salesChange')+"\n"
                            +'누적 매출\t'+dailyBoxOffice.findtext('salesAcc')+"\n"+'오늘의 관객수\t'+dailyBoxOffice.findtext('audiCnt')+"\n"
                            '관객수 증감\t'+dailyBoxOffice.findtext('audiInten')+"\n"+'관객수 증감 비율\t'+dailyBoxOffice.findtext('audiChange')+"\n"
                            +'누적 관객수\t'+dailyBoxOffice.findtext('audiAcc')+"\n"+'오늘 상영한 스크린수\t'+dailyBoxOffice.findtext('scrnCnt')+"\n"
                            '오늘 상영 횟수\t'+dailyBoxOffice.findtext('showCnt')+"\n\n")
                    f.close()
                    print('--------------------------------------------------------------')
                    print('영화 제목\t\t:' + dailyBoxOffice.findtext('movieNm'))
                    print('개봉 날짜\t\t:' + dailyBoxOffice.findtext('openDt'))
                    print('일일 매출\t\t:' + dailyBoxOffice.findtext('salesAmt'))
                    print('매출 총액 대비 비율\t:' + dailyBoxOffice.findtext('salesShare'))
                    print('매출 증감\t\t:' + dailyBoxOffice.findtext('salesInten'))
                    print('매출 증감 비율\t\t:' + dailyBoxOffice.findtext('salesChange'))
                    print('누적 매출\t\t:' + dailyBoxOffice.findtext('salesAcc'))
                    print('오늘의 관객수\t\t:' + dailyBoxOffice.findtext('audiCnt'))
                    print('관객수 증감\t\t:' + dailyBoxOffice.findtext('audiInten'))
                    print('관객수 증감 비율\t:' + dailyBoxOffice.findtext('audiChange'))
                    print('누적 관객수\t\t:' + dailyBoxOffice.findtext('audiAcc'))
                    print('오늘 상영한 스크린수\t:' + dailyBoxOffice.findtext('scrnCnt'))
                    print('오늘 상영 횟수\t\t:' + dailyBoxOffice.findtext('showCnt'))
                    print('--------------------------------------------------------------')

                    
        elif self.select_menu==self.MOVIEINFO:
            for movieListResult in self.root.iter("movieListResult"):
                for movie in movieListResult.iter("movie"):
                    f = open(self.movieNm+'(MN).txt','a')
                    self.filename = self.movieNm+'(MN).txt'
                    f.write('영화 제목\t'+movie.findtext('movieNm')+"\n"+'영화 제목\t'+movie.findtext('movieNmEn')+"\n"
                            +'제작연도\t'+movie.findtext('prdtYear')+"\n"+'개봉연도\t'+movie.findtext('openDt')+"\n"
                            '영화유형\t'+movie.findtext('typeNm')+"\n"+'제작국가\t'+movie.findtext('nationAlt')+"\n"
                            +'영화장르\t'+movie.findtext('genreAlt')+"\n\n")
                    f.close()
                    print('--------------------------------------------------------------')
                    print('영화 제목\t:' + movie.findtext('movieNm'))
                    print('영화 제목\t:' + movie.findtext('movieNmEn'))
                    print('제작연도\t:' + movie.findtext('prdtYear'))
                    print('개봉연도\t:' + movie.findtext('openDt'))
                    print('영화유형\t:' + movie.findtext('typeNm'))
                    print('제작국가\t:' + movie.findtext('nationAlt'))
                    print('영화장르\t:' + movie.findtext('genreAlt'))
                    print('--------------------------------------------------------------')
        elif self.select_menu==self.COMPANYINFO:
            for companyListResult in self.root.iter("companyListResult"):
                for company in companyListResult.iter("company"):
                    f = open(self.companyNm+'(CN).txt','a')
                    self.filename = self.companyNm+'(CN).txt'
                    f.write('영화사명\t'+company.findtext('companyNm')+"\n"+'영화사명\t'+company.findtext('companyNmEn')+"\n"
                            +'영화사분류\t'+company.findtext('companyPartNames')+"\n"+'대표자명\t'+company.findtext('ceoNm')+"\n\n")
                    f.close()
                    print('--------------------------------------------------------------')
                    print('영화사명\t:' + company.findtext('companyNm'))
                    print('영화사명\t:' + company.findtext('companyNmEn'))
                    print('영화사분류\t:' + company.findtext('companyPartNames'))
                    print('대표자명\t:' + company.findtext('ceoNm'))
                    print('--------------------------------------------------------------')
        return self.filename


if __name__ == "__main__":
    main()

