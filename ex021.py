from pygame import *
mixer.init()
mixer.music.load('suamusica.mp3')
mixer.music.play()
print('Tocando!!!')
while mixer.music.get_busy():
    time.Clock().tick(10)


