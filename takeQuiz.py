from Quiz import Quiz

with open('quiztopics','r') as fo:
    topics = fo.readlines()

name = input('enter your name : ')
print(f'\nWelcome {name}')

print(f'you can take quiz in any of these {len(topics)} topics\n')
for i in range(len(topics)):
    print(f'{i+1}. {topics[i]}',end='')

topic = input('enter topic name in which u want to give test').lower()
quiz = Quiz(topic)
quiz.start()
result = quiz.result()
print(f'your result is {result}')

