import random

print('Sorteio de alunos em sequencia para uma apresentação ')

alunos = [ 'maria' , 'joão' , 'matheus' , 'Luís' ]
sequencia = random.shuffle(alunos)

print('A ordem de apresentação será :')
for i, num in enumerate(alunos, start=1) :
    print(f'{i}°   {num}')