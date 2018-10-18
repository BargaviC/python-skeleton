# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question03(numNodes, edgeList):
  # modify and then return the variable below
  answer = -1
  xs = set(map(lambda x: x[1], edgeList))
  ys = set(map(lambda x: x[0], edgeList))
  print xs, ys
  return answer

question03(3,[(1,2),(2,3)])
