# The prime number has to be greater than 1. There are 25 number between 0-100.

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
