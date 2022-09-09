#In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

import re

hand = open("regex_sum_1631968.txt")
sum_num=list()


for line in hand:
     number = re.findall('[0-9]+',line)
     sum_num = sum_num + number

total=0

for var_num in sum_num:
    total = total + int(var_num)

print(total)
