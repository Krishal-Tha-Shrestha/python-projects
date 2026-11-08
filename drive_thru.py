def get_item(x):
  if x==1:
    return("Cheeseburger")
  elif x==2:
    return("Fries")
  elif x==3:
    return("Soda")
  elif x==4:
    return("Ice Cream")
  elif x==5:
    return("Cookie")
  else:
    return("Invalid option")
def welcome():
  print("------Welcome to dive thru--------")
  print("""What would you like to order?\n
  1.Cheeseburger 2.Fries 3.Soda 4.Ice Crean 5.Cookie""")  
welcome()
option=int(input("Enter your order:"))
print(get_item(option))
