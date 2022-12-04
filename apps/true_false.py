import time
from random import shuffle

q_n_as = [
    ['My favorite color is blue', 'T'],
    ['I hate animals', 'F'],
    ['I love cucumbers', 'F'],
    ['I speak some Turkish', 'T'],
    ['My parents have never divorced', 'F'],
    ['I graduated from a linguistic uni', 'T'],
    ['My name is rare in Belarus', 'T']
]
shuffle(q_n_as)

score = 0
start_time = time.perf_counter()
for q, a in q_n_as:
    my_answer = input(f'True or false: {q} ')
    if my_answer == a:
        score += 1
        print('Excellent!')
    else:
        print('Not correct.')
end_time = time.perf_counter()
print(f'Your score is {score}, time spent is {end_time - start_time}')