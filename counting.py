print("--------->")
#Greate Notest From
#https://www.wyzant.com/resources/answers/282513/how_many_integers_from_1_to_1000_inclusive_are_divisible_by_neither_2_nor_5
#----------
# I will be using a trick very similar to what you would see in probability class:
# The number of integers divisible by 2 from 1 to 1000 is 1000/2 = 500.
# The number of integers divisible by 5 from 1 to 1000 is 1000/5 = 200.
# The number of integers divisible by 2 AND 5 from 1 to 1000 is 1000/lcm(2,5) = 1000/10 = 100.
# The number of integers divisible by 2 OR 5 from 1 to 1000 is 500 + 200 - 100 = 600.
# <-- union minus intersection from probability
# The number of integers divisible by NEITHER 2 NOR 5 from 1 to 1000 is 1000 - 600 = 400.
# <-- complement from probability
# So your answer is 400 integers.
# These integers are the numbers ending in 1, 3, 7, and 9 (just in case you are curious).
# Final Answer
# 1- The number of integers divisible by 2 from 1 to 1000 is 1000/2 = >>> 500
# 2- The number of integers divisible by 3 from 1 to 1000 is 1000/3 >>> 333
# 3-The number of integers divisible by 2 AND 3 from 1 to 1000
# 1000/ (2*3) = 1000/6 = 166 this is intersection
# 4- The number of integers divisible by 2 OR 3 from 1 to 1000
# (500 + 333) - 166 = 667 this is union like in video
#
count = 0
for i in range(1,1001):
  if i %2 !=0 or i %3 !=0:
    count += 1
print(count)
