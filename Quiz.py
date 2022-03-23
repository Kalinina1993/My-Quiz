def quiz():
    gritting = input("Your name: ")
    print(f"Hello, my dear, {gritting}. Let's play in one interesting game. I will ask you a question about the most "
          f"famous tv-show 'Friends'.\n Be careful and think twice before give the answer.\n In case of wrong answer "
          f"you will lose your points.\n For win you must score 10 points.Good luck!")
    points = 0
    question_1 = input("1 QUESTION.\n Name of the song that plays in the title credits: ")
    if question_1 == "I'll be there for you":
        print("Good job! Take 2 points")
        points += 2
        print(f"Your account {points}")
    else:
        points -= 2
        print("Are kidding?!Wrong!")
        print(f"You have {points}")
    question_2 = int(input("2 QUESTION.\n How many the best friends does Monika have?: "))
    if question_2 == 5:
        print("Yeah, baby")
        points += 2
        print(f"You have {points}")
    else:
        points -= 2
        print("Oh, no...")
        print(f"You have {points}")
    question_3 = int(input("3 QUESTION.\n How many wifes does Rose have?: "))
    if question_3 == 3:
        print("Rossodivorse here! It's correct answer")
        points += 2
        print(f"You have {points}")
    else:
        points -= 2
        print("I hope that your lover is not gay. It's incorrect answer")
        print(f"You have {points}")
    question_4 = input("4 QUESTION.\n Who is the first Joe's roommate?:")
    if question_4 == "Chandler":
        print("Jo and Chan forever!!!")
        points += 2
        print(f"You have {points}")
    else:
        print("No, no, no. You must see the firsts seasons, my friend")
        points -= 2
        print(f"You have {points}")
    question_5 = bool(input("LAST! 5 QUESTION.\n Phoebe has a tween sister. Is it TRUE or FALSE?:"))
    if question_5:
        print("That's right! You are cool!")
        points += 2
        print(f"You have {points}")
    else:
        print("Your don't see her? Really?")
        points -= 2
        print(f"You have {points}")

    while True:
        if points == 10:
            print("Congratulations! You win")
        else:
            print("You suck! Bye-bye")
            break


print(quiz())
