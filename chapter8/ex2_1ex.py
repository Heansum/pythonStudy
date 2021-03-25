# test.txt 파일의 데이터를
# copy.txt 파일에 복사하세요

# test.txt 를 읽기 스트림으로 연다
# copy.txt
with open("C:/Users/ITPS/Desktop/textex.txt", "rt") as file:
    print("원본 파일 오픈")

    with open("C:/Users/ITPS/Desktop/copy.txt", "wt") as copy:
        print("복사 파일 오픈")

        print("복사 시작")

        while True:
            contents = file.readline()

            if contents == '':
                break
            else:
            copy.write(contents)

        print("복사 끝")

    print("원본 파일 스트림 닫음")

    # csv -> comma seperated value

