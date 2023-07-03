import pygame #сама игровая библиотека
import random #получаем случайные числа (при генерации новых противников)
import time #модуль подсчета времени для игровых очков
from pygame.locals import *


class Person: #к данному классу относятся и САМ ИГРОК и ПРОТИВНИКИ (НО только ПРОТИВНИКИ используют МЕТОД MOVE!)
    def __init__(self, x, y, speed, image):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load(image)

    def move(self): #ТОЛЬКО ДЛЯ ПРОТИВНИКОВ! ПЕРЕДВИЖЕНИЕ ПРОТИВНИКА СО СРАВНЕНИЕМ ПОЛОЖЕНИЯ ИГРОКА
        if self.x < player.x:
            self.x += self.speed
        elif self.x > player.x:
            self.x -= self.speed
        if self.y < player.y:
            self.y += self.speed
        elif self.y > player.y:
            self.y -= self.speed

        global gameovercheck

        if self.x <= player.x + 64 and self.x >= player.x and self.y >= player.y and self.y <= player.y + 64: #УСЛОВИЕ ПРЕКРАЩЕНИЯ ИГРЫ, ПРОИГРЫЩ
            gameovercheck = True
            screen.blit(gameover, (0, 0))

        if self.x+64 <= player.x + 64 and self.x+64 >= player.x and self.y+64 >= player.y and self.y+64 <= player.y + 64:
            gameovercheck = True
            screen.blit(gameover, (0, 0))


pygame.init()   #СТАРТ, ИНИЦИАЛИЗАЦИЯ
screen = pygame.display.set_mode((1280, 720), 0, 32)
pygame.display.set_caption("First Python Game!")
back = pygame.image.load('back.png')
gameover = pygame.image.load('gameover.png')

font = pygame.font.Font(None, 25)
scorefont = pygame.font.Font(None, 60)
score = 0   #ИГРОВЫЕ ОЧКИ
gameovercheck = False #БУЛЕВО ЗНАЧЕНИЕ, ПРОИГРАЛИ ИЛИ НЕТ
time0 = time.time() #СЧЕТ ВРЕМЕНИ, ДЛЯ ИГРОВЫХ ОЧКОВ

enemynum = 3 #НОМЕР СЛЕДУЮЩЕГО ПРОТИВНИКА (ДЛЯ ГЕНЕРАЦИИ)
lastadd = 0 #КАКОГО ПРОТИВНИКА ДОБАВЛЯЛИ ПОСЛЕДНИЙ РАЗ

player = Person(100, 320, 4, 'player.png') #САМ ИГРОК (X,Y, СКОРОСТЬ, ТЕКСТУРА)
allplayers = [player] #СПИСОК, ПО НЕМУ БУДЕМ ПРОХОДИТСЯ В БЕСКОНЕЧНОМ ИГРОВОМ ЦИКЛЕ, ЧТОБЫ ВСЕ ПРОТИВНИКИ ДВИГАЛИСЬ, А ИГРОК ОТОБРАЖАЛСЯ

abouttext = font.render("GitHub: stepigor. Version 1.0.", True, (255, 255, 255))

