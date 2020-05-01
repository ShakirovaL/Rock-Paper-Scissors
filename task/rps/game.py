from random import choice

name = input('Enter your name:')
print('Hello,', name)
options = input().split(',')
if options == ['']:
    options = ['paper', 'scissors', 'rock']
len_options = len(options)
scores = open('rating.txt')
score = 0
for line in scores:
    n, s = line.rstrip().split()
    if name == n:
        score = int(s)
len_opponents = (len_options - 1)//2
new_options = options[-len_opponents:]
new_options.extend(options)
beaten_by = {}
for i in range(len_options):
    beaten_by[new_options[i]] = new_options[(i+1):(i+1+len_opponents)]
print('Okay, let\'s start')
while True:
    human = input()
    if human in beaten_by.keys():
        computer = choice(list(beaten_by.keys()))
        if human == computer:
            print(f'There is a draw ({human})')
            score += 50
        elif computer in beaten_by[human]:
            print(f'Sorry, but computer chose {computer}')
        else:
            print(f'Well done. Computer chose {computer} and failed')
            score += 100
    elif human == '!exit':
        print('Bye!')
        break
    elif human == '!rating':
        print('Your rating:', score)
    else:
        print('Invalid input')
scores.close()
