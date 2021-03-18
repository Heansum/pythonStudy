personInfon = {
    "name": "이철수",
    "birth": "1990년 3월 18일",
    "address": "부산 부산진구 중앙대로 668",
    "tel": "010-1234-5678"
}

# 딕셔너리 주의사항 - key 가 중복될시에 데이터가 지워진다
name = personInfon["name"]
print("이름 = " + name)

menu = {
    "CaffeAmericano": "4600원",
    "CaffeLatte": "5100원",
    "Cappuccino": "5100원",
    "OatmealLatte": "5400원"
}

# key 와 value 추가
menu["DolceLatte"] = "6100원"
menu.setdefault("Espresso", "4100원")

menu.setdefault("DoubleShot", "4800원")

menu.setdefault("ColdBrew", "5000원")

# 딕셔너리의 여러 메서드들
keys = menu.keys()
print(keys)

values = menu.values()
print(values)

keyValue = menu.items()
print(keyValue)

