# 파일 복사
# - 원본 파일에 들어있는 데이터를 읽어와서 변수에 저장한 뒤 새로운 파일에 저장하는 것
# 데이터의 종류
# - 텍스트 데이터 : 문자로 이루어진 데이터 / 주로 사람이 사용하는 데이터
# - 바이너리 데이터 : 0과 1로만 이루어진 데이터 / 주로 컴퓨터가 사용하는 데이터
#   - 음악, 동영상, 이미지 등...

# r - 입력 스트림 연결
# w, a - 출력 스트림 연결

# t - 텍스트 데이터를 위한 스트림
# b - 바이너리 데이터를 위한 스트림

# rt - 텍스트 데이터를 위한 입력 스트림
# wt, at - 텍스트 데이터를 위한 출력 스트림
# rb - 바이너리 데이터를 위한 입력 스트림
# wb, ab - 바이너리 데이터를 위한 출력 스트림

# 운영 체제 마다, 프로그래밍 언어 마다 줄바꿈 문자가 다름
# 윈도우 - \r\n
# 리눅스 - \n
# 유닉스, MacOs

# 파일 복사
# 원본 데이터를 읽어서 변수에 저장하고
# 새로운 파일에 변수에 저장되어있는 원본 데이터를 저장한다.
with open("C:/Users/ITPS/Desktop/source.mp4", "rb") as source:
    print("원본 파일 오픈")

    with open("C:/Users/ITPS/Desktop/copy.mp4", "wb") as copy:
        print("복사 파일 오픈")

        print("복사 시작")

        while True:
            buffer = source.read(1024)

            if not buffer:
                break

            copy.write(buffer)

        print("복사 끝")

    print("원본 파일 스트림 닫음")

    contents = source.read()

with open("C:/Users/ITPS/Desktop/destination.mp4", "wb") as destination:
    destination.write(contents)

# 책 - p243 참고

# test.txt 파일의 데이터를
# copy.txt 파일에 복사하세요

with open("C:/Users/ITPS/Desktop/textex.txt", "rt") as textex:
    print("원본 파일 오픈")

    with open("C:/Users/ITPS/Desktop/copy.txt", "wt") as copy:
        print("복사 파일 오픈")

        print("복사 시작")

        while True:
            buffer = textex.read(1024)

            if not buffer:
                break

            copy.write(buffer)

        print("복사 끝")

    print("원본 파일 스트림 닫음")




