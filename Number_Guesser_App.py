import random
chances = 5
correct_answer = random.randint(1, 50)
won = False
while chances>0 and not won:
    print('Chances remaining = ', chances)
    guess = int(input('Enter a number between 1 to 50: '))
    if guess == correct_answer:
        print("You win!")
        won = True
    elif guess>correct_answer and chances>1:
        print("Your guess is high. Guess lower\n")
    elif guess<correct_answer and chances>1:
        print("Your guess is low. Guess higher\n")
    chances -= 1
    if not won and chances == 0:
        print("You lose!. Answer is:", correct_answer)