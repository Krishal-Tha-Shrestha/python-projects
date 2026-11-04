
while True:
    name = input("What is your name player?\n")
    print(name, ',Sounds promising more than the ones before')
    print('Welcome to your new journey.\nIt wont be an easy road from here onwards.')

    option = 0
    while option != 3:
        try:
            option = int(input("Do you have any questions?\n1.Who are you?\n2.Where am i?\n3.No, proceed.\n"))
        except ValueError:
            print('Invalid input, please enter a number.')
            continue
        if option == 1:
            print('I am the one beyond all.')
        elif option == 2:
            print('You are in Reasearch and Development Laboratory, where we are trying to create a new species of human.')
        elif option == 3:
            print('Good, lets move on.')
        else:
            print('Invalid option, please try again.')

    print('You are in a dark laboratory, with only one door in front of you.')
    option = 0
    while option not in (1, 2, 3):
        try:
            option = int(input("What do you want to do?\n1.Open the door\n2.Look around\n3.Scream for help\n"))
        except ValueError:
            print('Invalid input, please enter a number.')
            continue
        if option not in (1, 2, 3):
            print('Invalid option, please try again.')

    if option == 1:
        print('You open the door and find a long corridor with flickering lights.')
        option = 0
        while option not in (1, 2, 3):
            try:
                option = int(input("What do you want to do?\n1.Walk down the corridor\n2.Go back to the laboratory\n3.Scream for help\n"))
            except ValueError:
                print('Invalid input, please enter a number.')
                continue
            if option not in (1, 2, 3):
                print('Invalid option, please try again.')
        if option == 1:
            print('You walk down the corridor and find a room with a strange machine in it.')
            while option not in (1, 2):
                try:
                    option = int(input("What do you want to do?\n1.Examine the machine\n2.Go back to the corridor\n"))
                except ValueError:
                    print('Invalid input, please enter a number.')
                    continue
                if option not in (1, 2):
                    print('Invalid option, please try again.')
            if option == 1:
                print('You examine the machine and find a control panel with a button that says "Activate".')
                try:
                    option = int(input("What do you want to do?\n1.Press the button\n2.Go back to the room\n"))
                except ValueError:
                    print('Invalid input, please enter a number.')
                    continue
                if option == 1:
                    print('You press the button and the machine starts to hum. Suddenly, a bright light fills the room and you feel yourself being pulled into the machine.')
                    print('You wake up in a strange place, with no memory of how you got there. You are now part of the new species of human that was being created in the laboratory.')
                    print('Congratulations, you have completed the game!')
        elif option == 2:
            print('You go back to the laboratory.')
        elif option == 3:
            print('You scream for help, but no one answers. The only sound you hear is your own echo.')
        else:
            print('Invalid option, please try again.')
    elif option == 2:
        print('You look around and find a table with some strange equipment and a note that says "Do not touch".')
        option = 0
        while option not in (1, 2, 3):
            try:
                option = int(input("What do you want to do?\n1.Touch the equipment\n2.Go back to the laboratory\n3.Scream for help\n"))
            except ValueError:
                print('Invalid input, please enter a number.')
                continue
            if option not in (1, 2, 3):
                print('Invalid option, please try again.')
        if option == 1:
            print('You touch the equipment and it starts to glow. Suddenly, a bright light fills the room and you feel yourself being pulled into the equipment.')
            print('You wake up in a strange place, with no memory of how you got there. You are now part of the new species of human that was being created in the laboratory.')
            print('Congratulations, you have completed the game!')
        elif option == 2:
            print('You go back to the laboratory.')
        elif option == 3:
            print('You scream for help, but no one answers. The only sound you hear is your own echo.')
        else:
            print('Invalid option, please try again.')
    elif option == 3:
        print('You scream for help, but no one answers. The only sound you hear is your own echo.')
        print('You were found by an unknow creature and eaten alive. Game Over.')
        try:
            option = int(input("Do you want to play again?\n1.Yes\n2.No\n"))
        except ValueError:
            print('Invalid input, please enter a number.')
            continue
        option = 0
        while option not in (1, 2):
            print('Invalid option, please try again.')
            try:
                option = int(input("Do you want     to play again?\n1.Yes\n2.No\n"))
            except ValueError:
                print('Invalid input, please enter a number.')
                continue
        if option == 1:
            print('Restarting the game...')
            continue
        elif option == 2:
            print('Thank you for playing!')
        break
