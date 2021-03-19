pocket = {'paper', 'cellphone', 'money'}

money = 'money' in pocket

if money:
    print("택시를 타고 가라")
else:
    print("걸어가라")

pocket = ['paper', 'cellphone']

card = True

money = 'money' in pocket

if money:
    print("택시를 타고 가라")
else:
    if card:
        print("택시를 타고 가라")
    else:
        print("걸어가라")
