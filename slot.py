import random
symbols=['🍒','🍇', '🍉', '7️⃣']
def play():
  keep_playing="Y"

  while keep_playing.upper()=="Y":
    results=random.choices(symbols,k=3)
    print("|".join(results))
    if results.count("7️⃣")==3:
      print("Jackpot! 💰")
    else:
      print('Thanks for playing!')
    keep_playing=input('Keep playing Y/N?')
    while keep_playing.upper() not in ("Y","N"):
      print('Enter a valid input!')
      keep_playing=input('Keep playing Y/N?')
play()
