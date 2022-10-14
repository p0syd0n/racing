import arcade
import random
SCREEN_WIDTH = 960
SCREEN_HEIGTH = 720
SCREEN_TITLE= "racing"



class Yellow_car(arcade.Sprite):
    def update(self):
        self.center_x+=self.change_x
        if self.right >= SCREEN_WIDTH:
            self.right = SCREEN_WIDTH

        if self.left <= 0:
            self.left = 0


class Blue_car(arcade.Sprite):
    def update(self):
        self.center_y+=self.change_y
        if self.top <= 0:
            self.bottom=random.randint(SCREEN_HEIGTH, 820)
            self.center_x=random.randint(50, 960)
            window.points+=1
            self.change_y-=3
        
class Wall(arcade.Sprite):
    def update(self):
        self.center_y+=self.change_y
        if self.top <= 0:
            self.bottom=random.randint(SCREEN_HEIGTH, 820)
            self.center_x=random.randint(50, 960)
            window.points+=1
            self.change_y-=3

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGTH, SCREEN_TITLE)
        self.bg=arcade.load_texture('bg.png')
        self.explosion=arcade.load_texture('explosion.gif')
        self.my_car=Yellow_car('yellow_car.png', 1)
        self.other_car=Blue_car('blue_car.png', 1)
        self.wall=Wall('wall.png', 1)
        self.points=0
        self.lives=5
        self.game=True
        self.setup()
    
    def on_key_press(self, symbol: int, modifiers: int):
        if self.game:
            if symbol == arcade.key.RIGHT:
                self.my_car.change_x = 15
                self.my_car.angle = -20

            if symbol == arcade.key.LEFT:
                self.my_car.change_x = -15
                self.my_car.angle = 20



    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.my_car.change_x = 0
            self.my_car.angle = 0

        if symbol == arcade.key.LEFT:
            self.my_car.change_x = 0
            self.my_car.angle = 0

    def setup(self):
        self.my_car.center_x=SCREEN_WIDTH/2
        self.my_car.center_y=SCREEN_HEIGTH/5

        self.other_car.center_x=random.randint(50, 960)
        self.other_car.center_y=300
        self.other_car.change_y=-2    
        self.other_car.angle=180

        self.wall.center_x=random.randint(50, 960)
        self.wall.center_y=300
        self.wall.change_y=-2
    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGTH/2, SCREEN_WIDTH, SCREEN_HEIGTH, self.bg)
        self.my_car.draw()
        self.other_car.draw()
        self.wall.draw()
        arcade.draw_text(f"points: {self.points}", 10, SCREEN_HEIGTH-50, arcade.color.ANTIQUE_BRASS, 25)
        arcade.draw_text(f"lives: {self.lives}", 840, SCREEN_HEIGTH-50, arcade.color.ANTIQUE_BRASS, 25)

        if self.lives <= 0:
            self.game = False
            arcade.draw_texture_rectangle(self.my_car.center_x, self.my_car.center_y, self.explosion.width, self.explosion.height, self.explosion)
            arcade.draw_text(f"YOU LOST", SCREEN_WIDTH/2-250, SCREEN_HEIGTH/2, arcade.color.RED_DEVIL, 100)
        if self.points >= 20:
            self.game = False
            arcade.draw_text(f"YOU WON", SCREEN_WIDTH/2-250, SCREEN_HEIGTH/2, arcade.color.GREEN, 100)
        

    def update(self, delta_time: float):
        if self.game:
            self.my_car.update()
            self.other_car.update()
            self.wall.update()
            if arcade.check_for_collision(self.my_car, self.other_car):
                self.lives-=1
                self.points-=1
                self.other_car.bottom=random.randint(720, 820)
            if arcade.check_for_collision(self.my_car, self.wall):
                self.lives-=1
                self.points-=1
                self.wall.bottom=random.randint(720, 820)

window=Game()
arcade.run()

