a=1
for i in range(100):
  b=a%3
  c=a%5
  if b==0 and c==0:
    print("FizzBuzz")
  elif b==0 and c!=0:
    print("Fizz")
  elif b!=0 and c==0:
    print("Buzz")
  else:
    print(a)
  a+=1
