def fizz_buzz(x):
  if((x%3==0)and(x%5==0)):
    c="FizzBuzz"
  elif(x%3==0):
    c="Fizz"
  elif(x%5==0):
    c="Buzz"
  else:
    c=x
  return c;
print(fizz_buzz(9))
print(fizz_buzz(25))
print(fizz_buzz(15))
