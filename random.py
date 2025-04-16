import random
print('''
+=====================================+
|  Welcome to the Total Random Game   |
+=====================================+

***************************************

+=====================================+
|              RULES                  |
+=====================================+
| 1. Choose a start and end number.   |
| 2. The computer picks a secret one. |
| 3. Random numbers are generated     |
|    until the secret one appears.    |
| 4. When it matches, the round ends. |
| 5. You can play again or quit.      |
| 6. DISCLAIMER!!! Can take forever   |
|    to end. Since Odds are completely|
|    random.                          |
+=====================================+''')

play = input("Are You Ready TO PLay(y/n): ").strip().lower()
if play != 'y':
    print('''
( T_T) 
Oh no, you're leaving?
I’ll be here waiting...
Come back soon, okay? 💔''')
    exit()
else:
    print('''
\\(^_^)/

I'm so happy 
you're playing!
Let's do this! 🎉

''')


while True:
    start = int(input("Enter start value : "))
    end = int(input("Enter end value : "))

    x = random.randrange(start, end)
    while True:
        if x == random.randrange(start, end):
            
            print(f"OH no its {x} you are out")
            break
        x = random.randrange(start,end)
        print(x)
    play_again = input("Would You Like To Play Again(y/n): ").strip().lower()
    if play_again != 'y':
        break
        
    
    
