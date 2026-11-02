print('-------Sorting hat-------')
q=int(input('Do you like Dawn or Dusk? \n1)Dawn \n2)Dusk\n'))
Gryffindor=0
Ravenclaw=0
Hufflepuff=0
Slytherin=0
if q==1:
  Gryffindor+=1
  Ravenclaw+=1
elif q==2:
  Hufflepuff+=1
  Slytherin+=1
else:
  print("Wrong input")
q=int(input("When I'm dead, I want people to remember me as: \n1)The good\n2)The great\n3)The wise\n4)The bold\n"))
if q==1:
  Hufflepuff +=2
elif q==2:
  Slytherin +=2
elif q==3:
  Ravenclaw +=2
elif q==4:
  Gryffindor +=2
else:
  print("Wrong input.")
q=int(input('Q3) Which kind of instrument most pleases your ear?\n1)The violin\n2)The trumpet\n3)The piano\n4)The drum\n'))
if q==1:
  Slytherin +=4
elif q==2:
  Hufflepuff +=4
elif q==3:
  Ravenclaw +=4
elif q==4:
  Gryffindor +=4
else:
  print("Wrong input.")
if Slytherin>Hufflepuff and Slytherin>Ravenclaw and Slytherin>Gryffindor:
  print("Slytherin has most points:",Slytherin)
elif Hufflepuff>Slytherin and Hufflepuff>Ravenclaw and Hufflepuff>Gryffindor:
  print("Hufflepuff has most points:",Hufflepuff)
elif Ravenclaw>Slytherin and Ravenclaw>Hufflepuff and Ravenclaw>Gryffindor:
  print("Ravenclaw has most points:",Ravenclaw)
elif Gryffindor>Ravenclaw and Gryffindor>Slytherin and Gryffindor>Hufflepuff:
  print("Gryffindor has most points:",Gryffindor)
else:
  print("there is a tie between houses")
