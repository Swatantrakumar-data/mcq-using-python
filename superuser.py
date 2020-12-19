from Question import Question
from Quiz import Quiz
import pickle
while True:
    print('1. create a new quiz file')
    print('2. add question to the existing quiz file')
    print('3. Exit')

    choice = input('enter ur choice')
    if choice != '1' and choice != '2':
        break

    with open('quiztopics','r') as fo:
        topics = [topic.strip() for topic in fo.readlines()]

    if choice == '1':
        topic = input('enter the new topic : ')
        if topic in topics:
            print('already present')
            continue

        with open('quiztopics','a') as fo:
            fo.write(f'{topic}\n')

        questions_list = []

    else:
        print(f'\nAvilable topics : {topics}')
        topic = input('enter the topic in which u want to add Q : ')
        if topic not in topics:
            print('this topic not in list, choose option 1 to create a new quiz file')
            continue

        filename = topic.lower().strip(' ') + '.pck'
        with open(filename,'rb') as fo:
            questions_list = pickle.load(fo)

        for question in questions_list:
            print(f'- {question}\n')

    while True:
        question = Question()
        question.enter_question_anser()
        questions_list.append(question)
        your_answer = input('wan to enter another response (y/n)')
        if your_answer == 'n':
            break

    filename = topic.lower().strip(' ') + '.pck'
    with open(filename,'wb') as fo:
        pickle.dump(questions_list,fo)
