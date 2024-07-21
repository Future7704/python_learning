#initial code

# input_message = input('>')
# while input_message.lower() != 'quit':
#     if input_message.lower() == 'start':
#         print('Car started...Ready to go!')
#     elif input_message.lower() == 'stop':
#         print('Car stopped.')
#     elif input_message.lower() == 'help':
#         print('''
# start - to start the car
# stop - to stop the car
# quit - to exit
#             ''')
#     else:
#         print("I don't understand that...")
#     input_message = input('>')

#better code

# while True: #repeat the block till break
#     input_message = input('>').lower() #avoid using ".lower" repeatedly
#     if input_message == 'start':
#         print('Car started...Ready to go!')
#     elif input_message == 'stop':
#         print('Car stopped.')
#     elif input_message == 'help':
#         print('''
# start - to start the car
# stop - to stop the car
# quit - to exit
#             ''')
#     elif input_message == 'quit':
#         break
#     else:
#         print("I don't understand that...")

#advanced code

started = False
while True: #repeat the block till break
    input_message = input('>').lower() #avoid using ".lower" repeatedly
    if input_message == 'start':
        if started:
            print('The car has already started.')
        else:
            started = True
            print('Car started...Ready to go!')
    elif input_message == 'stop':
        if not started:
            print('The car has already stopped.')
        else:
            started = False
            print('Car stopped.')
    elif input_message == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to exit
            ''')
    elif input_message == 'quit':
        break
    else:
        print("I don't understand that...")