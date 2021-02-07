def primeNums():
    for i in range(0, 100+1):
        if i > 1:
                for k in range(2, i):
                    if i % k == 0:
                        break
                else:
                    print(i)          
        else:
            continue

            
primeNums()
