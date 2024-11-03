def check_guess(guess,answer):
    global score
    still_guessing=True
    attempt=0

    while still_guessing and attempt<3:
        if guess.lower()==answer.lower():
            print("Correct answer")
            score=score+1
            still_guessing=False
        else:
            if attempt<2:
                print("Wrong answer try again")
            attempt=attempt+1
    if attempt==3:
       
     print("The correct answer is:",answer)       

score=0
print("Guess the animal")

guess_1=input("Which bear lives near the North Pole?")
check_guess(guess_1,"Polar Bear")

guess_2=input("Which is the fastest land animal?")
check_guess(guess_2,"Cheetah")

guess_3=input("Which is the largest animal?")
check_guess(guess_3,"Blue whale")
print("Your score is:"+str(score))
