from pygame import *
mixer.init()
mixer.music.load('Saint Cecilia.mp3')
mixer.music.play()
print('Tocando Foo Fighters!!!')
while mixer.music.get_busy():
    time.Clock().tick(10)


