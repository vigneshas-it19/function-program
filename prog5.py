def limit(x):
  count=0
  for i in range (x+1):
    if((i%3==0)or(i%5==0)):
      count=count+i
  return count;
print(limit(20))
print(limit(80))
print(limit(200))
