# -*- coding: utf8 -*-
from xmlParse import Data
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os



def Send(menu,companyNm,movieNm,Year,Month,Date, filename):
    select=str(input("이메일을 보내시겠습니까? y/n:  "))
    if select=='y' or select=='Y':
        senderAddr = 'kimsoo0826@naver.com'  # 보내는 사람
        recipientAddr = str(input("이메일 주소를 입력하세요 :  ")) # 받는 사람
        if menu == Data.DATEINFO:
            fp=open(str(Year)+str(Month)+str(Date)+'(Day).txt','rb')
            msg = MIMEText(fp.read(),_charset= 'utf8')
            fp.close()
            msg['Subject'] = Header('날짜('+str(Year)+str(Month)+str(Date)+')에 대한 영화 정보입니다','utf8')
        elif menu == Data.MOVIEINFO:
            fp=open(movieNm+'(MN).txt','rb')
            msg = MIMEText(fp.read(),_charset= 'utf8')
            fp.close()
            msg['Subject'] = Header('영화: '+movieNm+' 에 대한 정보입니다','utf8')
        elif menu == Data.COMPANYINFO:
            fp=open(companyNm+'(CN).txt','rb')
            msg = MIMEText(fp.read(),_charset= 'utf8')
            fp.close()
            msg['Subject'] = Header('영화사: '+companyNm+' 에 대한 영화 정보입니다','utf8')
        msg['From'] = senderAddr
        msg['To'] = recipientAddr


        s = smtplib.SMTP_SSL('smtp.naver.com',465)
        s.login( "kimsoo0826" , "666tkxks" ) # <아이디>, <암호>
        s.sendmail(senderAddr, recipientAddr, msg.as_string())
        s.quit()
        
        os.remove(filename)
    elif select=='n' or select=='N':
        os.remove(filename)
    else:
        select=str(input("다시 입력해주세요:  "))


#kimsoo0826@naver.com
#일단 텍스트를 불러와서 내용에 적용시키는것
#파일을 작성할때 원래있었던 같은 제목의 파일 삭제



#이게 되면 xml파일 txt로 바꿔서 보내기만 하면 끝.
