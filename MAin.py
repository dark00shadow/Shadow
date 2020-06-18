import pyglet
from pyglet.window import mouse, key
from RectangleCollision import *
from MouseStuff import MouseStateHandler
def read_line(filename, linenumber):
    with open(filename, 'r') as f:
        f.seek(linenumber)
        line = f.readline()
    return line.replace('\n', '')
    return line[:-1]
print('block limit = 5, player limit = 1, goal limit = 1 and enemy limit = 2')
print('load dont work right now')
Enter = str(input('load or console? load/console>> '))
if Enter == 'load':
    File = 'games/' + str(input('File name>> '))
    Screen_Name = read_line(File, 1)
    screen_width = read_line(File, 2)
    screen_height = read_line(File, 3)
    class player():
        direction = ''
        posx = read_line(File, 5)
        posy = read_line(File, 6)
        oldposx = posx
        oldposy = posy
        extract = 'textures/'+ read_line(File, 7)
        print(extract)
        image = pyglet.image.load(extract)
        width = read_line(File, 8)
        heght = read_line(File, 9)
        print('Player created')
    class block1():
        One = read_line(File, 11)
        if One == 'True':
            posx1 = read_line(File, 12)
            posy1 = read_line(File, 13)
            image1 = pyglet.image.load('textures/'+ read_line(File, 14))
            width1 = read_line(File, 15)
            heght1 = read_line(File, 16)
            print('block 1 created')
        Two = read_line(File, 18)
        if Two == 'True':
            posx2 = read_line(File, 19)
            posy2 = read_line(File, 20)
            image2 = pyglet.image.load('textures/'+ read_line(File, 21))
            width2 = read_line(File, 22)
            heght2 = read_line(File, 23)
            print('block 2 created')
        Three = read_line(File, 25)
        if Three == 'True':
            posx3 = read_line(File, 26)
            posy3 = read_line(File, 27)
            image3 = pyglet.image.load('textures/'+ read_line(File, 28))
            width3 = read_line(File, 29)
            heght3 = read_line(File, 30)
            print('block 3 created')
        Four = read_line(File, 32)
        if Four == 'True':
            posx4 = read_line(File, 33)
            posy4 = read_line(File, 34)
            image4 = pyglet.image.load('textures/'+ read_line(File, 35))
            width4 = read_line(File, 36)
            heght4 = read_line(File, 37)
            print('block 4 created')
        Five = read_line(File, 39)
        if Five == 'True':
            posx5 = read_line(File, 40)
            posy5 = read_line(File, 41)
            image5 = pyglet.image.load('textures/'+ read_line(File, 42))
            width5 = read_line(File, 43)
            heght5 = read_line(File, 44)
            print('block 5 created')
    class goal():
        show = False
        label_text = read_line(File, 46)
        label_size = read_line(File, 47)
        label_posx = read_line(File, 48)
        label_posy = read_line(File, 49)
        label = pyglet.text.Label(label_text, x=label_posx,y=label_posy,font_size=label_size)
        posx = read_line(File, 51)
        posy = read_line(File, 52)
        image = pyglet.image.load('textures/'+ read_line(File, 53))
        width = read_line(File, 54)
        heght = read_line(File, 55)
        print('goal created')
    class enemy1():
        One = read_line(File, 57)
        if One == 'True':
            posx1 = read_line(File, 58)
            posy1 = read_line(File, 59)
            image1 = pyglet.image.load('textures/'+ read_line(File, 60))
            width1 = read_line(File, 61)
            heght1 = read_line(File, 62)
            print('enemy 1 created')
        Two = read_line(File, 64)
        if Two == 'True':
            posx2 = read_line(File, 65)
            posy2 = read_line(File, 66)
            image2 = pyglet.image.load('textures/'+ read_line(File, 67))
            width2 = read_line(File, 68)
            heght2 = read_line(File, 69)
            print('enemy 2 created')
