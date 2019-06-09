termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
i=0
while i < 10:
   print('{}º termo: {}'.format(i+1, termo + (i * razao)))
   i += 1
