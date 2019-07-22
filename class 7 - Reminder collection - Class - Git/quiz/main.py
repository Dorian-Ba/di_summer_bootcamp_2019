import quiz
import scoring
import login

def init_data():
    #initialize
    quiz.load_json_to_python()
    scoring.load_json_to_python()
    login.load_json_to_python()


def application_launcher():
    while True:
        print("""
                ----------------------------------------------------------
                Welcome {} to your math online quiz 
                ==========================================================
                1 - Start a new test 
                2 - Display scores
                3 - Use a different User 
                4 - Exit 
                -----------------------------------------------------------""".format(login.connected_user["username"]))

        user_choice = int(input("Please choose a number from the menu: "))

        if user_choice == 1:
                level = int(input("Please enter a level between 1 to 10: "))
                questions=quiz.generate_random_questions(number=5,level=level)
                score=quiz.quiz_maker(questions)
                print("Final score is {}".format(score))
                scoring.save_scoring(level=level,score=score,name=login.connected_user["username"])

        elif user_choice == 2:
                level = int(input("Please enter a level between 1 to 10: "))
                scoring.display_scoring(level)
        elif user_choice == 3:
                isLogged = login.log_in()
        elif user_choice==4:
                scoring.load_python_to_json()
                break;

def start():
    print("""
            ----------------------------------------------------------
            Login online quiz 
            ==========================================================
            1 - Connect 
            2 - Create new user
            3 - Exit 
            -----------------------------------------------------------""")

    user_choice = int(input("Please choose a number from the menu: "))

    while True:
        if user_choice==1:
            isLogged=login.log_in()
            if(isLogged):
                application_launcher()
                login.load_python_to_json()
                break
        elif user_choice==2:
            login.create_new_user()
            login.load_python_to_json()
            application_launcher()
            break
        elif user_choice==3:
            break
        else:
            user_choice = int(input("Incorrect input.Please choose a number from the menu: "))


init_data()
start()