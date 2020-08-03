from pygame import mixer
mixer.init()
mixer.music.load("some.mp3")
mixer.music.play()
mixer.music.set_volume(0.1)
input("\033[31mEnter para parar")
