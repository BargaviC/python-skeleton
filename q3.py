# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question03(numNodes, edgeList):
  # modify and then return the variable below
  answer = -1
  nums = set([i for i in range(1, numNodes+1)])
  print nums
  xs = set(map(lambda x: x[1], edgeList))
  ys = set(map(lambda x: x[0], edgeList))
  print xs, ys
  excs = {}
  for i in ys:
    excs[i] = []
  for i in edgeList:
    excs[i[0]].append(i[1])
  print excs

  return answer

question03(3,[(1,2),(2,3)])
