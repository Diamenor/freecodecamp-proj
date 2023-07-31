import numpy as np

def calculate(l):
  
  if len(l) < 9:
    raise ValueError("List must contain nine numbers.")
  else:
    L = np.reshape(l,(3,3))
      
    mean = [list(np.mean(L, axis=0)), list(np.mean(L, axis=1)), np.mean(L)]
    var = [list(np.var(L, axis=0)), list(np.var(L, axis=1)), np.var(L)]
    std = [list(np.std(L, axis=0)), list(np.std(L, axis=1)), np.std(L)]
    max = [list(np.max(L, axis=0)), list(np.max(L, axis=1)), np.max(L)]
    min = [list(np.min(L, axis=0)), list(np.min(L, axis=1)), np.min(L)]
    sum = [list(np.sum(L, axis=0)), list(np.sum(L, axis=1)), np.sum(L)]
  
    calculations = {'mean': mean,
                    'variance': var,
                    'standard deviation': std,
                    'max': max,
                    'min': min,
                    'sum': sum}
  return calculations    