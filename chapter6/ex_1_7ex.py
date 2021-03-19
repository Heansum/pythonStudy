print("중간고사 성적은? ", end="")
score = input()
score = int(score)

print("리포트 성적은? ", end="")
report = input()
report = int(report)

if score >= 50:
    if report >= 5:
        print("Perfect Pass")

    if report < 5:
        print("Pass")

if score < 50:
    if report >= 5:
        print("Fail")

    if report < 5:
        print("Perfect Fail")