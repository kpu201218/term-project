import inputs

def main():

        
    print("------------메뉴-------------")
    print("1. 검색")
    print("2. 날짜데이터 통계")
    print("------------------------------")

    while(1):
        
        print("------------메뉴-------------")
        print("1. 검색")
        print("2. 날짜데이터 통계")
        print("------------------------------")

        menu = int(input("메뉴를 선택하세요: "))
        print('\n')

        if menu == 1:
            inputs.Search()
        elif menu == 2:
            pass
        else:
            print("잘못된 입력입니다. 다시 시도하세요.\n")
    

if __name__ == "__main__":
    main()
