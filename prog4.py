def shownumbers(x):
  for i in range(x+1):
    if(i%2==0):
      print("%d EVEN"%i)
    else:
      print("%d ODD"%i)
shownumbers(10)
d=int(input("enter limit:"))
shownumbers(d)

