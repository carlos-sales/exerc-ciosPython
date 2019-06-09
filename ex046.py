from time import sleep
import emoji
print('Contagem regressiva!')
for i in range(10, 0, -1):
    print('{}...'.format(i))
    sleep(1)
print(emoji.emojize(':party_popper: Feliz ano novo! :star-struck:'))