mainLoop = True
while mainLoop: #БЕСКОНЕЧНЫЙ ИГРОВОЙ ЦИКЛ

    if gameovercheck == False: #ЕСЛИ НЕ ПРОИГРАЛИ
        
        if score == 5: #ВРЕМЯ ПОЯВЛЕНИЯ ПЕРВЫХ ПРОТИВНИКОВ
            try: #ИСПОЛЬЗУЕМ ДАННУЮ КОНСТРУКЦИЮ, ЧТОБЫ БЫТЬ УВЕРЕННЫМИ, ЧТО МЫ ЕЩЕ НЕ СОЗДАВАЛИ ПРОТИВНИКОВ, ИНАЧЕ ЗА ОДНУ СЕКУНДУ ПОЛЕ ЗАПОЛНИТСЯ ПРОТИВНИКАМИ
                enemy1
                enemy2
            except:
                enemy1 = Person(1000, 250, random.randint(0,3), 'enemy.png')
                enemy2 = Person(1000, 500, random.randint(0,3), 'enemy.png')
                allplayers.append(enemy1) #ДОБАВЛЯЕМ В ТОТ САМЫЙ СПИСОК, ЧТО БЫЛ ВЫШЕ
                allplayers.append(enemy2)

        if score > 29 and score % 30 == 0 and score != lastadd: #СЛЕДУЮЩИЕ ПРОТИВНИКИ, КАЖДЫЕ 30 ОЧКОВ
            try: #ИСПОЛЬЗУЕМ ДАННУЮ КОНСТРУКЦИЮ, ЧТОБЫ БЫТЬ УВЕРЕННЫМИ, ЧТО МЫ ЕЩЕ НЕ СОЗДАВАЛИ ПРОТИВНИКОВ, ИНАЧЕ ЗА ОДНУ СЕКУНДУ ПОЛЕ ЗАПОЛНИТСЯ ПРОТИВНИКАМИ
                globals()['enemy' + str(enemynum)]
            except KeyError:
                globals()['enemy' + str(enemynum)] = Person(random.randint(0,1200),random.randint(0,650),random.randint(0,3),'enemy.png');
                allplayers.append(globals()['enemy' + str(enemynum)])
                enemynum+=1
                lastadd = score

        time1 = time.time() #ВТОРОЕ ВРЕМЯ, ЧТОБЫ ВЫЧЕТОМ ПОЛУЧИТЬ АКТУАЛЬНЫЕ ОЧКИ (БЫЛ TIME0 ЕЩЕ)
        score = int(time1 - time0)
        scoretext = scorefont.render(str(score), True, (255, 255, 255))

        screen.blit(back, (0, 0))

        for i, item in enumerate(allplayers): #ПРОХОДИМСЯ ПО СПИСКУ, ЧТО БЫЛ ВЫШЕ (ГДЕ САМ ИГРОК И ПРОТИВНИКИ)
            screen.blit(item.image, (item.x, item.y))
            if i != 0: #ИСКЛЮЧАЕМ ИГРОКА (У НЕГО ID В СПИСКЕ 0), ТАК КАК ИМ УПРАВЛЯЕМ САМ ЧЕЛОВЕК, А НЕ КОМПЬЮТЕР
                item.move()

        keys_pressed = pygame.key.get_pressed() #ПЕРЕДВИЖЕНИЕ ГЛАВНОГО ГЕРОЯ
        if keys_pressed[K_d] and player.x < 1216:
            player.x += player.speed
        if keys_pressed[K_a] and player.x > 0:
            player.x -= player.speed
        if keys_pressed[K_w] and player.y > 0:
            player.y -= player.speed
        if keys_pressed[K_s] and player.y < 656:
            player.y += player.speed

        screen.blit(abouttext, (3, 695))
        screen.blit(scoretext, (1200, 15))

    else: #ЕСЛИ ПРОИГРАЛИ

        screen.blit(gameover, (0, 0))
        screen.blit(scoretext, (122, 400))
        
        key_press = pygame.key.get_pressed()
        
        if key_press[K_RETURN]: #НАЖИМАЕМ ENTER, ЧТОБЫ НАЧАТЬ СНАЧАЛА. ОБНУЛЯЕМ СЧЕТА, УДАЛЯЕМ ПРОТИВНИКОВ
            time0=time.time()
            time1=time.time()
            score = 0
            for i in range(1,enemynum):
                del globals()['enemy'+str(i)]
            lastadd = 0
            enemynum = 3
            allplayers = [player]
            gameovercheck = False

    for event in pygame.event.get(): #УСЛОВИЕ НОРМАЛЬНОГО ЗАКРЫТИЯ ИГРЫ НА КРЕСТИК В WINDOWS
        if event.type == QUIT:
            mainLoop = False

    pygame.display.update()

pygame.quit() #САМ ВЫХОД ИЗ ИГРЫ. НАХОДИТСЯ ВНЕ ИГРОВОГО ЦИКЛА, КОТОРЫЙ ПРЕРЫВАЕТСЯ В GAMEOVER (ПРИ НАЖАТИИ ENTER)