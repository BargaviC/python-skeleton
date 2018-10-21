# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question06(numServers, targetServer, times):
  # modify and then return the variable below
  answer = -1
  b=[]
  for i in range(len(times)):
      bi = []
      for j in range(len(times[0])):

          if i==j:
              bi.append(0)
          elif times[i][j] == 0:
              bi.append(1000000)
          else:
              bi.append(times[i][j])
      b.append(bi)
  for k in range(len(times)):
      for i in range(len(times)):
          for j in range(len(times)):
              b[i][j] = min(b[i][j], b[i][k]+b[k][j])
  answer = b[0][targetServer]

  return answer
