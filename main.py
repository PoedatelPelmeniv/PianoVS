import play
import pygame
pygame.init()
pygame.mixer.init() # Функція для відтворення звуку
play.set_backdrop((171, 128, 160)) # Колір фону за допомогою RGB
# Створення текстових спрайтів
text1 = play.new_text(words = 'Це саме круте піаніно в світі,', x = 0, y = 220) # Текст вище
text2 = play.new_text(words = 'Гайда бринчать на піаніно!', x = 0, y = 175) # Текст нище

# Створення перемекачів
piano_on = play.new_circle(color='dark blue', x = -170, y = -100, radius = 10, border_color = 'black', border_width = 3)
piano_txt = play.new_text(words = 'piano', x = -135, y = -100, font_size = 25)

violin_on = play.new_circle(color='dark blue', x = 80, y = -100, radius = 10, border_color = 'black', border_width = 3)
violin_txt = play.new_text(words = 'violin', x = 120, y = -100, font_size = 25)

guitar_on = play.new_circle(color='dark blue', x = -5, y = -100, radius = 10, border_color = 'black', border_width = 3)
guitar_txt = play.new_text(words = 'guitar', x = 35, y = -100, font_size = 25)

flute_on = play.new_circle(color='dark blue', x = -90, y = -100, radius = 10, border_color = 'black', border_width = 3)
flute_txt = play.new_text(words = 'flute', x = -50, y = -100, font_size = 25)

# Списки для клавіш і звуків
keys = [] 
sounds = []

for s in range(4):
    sounds.append([])
# Формуємо списки з клавішами та звуками
for i in range(8):
    key_x = -180 + i * 50
    key = play.new_box(color='light blue', width = 40, height = 120, x = key_x, y = 0, border_width = 3, border_color = 'dark blue')
    keys.append(key)
    sound = pygame.mixer.Sound(str(i + 1) + '.ogg')
    sounds[0].append(sound)
    sound = pygame.mixer.Sound('f' + str(i + 1) + '.ogg')
    sounds[1].append(sound)
    sound = pygame.mixer.Sound('g' + str(i + 1) + '.ogg')
    sounds[2].append(sound)
    sound = pygame.mixer.Sound('v' + str(i + 1) + '.ogg')
    sounds[3].append(sound)

get_instrument = 0

@play.when_program_starts
def start():
    pass

@piano_on.when_clicked
def piano_on():
    global get_instrument
    get_instrument = 0
    piano_on.color = 'black'
    flute_on.color = 'light blue'
    guitar_on.color = 'light blue'
    violin_on.color = 'light blue'

@flute_on.when_clicked
def flute_on():
    global get_instrument
    get_instrument = 1
    piano_on.color = 'light blue'
    flute_on.color = 'black'
    guitar_on.color = 'light blue'
    violin_on.color = 'light blue'

@guitar_on.when_clicked
def guitar_on():
    global get_instrument
    get_instrument = 2
    piano_on.color = 'light blue'
    flute_on.color = 'light blue'
    guitar_on.color = 'black'
    violin_on.color = 'light blue'

@violin_on.when_clicked
def violin_on():
    global get_instrument
    get_instrument = 3
    piano_on.color = 'light blue'
    flute_on.color = 'light blue'
    guitar_on.color = 'light blue'
    violin_on.color = 'black'

@play.repeat_forever
async def play_piano():
    for j in range(8):
        if keys[j].is_clicked:
            sounds[j].play()
            keys[j].color = (23, 24, 120)
            await play.timer(0.3)
            keys[j].color = 'light blue'
play.start_program() 