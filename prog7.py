def limit(x):
  a=[]
  count=0
  for i in range(1,x+1):
    for j in range(1,x+1):
      if(i%j==0):
        count=count+1
    if(count==2):
      a.append(i)
    count=0
  return a;
print(limit(20))
print(limit(50))
a=int(input("enter limit:"))
print(limit(a))
