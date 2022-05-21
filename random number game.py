"""
Your module description
"""
run = True
while run:
    user_input = int(input('Enter Number: '))
    if user_input == 7:
        print('Congradulations, You won!')
        run = False
    elif user_input > 7:
        print("lower, try again")
    elif user_input < 7:
        print("higher, try again")
        continue
    
        
        