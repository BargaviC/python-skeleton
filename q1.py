# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  answer = 0
  ans = []
  for i in portfolios:
    for j in portfolios:
      ans.append(i ^ j)
  answer = max(ans)
  return answer

def toBinary(n):
  num = 0
  power = 0
  while(n > 0):
    num += (n % 2) * (10 ** power)
    n = n/2
    power += 1
  return num
