from math import sqrt
y_vals = []
closed_y_vals = []
def y_n(n):
  return (sqrt(13) + 2)/(sqrt(13))*(-1/4 + sqrt(13)/4)**n + (sqrt(13) - 2)/(sqrt(13))*(-1/4 - sqrt(13)/4)**n

for i in range(-2, 10):
  if i == -2:
    y_vals.append(4)
  elif i == -1:
    y_vals.append(2)
  else:
    y_vals.append(-0.5*y_vals[i-1] + 0.75*y_vals[i-2])
  
  closed_y_vals.append(y_n(i))

for i in range(-2, 10):
  print(f"y[{i}] = {y_vals[i+2]}")
  print(f"closed y[{i}] = {closed_y_vals[i+2]}")