# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  answer = 0
  ans = []
  for i in portfolios:
    for j in portfolios:

      if((i ^ j) > answer):
          answer = i ^ j
  return answer
