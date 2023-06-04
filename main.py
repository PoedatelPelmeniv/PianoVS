import play
import pygame
pygame.init()
pygame.mixer.init() # Функція для відтворення звуку
play.set_backdrop((171, 128, 160)) # Колір фону за допомогою RGB

text1 = play.new_text(words = 'Це саме круте піаніно в світі,', x = 0, y = 220) # Текст вище
text2 = play.new_text(words = 'Гайда бринчать на піаніно!', x = 0, y = 175) # Текст нище

keys = []
sounds = []
for i in range(8):
    key_x = -180 + i * 50
    key = play.new_box(color='light blue', width = 40, height = 120, x = key_x, y = 0, border_width = 3, border_color = 'dark blue')
    keys.append(key)
    sound = pygame.mixer.Sound(str(i + 1) + '.ogg')
    sounds.append(sound)

@play.when_program_starts
def start():
    pass

@play.repeat_forever
async def play_piano():
    for j in range(8):
        if keys[j].is_clicked:
            sounds[j].play()
            keys[j].color = (23, 24, 120)
            await play.timer(0.5)
            keys[j].color = 'light blue'
play.start_program()