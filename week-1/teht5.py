import random

feedback = []
correctCount = 0

print('Calculate the following equations:')

for i in range(5):
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    correct = a * b
    userInput = int(input(f'{a} * {b} = '))
    
    feedbackStr = ''
    
    if (userInput == correct):
        feedbackStr += 'Correct!'
        correctCount += 1
    else:
        feedbackStr += 'Incorrect! The correct answer is'
        
    feedback.append(f'{feedbackStr} {a} * {b} = {correct}')
    
feedback.append(f'You got {correctCount} correct!')

for str in feedback:
    print(str)
