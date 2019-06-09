termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
i=0
qtd = 10
while i < qtd:
   print('{}º termo: {}'.format(i+1, termo + (i * razao)))
   i += 1
   if i == qtd:
       aux = int(input('Esses são os {} primeiros termos. Deseja mostrar quantos termos a mais? '.format(qtd)))
       qtd += aux
