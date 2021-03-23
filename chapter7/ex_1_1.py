kor1 = 0
while True:
    print("첫 번째 학생의 국어 점수: ", end="")
    kor1 = int(input())
    if 0 <= kor1 and kor1 <= 100:
        break
    else:
        print("0 ~ 100점 사이로 입력해주세요")

# --> 함수로 변환
def inputKor():
    while True:
        print("국어 점수: ", end="")
        kor = int(input())
        if 0 <= kor and kor <= 100:
            break
        else:
            print("0 ~ 100점 사이로 입력해주세요")

    return kor


kor1 = inputkor()
kor2 = inputkor()
kor3 = inputkor()