if Enter == 'console':
    Screen_Name = str(input('Screen Name>> '))
    screen_width = int(input('screen width>> '))
    screen_height = int(input('screen height>> '))
    class player():
        direction = ''
        posx = float(input('player position x>> '))
        posy = float(input('player position y>> '))
        oldposx = posx
        oldposy = posy
        image = pyglet.image.load('textures/'+ str(input('player image>> ')))
        width = float(input('x size of player>> '))
        heght = float(input('y size of player>> '))
        print('Player created')
    class block1():
        One = str(input('block 1? False/True>> '))
        if One == 'True':
            posx1 = float(input('block1 position x>> '))
            posy1 = float(input('block1 position y>> '))
            image1 = pyglet.image.load('textures/'+ str(input('block1 image>> ')))
            width1 = float(input('x size of block 1>> '))
            heght1 = float(input('y size of block 1>> '))
            print('block 1 created')
        Two = str(input('block 2? False/True>> '))
        if Two == 'True':
            posx2 = float(input('block2 position x>> '))
            posy2 = float(input('block2 position y>> '))
            image2 = pyglet.image.load('textures/'+ str(input('block2 image>> ')))
            width2 = float(input('x size of block 2>> '))
            heght2 = float(input('y size of block 2>> '))
            print('block 2 created')
        Three = str(input('block 3? False/True>> '))
        if Three == 'True':
            posx3 = float(input('block3 position x>> '))
            posy3 = float(input('block3 position y>> '))
            image3 = pyglet.image.load('textures/'+ str(input('block3 image>> ')))
            width3 = float(input('x size of block 3>> '))
            heght3 = float(input('y size of block 3>> '))
            print('block 3 created')
        Four = str(input('block 4? False/True>> '))
        if Four == 'True':
            posx4 = float(input('block4 position x>> '))
            posy4 = float(input('block4 position y>> '))
            image4 = pyglet.image.load('textures/'+ str(input('block4 image>> ')))
            width4 = float(input('x size of block>> 4'))
            heght4 = float(input('y size of block>> 4'))
            print('block 4 created')
        Five = str(input('block 5? False/True>> '))
        if Five == 'True':
            posx5 = float(input('block5 position x>> '))
            posy5 = float(input('block5 position y>> '))
            image5 = pyglet.image.load('textures/'+ str(input('block5 image>> ')))
            width5 = float(input('x size of block 5>> '))
            heght5 = float(input('y size of block 5>> '))
            print('block 5 created')
    class goal():
        show = False
        label_text = str(input('text for you won label>> '))
        label_size = float(input('size of you won label>> '))
        label_posx = float(input('you won label position x>> '))
        label_posy = float(input('you won label position y>> '))
        label = pyglet.text.Label(label_text, x=label_posx,y=label_posy,font_size=label_size)
        posx = float(input('goal position x>> '))
        posy = float(input('goal position y>> '))
        image = pyglet.image.load('textures/'+ str(input('goal image>> ')))
        width = float(input('x size of goal>> '))
        heght = float(input('y size of goal>> '))
        print('goal created')
    class enemy1():
        One = str(input('enemy 1? False/True>> '))
        if One == 'True':
            posx1 = float(input('enemy 1 position x>> '))
            posy1 = float(input('enemy 1 position y>> '))
            image1 = pyglet.image.load('textures/'+ str(input('enemy 1 image>> ')))
            width1 = float(input('x size of enemy>> '))
            heght1 = float(input('y size of enemy>> '))
            print('enemy 1 created')
        Two = str(input('enemy 2? False/True>> '))
        if Two == 'True':
            posx2 = float(input('enemy 2 position x>> '))
            posy2 = float(input('enemy 2 position y>> '))
            image2 = pyglet.image.load('textures/'+ str(input('enemy 2 image>> ')))
            width2 = float(input('x size of enemy 2>> '))
            heght2 = float(input('y size of enemy 2>> '))
            print('enemy 2 created')
def solid(obj1x,obj1y,obj2x,obj2y,obj1w,obj1h,obj2w,obj2h):
            if collision.rectangle(obj1x,obj1y,obj2x,obj2y,obj1w,obj1h,obj2w,obj2h):
                if player.direction == 'up': player.posy -= 2
                if player.direction == 'down': player.posy += 2
                if player.direction == 'left': player.posx += 2
                if player.direction == 'right': player.posx -= 2
