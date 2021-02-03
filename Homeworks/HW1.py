#Question 1
# I got bored and decided to get a random value for length of list
# if the value is not divided by 2, the number which is in the middle stays and the halfs on either sides are replaced.
import random as rnd
value = rnd.randint(0, 100)

list1 = [i for i in range(0, value)]
print(list1)
print(len(list1)/2)

if len(list1) %2 == 0:
  listFirst = list(i for i in range(0, int(len(list1)/2)))
  listLast = list(k for k in range(int(len(list1)/2), int(len(list1))))
  list1 = listLast + listFirst
  print(list1)

else:
  mid = int(len(list1)/2)+1
  listFirst = list(i for i in range(0, mid))
  listMid = list(j for j in range(mid, mid +1))
  listLast = list(k for k in range(mid+1, int(len(list1))))
  list1 = listLast + listMid + listFirst
  print(list1)



#Question 2
# The while loop continues until the correct value is entered. Then, even numbers up to n are written to the newly created list evenNums and prints.

end = False

while not end:
    n = int(input("Please enter a single digit number: "))
    
    if n >= 10 and n < 0:
        print("Invalid Value")
    else:
    	end = True
    
evenNums = list(i for i in range(0, n+1) if i % 2 == 0)
print(evenNums)
