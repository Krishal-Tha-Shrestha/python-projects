import random
def get_number():
    option = [str(i) for i in range(1, 101)]
    number=random.choice(option)
    return number

def check(number):
    while True:
        guess=input("Enter your guess")
        if number==guess:
            print(f"You are right. The number was {number}")
            break
        else:
            print(f"You are wrong.")
            if (int(number)<int(guess)):
                print(f"It is smaller than {guess}")
            else:
                print(f"It is higher than {guess}")
            ask=input("do you want to try again?(y/n):")
            if ask!="y":
                print(f"The number was {number}")
                break


    number=get_number()
    check(number)
