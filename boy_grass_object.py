from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)
    def update(self): pass
    
class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        
class BigBall:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.speed= random.randint(4, 20)
        self.image = load_image('ball41x41.png')
    def update(self):
        if self.y>75:
            self.y -= self.speed
            if self.y<75:
                self.y=75
    def draw(self):
        self.image.draw(self.x, self.y)
        
class SmallBall:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.speed= random.randint(4, 20)
        self.image = load_image('ball21x21.png')
    def update(self):
        if self.y>65:
            self.y -= self.speed
            if self.y<65:
                self.y=65
        
    def draw(self):
        self.image.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

def reset_world():
    global running
    global grass
    global team
    global SmallBalls
    global BigBalls
    running = True
    team = [Boy() for i in range(10)]
    BigballNum=random.randint(5,16)
    BigBalls = [BigBall() for i in range(BigballNum)]
    SmallBalls = [SmallBall() for i in range(20-BigballNum)]

    grass = Grass()
def update_world():
    grass.update()
    for boy in team:
        boy.update()
    for BigBall in BigBalls:
        BigBall.update()
    for SmallBall in SmallBalls:
        SmallBall.update()
        
    
def render_world():
    clear_canvas()
    grass.draw()
    
    for boy in team:
        boy.draw()
    for BigBall in BigBalls:
        BigBall.draw()
    for SmallBall in SmallBalls:
        SmallBall.draw()
    update_canvas()

# game main loop code
open_canvas()
reset_world()
while running:
    handle_events()
    update_world()
    render_world()

    delay(0.05)
close_canvas()
# finalization code

close_canvas()
