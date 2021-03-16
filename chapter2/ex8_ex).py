# 어제의 기온을 입력 받는 부분
print("어제의 기온: ", end="")
temperature_yesterday = input()
temperature_yesterday = float(temperature_yesterday)

# 오늘의 기온을 입력 받는 부분
print("오늘의 기온: ", end="")
temperature_today = input()
temperature_today = float(temperature_today)

# 어제, 오늘 기온차를 계산하는 부분
gap = temperature_today - temperature_yesterday
print("어제와 오늘의 기온차는 ", gap, "도 입니다.")

# 계산 결과를 출력하는 부분