def distinct_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(distinct_list([1, 3, 5, 2, 6, 1, 5, 3, 5, 2]))