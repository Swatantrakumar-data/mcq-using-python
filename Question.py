class Question:
    def __init__(self):
        self.question = ''
        self.options = []
        self.answer = 0

    def enter_question_anser(self):
        self.question = input('enter the question : ')
        for i in range(4):
            option = input(f'enter option {i+1} : ')
            self.options.append(option)

        self.answer = int(input('enter the correct option : '))

    def ask(self):
        print(self.question)
        for i in range(len(self.options)):
            print(f'{i+1}.  {self.options[i]}')

        your_answer = int(input('enter your option : '))
        return self.check(your_answer)

    def check(self,your_answer):
        if your_answer == self.answer:
            print('correct\n')
            return True
        else:
            print('wrong')
            print(f'option {self.answer} is correct')
            return False

# if __name__ == "__main__":
#     question1=Question()
#     question1.enter_question_anser()
#     question1.ask()
