num = 137
flag = False
for i in range(2, num):
    if(num % i == 0):
        print(f"{num} is not simple")
        flag = True
        break
if(not flag):
    print(f"{num} is simple")
#print('5'+'5')