import random
question=input('Question:    ')
random_number=random.randint(1,9)
if random_number==1:
  a='Yes definitely.'
elif random_number==2:
  a='It is decidedly so.'
elif random_number==3:
  a='Without a doubt.'
elif random_number==4:
  a='Reply hazy, try again.'
elif random_number==5:
  a='Ask again later.'
elif random_number==6:
  a='Better not tell you now.'
elif random_number==7:
  a='My sources say no.'
elif random_number==8:
  a='Outlook not so good.'
else:
  a='Very doubtful.'
print(question)
print('Magic 8 Ball: '+a)
