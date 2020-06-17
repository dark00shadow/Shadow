import pyglet
from pyglet.window import mouse, key
from RectangleCollision import *
from os import *
from MouseStuff import MouseStateHandler

print('block limit = 5, player limit = 1, goal limit = 1 and enemy limit = 2')
Enter = str(input('load or console? load/console>> '))
if Enter == 'load':
    LVL = 'games/' + str(input('the file >> '))
    FILE = open(LVL, 'r').read()
    Screen_Name = FILE.readline(1)
    screen_width = FILE.readline(2)
    screen_height = FILE.readline(3)
    class player():
        direction = ''
        posx = FILE.readline(4)
        posy = FILE.readline(5)
        oldposx = posx
        oldposy = posy
        image = pyglet.image.load('Textures/' + FILE.readline(6))
        width = FILE.readline(7)
        heght = FILE.readline(8)
    class block1():
        One = FILE.readline(9)
        if One == 'True':
            posx1 = FILE.readline(10)
            posy1 = FILE.readline(11)
            image1 = pyglet.image.load('Textures/' + FILE.readline(12))
            width1 = FILE.readline(13)
            heght1 = FILE.readline(14)
        Two = FILE.readline(15)
        if Two == 'True':
            posx2 = FILE.readline(16)
            posy2 = FILE.readline(17)
            image2 = pyglet.image.load('Textures/' + FILE.readline(18))
            width2 = FILE.readline(19)
            heght2 = FILE.readline(20)
        Three = FILE.readline(21)
        if Three == 'True':
            posx3 = FILE.readline(22)
            posy3 = FILE.readline(23)
            image3 = pyglet.image.load('Textures/' + FILE.readline(24))
            width3 = FILE.readline(25)
            heght3 = FILE.readline(26)
        Four = FILE.readline(27)
        if Four == 'True':
            posx4 = FILE.readline(28)
            posy4 = FILE.readline(29)
            image4 = pyglet.image.load('Textures/' + FILE.readline(30))
            width4 = FILE.readline(31)
            heght4 = FILE.readline(32)
        Five = FILE.readline(33)
        if Five == 'True':
            posx5 = FILE.readline(34)
            posy5 = FILE.readline(35)
            image5 = pyglet.image.load('Textures/'+ FILE.readline(36))
            width5 = FILE.readline(37)
            heght5 = FILE.readline(38)
        def solid(obj1x,obj1y,obj2x,obj2y,obj1w,obj1h,obj2w,obj2h):
            if collision.rectangle(obj1x,obj1y,obj2x,obj2y,obj1w,obj1h,obj2w,obj2h):
                if player.direction == 'up': player.posy -= 2
                if player.direction == 'down': player.posy += 2
                if player.direction == 'left': player.posx += 2
                if player.direction == 'right': player.posx -= 2
    class goal():
        show = False
        label_text = FILE.readline(39)
        label_size = FILE.readline(40)
        label_posx = FILE.readline(41)
        label_posy = FILE.readline(42)
        label = pyglet.text.Label(label_text, x=label_posx,y=label_posy,font_size=label_size)
        posx = FILE.readline(43)
        posy = FILE.readline(44)
        image = pyglet.image.load('Textures/' + FILE.readline(45))
        width = FILE.readline(46)
        heght = FILE.readline(47)
    class enemy1():
        One = FILE.readline(49)
        if One == 'True':
            posx1 = FILE.readline(50)
            posy1 = FILE.readline(51)
            image1 = pyglet.image.load('Textures/' + FILE.readline(52))
            width1 = FILE.readline(52)
            heght1 = FILE.readline(53)
        Two = FILE.readline(54)
        if Two == 'True':
            posx2 = FILE.readline(55)
            posy2 = FILE.readline(56)
            image2 = pyglet.image.load('Textures/' + FILE.readline(57))
            width2 = FILE.readline(58)
            heght2 = FILE.readline(59)
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
        image = pyglet.image.load('Textures/'+ str(input('player image>> ')))
        width = float(input('x size of player>> '))
        heght = float(input('y size of player>> '))
        print('Player created')
    class block1():
        One = str(input('block 1? False/True>> '))
        if One == 'True':
            posx1 = float(input('block1 position x>> '))
            posy1 = float(input('block1 position y>> '))
            image1 = pyglet.image.load('Textures/'+ str(input('block1 image>> ')))
            width1 = float(input('x size of block 1>> '))
            heght1 = float(input('y size of block 1>> '))
            print('block 1 created')
        Two = str(input('block 2? False/True>> '))
        if Two == 'True':
            posx2 = float(input('block2 position x>> '))
            posy2 = float(input('block2 position y>> '))
            image2 = pyglet.image.load('Textures/'+ str(input('block2 image>> ')))
            width2 = float(input('x size of block 2>> '))
            heght2 = float(input('y size of block 2>> '))
            print('block 2 created')
        Three = str(input('block 3? False/True>> '))
        if Three == 'True':
            posx3 = float(input('block3 position x>> '))
            posy3 = float(input('block3 position y>> '))
            image3 = pyglet.image.load('Textures/'+ str(input('block3 image>> ')))
            width3 = float(input('x size of block 3>> '))
            heght3 = float(input('y size of block 3>> '))
            print('block 3 created')
        Four = str(input('block 4? False/True>> '))
        if Four == 'True':
            posx4 = float(input('block4 position x>> '))
            posy4 = float(input('block4 position y>> '))
            image4 = pyglet.image.load('Textures/'+ str(input('block4 image>> ')))
            width4 = float(input('x size of block>> 4'))
            heght4 = float(input('y size of block>> 4'))
            print('block 4 created')
        Five = str(input('block 5? False/True>> '))
        if Five == 'True':
            posx5 = float(input('block5 position x>> '))
            posy5 = float(input('block5 position y>> '))
            image5 = pyglet.image.load('Textures/'+ str(input('block5 image>> ')))
            width5 = float(input('x size of block 5>> '))
            heght5 = float(input('y size of block 5>> '))
            print('block 5 created')
        def solid(obj1x,obj1y,obj2x,obj2y,obj1w,obj1h,obj2w,obj2h):
            if collision.rectangle(obj1x,obj1y,obj2x,obj2y,obj1w,obj1h,obj2w,obj2h):
                if player.direction == 'up': player.posy -= 2
                if player.direction == 'down': player.posy += 2
                if player.direction == 'left': player.posx += 2
                if player.direction == 'right': player.posx -= 2
    class goal():
        show = False
        label_text = str(input('text for you won label>> '))
        label_size = float(input('size of you won label>> '))
        label_posx = float(input('you won label position x>> '))
        label_posy = float(input('you won label position y>> '))
        label = pyglet.text.Label(label_text, x=label_posx,y=label_posy,font_size=label_size)
        posx = float(input('goal position x>> '))
        posy = float(input('goal position y>> '))
        image = pyglet.image.load('Textures/'+ str(input('goal image>> ')))
        width = float(input('x size of goal>> '))
        heght = float(input('y size of goal>> '))
        print('goal created')
    class enemy1():
        One = str(input('enemy 1? False/True>> '))
        if One == 'True':
            posx1 = float(input('enemy 1 position x>> '))
            posy1 = float(input('enemy 1 position y>> '))
            image1 = pyglet.image.load('Textures/'+ str(input('enemy 1 image>> ')))
            width1 = float(input('x size of enemy>> '))
            heght1 = float(input('y size of enemy>> '))
            print('enemy 1 created')
        Two = str(input('enemy 2? False/True>> '))
        if Two == 'True':
            posx2 = float(input('enemy 2 position x>> '))
            posy2 = float(input('enemy 2 position y>> '))
            image2 = pyglet.image.load('Textures/'+ str(input('enemy 2 image>> ')))
            width2 = float(input('x size of enemy 2>> '))
            heght2 = float(input('y size of enemy 2>> '))
            print('enemy 2 created')
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