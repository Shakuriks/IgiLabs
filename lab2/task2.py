import container
import re

while True:
    username = input("Enter username: ")
    if not re.findall(r'\b[A-z]\w+\b', username):
        print('Incorrect name.')
    else:
        container = container.Container(username)
        break

while True:
    command = input('> ').split()
    match command[0]:
        case 'add':
            if len(command) == 1:
                print('You entered the wrong command.')
            else:
                container.add(*command[1:])
        case 'remove':
            if len(command) != 2:
                print('You entered the wrong command.')
            else:
                container.remove(command[1])
        case 'find':
            if len(command) == 1:
                print('You entered the wrong command.')
            else:
                container.find(*command[1:])
        case 'list':
            if len(command) != 1:
                print('You entered the wrong command.')
            else:
                container.list()
        case 'grep':
            if len(command) == 3 and (command[2].lower() == 'true' or command[2].lower() == 'false'):
                if command[2].lower() == 'true':
                    container.grep(command[1], True)
                else:
                    container.grep(command[1], False)
            elif len(command) == 2:
                container.grep(command[1])
            else:
                print('You entered the wrong command.')
        case 'save':
            if len(command) != 1:
                print('You entered the wrong command.')
            else:
                container.save()
        case 'load':
            if len(command) != 1:
                print('You entered the wrong command.')
            else:
                container.load()
        case 'switch':
            if len(command) != 2:
                print('You entered the wrong command.')
            else:
                container.switch(command[1])
        case 'exit':
            if len(command) != 1:
                print('You entered the wrong command.')
            else:
                print('Would you like to save? (y/n):')
                while True:
                    answer = input('> ')
                    if answer == 'y' or answer == 'Y':
                        container.save()
                        break
                    elif answer == 'n' or answer == 'N':
                        break
                break
        case _:
            print('You entered the wrong command.')
