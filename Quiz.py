#from Question import Question
import pickle

class Quiz:
    correct_gain_points = 2
    wrong_gain_points = -1

    def __init__(self,topic):
        self.topic = topic
        self.filename = topic.lower().strip(' ') +'.pck'
        self.no_of_Qs = 5
        self.correct_answers = 0
        self.wrong_answers = 0
        self.score = 0
        self.total_score = 0

    def start(self):
        with open(self.filename,'rb') as fo:
            question_list = pickle.load(fo)



        self.total_score = self.no_of_Qs * Quiz.correct_gain_points

        for i in range(self.no_of_Qs):
            question = question_list[i]
            a=question.ask()
            if a == True:
                self.correct_answers += 1
            else:
                self.wrong_answers += 1

        print('........result.......')


    def result(self):
        print(f'correct ansers = {self.correct_answers}')
        print(f'wrong answers = {self.wrong_answers}')
        self.score = self.correct_answers * self.correct_gain_points + self.wrong_answers * self.wrong_gain_points
        return f'your result is {self.score}/{self.total_score}'

# if __name__ == '__main__':
#     quiz = Quiz('Maths')
#     quiz.start()
#     print(quiz.result())

