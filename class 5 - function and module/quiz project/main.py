import quiz
import scoring
#initialize
quiz.load_json_to_python()
scoring.load_json_to_python()

while True:
    print("""
            ----------------------------------------------------------
            Welcome to your math online quiz 
            ==================================
            1 - Start a new test 
            2 - Display scores
            3 - Exit 
            -----------------------------------------------------------""")

    user_choice = int(input("Please choose a number from the menu: "))

    if user_choice == 1:
            level = int(input("Please enter a level between 1 to 10: "))
            questions=quiz.generate_random_questions(number=5,level=level)
            score=quiz.quiz_maker(questions)
            print("Final score is {}".format(score))
            name="Please insert your name:"
            scoring.save_scoring(level=level,score=score,name=name)
            print(scoring.scoring)
    elif user_choice == 2:
            level = int(input("Please enter a level between 1 to 10: "))
            scoring.display_scoring(level)
    elif user_choice==3:
            scoring.load_python_to_json()
            break;
