# 출력스트림
# - 데이터가 프로그램에서 바깥으로 나가는 스트림
# 입력스트림
# - 데이터가 바깥에서 프로그램으로 들어오는 스트림

# open 함수를 사용해서
# 프로그램과 파일을 입력 스트림으로 연결할 수 있고

# open 함수를 사용해서
# 프로그램과 파일을 출력 스트림으로 연결할 수 있다.



# open 함수를 사용해서 프로그램과 파일을 연결할 수 있다.
# 입력스트림을 사용해서 연결할 수도 있고
# 출력스트림을 사용해서 연결할 수도 있다.

# 입력스트림을 사용해서 연결 - open("파일의 경로", "r")
# 파일에 있는 데이터를 프로그램에서 사용하겠다.

# 출력스트림을 사용해서 연결 - open("파일의 경로", "w")
# 프로그램에 있는 데이터를 파일에 저장하겠다.

# 잘못해서 r을 w로 썻다가 다시 r로 쓰면 파일 내용이 지워진다 ** 중요
file = open("C:/Users/ITPS/Desktop/text.txt", "r")

# file.write("Hello World~!")
contents = file.readline()
print(contents)


file.close()

