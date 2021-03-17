'''
논리 연산자 - 논리값(bool)을 연산하는 연산자
논리값 - True, False
True - 참, 1
False - 거짓, 0

True 또는 False 논리연산 True 또는 False

and - 두 값 모두 True 일 때 결과가 True  (그리고)
or - 두 값 중 하나만 True 이면 결과가 True (또는)
not - 결과를 반대로 바꾸는 연산자
'''

print(True and True)    # 논리곱 1*1
print(True and False)   #       1*0
print(False and True)   #       0*1
print(False and False)  #       0*0

print(True or True)     # 논리합 1+1
print(True or False)    #       1+0
print(False or True)    #       0+1
print(False or False)   #       0+0

print(not True)
print(not False)