class restart():
    def restart():
        goal.show = False
        player.posx = player.oldposx
        player.posy = player.oldposy
window = pyglet.window.Window(caption=Screen_Name,width=screen_width,height=screen_height)
key_handler = key.KeyStateHandler()
mouse_handler = MouseStateHandler()
window.push_handlers(key_handler)
window.push_handlers(mouse_handler)

@window.event
def on_draw():
    window.clear()
    if block1.One == 'True':
        block1.image1.blit(block1.posx1,block1.posy1)
    if block1.Two == 'True':
        block1.image2.blit(block1.posx2,block1.posy2)
    if block1.Three == 'True':
        block1.image3.blit(block1.posx3,block1.posy3)
    if block1.Four == 'True':
        block1.image4.blit(block1.posx4,block1.posy4)
    if block1.Five == 'True':
        block1.image5.blit(block1.posx5,block1.posy5)
    if enemy1.One == 'True':
        enemy1.image1.blit(enemy1.posx1,enemy1.posy1)
    if enemy1.Two == 'True':
        enemy1.image2.blit(enemy1.posx2,enemy1.posy2)
    goal.image.blit(goal.posx,goal.posy)
    if goal.show == True: goal.label.draw()
    player.image.blit(player.posx,player.posy)
P_Key_Pressed = False
U_Key_Pressed = False
play = False

def update1(dt):
    global play, U_Key_Pressed, P_Key_Pressed
    # Play mode
    if key_handler[key.P] and P_Key_Pressed == False and play == False:
        P_Key_Pressed = True
        play = True
        restart.restart()
    if key_handler[key.U] and U_Key_Pressed == False and play == True:
        P_Key_Pressed = True
        play = False

    if not key_handler[key.P] and P_Key_Pressed == True:
        P_Key_Pressed = False
    if not key_handler[key.U] and U_Key_Pressed == True:
        U_Key_Pressed = False
    # Collision
    if collision.rectangle(player.posx,player.posy,goal.posx,goal.posy,player.width,player.heght,goal.width,goal.heght):
        goal.show = True
    if enemy1.One == 'True':
        if collision.rectangle(player.posx,player.posy,enemy1.posx1,enemy1.posy1,player.width,player.heght,enemy1.width1,enemy1.heght1):
            restart.restart()
            play = False
    if enemy1.Two == 'True':
        if collision.rectangle(player.posx,player.posy,enemy1.posx2,enemy1.posy2,player.width,player.heght,enemy1.width2,enemy1.heght2):
            restart.restart()
            play = False
    # Restart if play = False
    if play == False: restart.restart()
    # Solid
    if block1.One == 'True': block1.solid(player.posx,player.posy,block1.posx1,block1.posy1,player.heght,player.width,block1.width1,block1.heght1)
    if block1.Two == 'True': block1.solid(player.posx,player.posy,block1.posx2,block1.posy2,player.heght,player.width,block1.width2,block1.heght2)
    if block1.Three == 'True': block1.solid(player.posx,player.posy,block1.posx3,block1.posy3,player.heght,player.width,block1.width3,block1.heght3)
    if block1.Four == 'True': block1.solid(player.posx,player.posy,block1.posx4,block1.posy4,player.heght,player.width,block1.width4,block1.heght4)
    if block1.Five == 'True': block1.solid(player.posx,player.posy,block1.posx5,block1.posy5,player.heght,player.width,block1.width5,block1.heght5)
    # Movment
    if play == True:
        if key_handler[key.W] and not key_handler[key.A] and not key_handler[key.D] and not key_handler[key.S]:
            player.posy += 2
            player.direction = 'up'
        if not key_handler[key.W] and not key_handler[key.A] and not key_handler[key.D] and key_handler[key.S]:
            player.posy -= 2
            player.direction = 'down'
        if not key_handler[key.W] and key_handler[key.A] and not key_handler[key.D] and not key_handler[key.S]:
            player.posx -= 2
            player.direction = 'left'
        if not key_handler[key.W] and not key_handler[key.A] and key_handler[key.D] and not key_handler[key.S]:
            player.posx += 2
            player.direction = 'right'
pyglet.clock.schedule_interval(update1, 1/120)
pyglet.app.run()