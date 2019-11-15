def speed(x):
  if(x<=70):
    c="OK"
  elif(x>70):
    d=x-70
    e=d//5
    if(e>12):
      c="License suspended"
    else:
      c="Point:%d"%e
  return c;
print(speed(50))
print(speed(150))
print(speed(90))
