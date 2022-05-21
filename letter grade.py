"""
Your module description
"""
grades = int(input("What did you score on you test "))

if grades >=90:
        print('You got an A')
elif grades >=80 and grades <90:
        print('You got a B')
elif grades >=70 and grades <80:
        print('You got a C')
elif grades >=60 and grades <70:
        print('You got a D')
else:
        print('You got a F')