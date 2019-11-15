def show_stars(x):
  for i in range(1,x+1):
    for j in range(1,i+1):
      print("*",end="")
    print("\r")
show_stars(5)
show_stars(10)
a=int(input("enter limit:"))
show_stars(a)
