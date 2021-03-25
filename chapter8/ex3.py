# csv -> comma seperated value
# 파일의 확장자: .jpg 이미지 -> 그냥 파일이름이다, 확장자는 윈도우를 위한 것
# .png 이미지
# .avi
# .mpeg

with open("C:/Users/ITPS/Desktop/covid.csv", "r") as file:
    file.readline()
    # 월별 검사 진행자의 수
    add = 0
    # 10월달 검사 진행자의 수
    month10Add = 0
    # 11월달 검사 진행자의 수
    month11Add = 0
    # 12월달 검사 진행자의 수
    month12Add = 0

    while True:
        contents = file.readline()

        if contents == "":
            break

        dataList = contents.split(",")
        dateInfo = dataList[0].split("-")
        print(dateInfo)

        # covid.csv 파일의 데이터를 읽어서
        # 월별 검사 진행자의 수를 출력하세요.
        if dateInfo[1] == '10':
            month10Add = month10Add + int(dataList[3])
        elif dateInfo[1] == '11':
            month11Add = month11Add + int(dataList[3])
        elif dateInfo[1] == '12':
            month12Add = month12Add + int(dataList[3])

        add = add + int(dataList[3])

    print("전체 검사 진행자의 수 = ", add)
    print("10월 검사 진행자의 수 = ", month10Add)
    print("11월 검사 진행자의 수 = ", month11Add)
    print("12월 검사 진행자의 수 = ", month12Add)



