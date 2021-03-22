# 내가 한 풀이
student = ["김철수", "고영희", "홍길동", "이영수", "최영길"]       # 이름
score = [36, 70, 83, 59, 61]                                  # 점수

student[0] = score[0]
student[1] = score[1]
student[2] = score[2]
student[3] = score[3]
student[4] = score[4]

for score in student:
    if score > 60 :
        print("합격입니다")
    else:
        print("불합격입니다")
#

student = [["김철수", 36],
           ["고영희", 70],
           ["홍길동", 83],
           ["이영수", 59],
           ["최영길", 61]]       # 이름

scoreList = student[][]         # 점수

#student[0][1] # -> 가능하다

for score in student:
    if score > 60 :
        print("합격입니다")
    else:
        print("불합격입니다")
#

# answer

scoreList = [36, 70, 83, 59, 61]
for score in scoreList:
    if score > 60:
        print("합격")
    else:
        print("불합격")

