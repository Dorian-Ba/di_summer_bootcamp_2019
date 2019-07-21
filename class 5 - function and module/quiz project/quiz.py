import random,json,os
quiz={}
def load_json_to_python():
    global quiz
    if not os.path.exists("quiz.json"):
        generate_json_quiz_file()
    else:
        quiz_file=open("quiz.json","r")
        quiz = json.load(quiz_file)
        quiz_file.close()

def load_python_to_json():
    global quiz
    quiz_file=open("quiz.json","w")
    quiz_file.write(json.dumps(quiz, indent=4))
    quiz_file.close()


def generate_json_quiz_file():
    operator=['+','-','*','/']
    global quiz

    for level in range(1, 11):
        level_label = 'quiz math level ' + str(level)
        quiz[level_label] = {}

        # Generate question number
        for question_number in range(1, 11):
            question_label = 'Q' + str(question_number)
            quiz[level_label][question_label] = {}

            if level<3:
                oper=random.choice(operator[:2])
            elif level<6:
                oper = random.choice(operator[:3])
            else:
                oper = random.choice(operator)


            number_from = 4 * level
            number_to = 4 * 4 * level
            number_a = random.randrange(number_from, number_to)
            number_b = random.randrange(number_from, number_to)


            total =eval(str(number_a)+oper+str(number_b))

            # Options
            option_list = []
            option_list.append(total)
            for o in range(1, 4):
                option = total + (random.randrange(-4*(level/2), 4*(level/2)))
                while(option in option_list):
                    option = total + (random.randrange(-4 * (level / 2), 4 * (level / 2)))
                option_list.append(option)
            random.shuffle(option_list)


            quiz[level_label][question_label]['question'] = str(number_a) + oper+ str(number_b) + '= ?'
            quiz[level_label][question_label]['options'] = option_list
            quiz[level_label][question_label]['answer'] = total

    load_python_to_json()


def generate_random_questions(level,number):
    question_level_dict = {}
    question_list = []
    question_level = quiz["quiz math level " + str(level)]
    questions_num_list = list(range(1, 11))
    random.shuffle(questions_num_list)
    for random_question_num in questions_num_list[:number]:
        question_number = 'Q' + str(random_question_num)
        question_list.append(question_level[question_number])

    question_level_dict["questions"] = question_list
    return question_level_dict


def quiz_maker(question_dict):
    score = 0
    question_list = question_dict['questions']

    for num,question in enumerate(question_list):
        test="""
                ___________________________________________________________________________
                Question {}:
                ============================
                {}
                ____________________________
                Choice:
                1 . {}
                2 . {}
                3 . {}
                4 . {}
                ____________________________
                Type your choice here:""".format(num+1,question['question'],question['options'][0],question['options'][1],question['options'][2],question['options'][3])


        user_answer = int(input(test))
        if question['options'][user_answer - 1] == question['answer']:
            score += 10
            print("Good answer - Score:",score)
        else:
            print("Bad answer - Score:", score)
    return score

def getLevelLen():
    return len(quiz['quiz math level 1'])