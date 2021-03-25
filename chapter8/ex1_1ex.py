with open("C:/Users/ITPS/Desktop/textex.txt", "r") as file:
    # 파일에 있는 모든 데이터를 불러올 때
    # readlines -> 테스트 용으로 모든 데이터를 불러올 때 사용하지 자주 사용하지는 않는다 --> 램 용량을 많이 먹기 때문에
    
    contents = file.readlines()
    for text in contents:
        print(text, end="")

    '''
    while True:
        contents = file.readline()

        if contents == "":
            break
        else:
            print(contents, end="")
    '''


#for i in range(1, 11):
 #   file.write("%d 번째 줄입니다.\n" % i)

'''

#file.write("1 번째 줄입니다.\n")
file.write("2 번째 줄입니다.\n")
file.write("3 번째 줄입니다.\n")
file.write("4 번째 줄입니다.\n")
file.write("5 번째 줄입니다.\n")
file.write("6 번째 줄입니다.\n")
file.write("7 번째 줄입니다.\n")
file.write("8 번째 줄입니다.\n")
file.write("9 번째 줄입니다.\n")
file.write("10 번째 줄입니다.\n")
'''


# textex.txt 파일의 마지막에
# 11번째 줄입니다. ~ 20번째 줄입니다. 내용을 덧붙이세요.

#for i in range(11, 21):
   # file.write("%d 번째 줄입니다.\n" % i)
   #content = file.readline()
    #print(content, end="")


#for i in range(1, 21):
 #   contents = file.readline()
  #  print(contents, end="")

# 파일 복사
# - 원본 파일에 들어있는 데이터를 읽어와서 변수에 저장한 뒤 새로운 파일에 저장하는 것
# 데이터의 종류
# - 텍스트 데이터 : 문자로 이루어진 데이터 / 주로 사람이 사용하는 데이터
# - 바이너리 데이터 : 0과 1로만 이루어진 데이터 / 주로 컴퓨터가 사용하는 데이터
#   - 음악, 동영상, 이미지 등...
# -

