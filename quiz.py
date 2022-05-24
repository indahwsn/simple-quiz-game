print('Quiz')
answer=input('Are you ready(yes/no) :')
score=0
total_questions=3
 
if answer.lower()=='yes':
    answer=input('Question 1: What is the most hardest programming language?')
    if answer.lower()=='malbolge':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
 
    answer=input('Question 2: What is the best programming language for data science')
    if answer.lower()=='python':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    answer=input('Question 3: What is the oldest programming language to learn?')
    if answer.lower()=='fortran':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
print('Your score',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('Thanks for playing!')
