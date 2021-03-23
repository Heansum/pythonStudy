interviewresult = [
    ("홍길동", "sbs@naver.com", 45),
    ("심봉사", "academy@gamil.com", 79),
    ("철수", "computer@daum.net", 85),
    ("영희", "art@naver.com", 99),
    ("이몽룡", "academy@naver.com", 69)
]

for (name, email, point) in interviewresult:
    if point < 80: continue

    print("\n");
    print("발신자 : <코리아 IT 아카데미학원>");
    print("수신자 : <{0}>".format(email))
    print("내용 : ");
    print("\t축하드립니다. %s님은 %d점으로 면접에 합격하셨습니다!" % (name, point))
    print(("=" * 50) )