# 성적 : 0 ~ 100
score = 50
# 과제 : 0 ~ 10
report = 10

# 성적이 80점 이상이면서 과제 점수가 10점이면 A+
# 성적이 80점 이상이면서 과제 점수가 10점이 아니면 A

if score >= 80:
    if report == 10:
        print("A+")

    if report != 10:
        print("A")

if score >= 80 and report == 10:
        print("A+")

if score >= 80 or report != 10:
        print("A")
