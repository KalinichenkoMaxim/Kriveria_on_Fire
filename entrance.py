import arcade
from arcade.gui import UIManager, UILabel
from arcade.gui.widgets.layout import UIAnchorLayout, UIBoxLayout
import random

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

class Enterance(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, fullscreen=True)
        self.m = random.randint(1, 19)
        self.background = arcade.load_texture(f"background_images/{self.m}.jpg")
        self.sound = arcade.load_sound(f"soundtrack/{random.randint(1, 9)}.mp3")
        self.logo = arcade.load_texture("background_images/Kriveria on Fire.png")
        self.choice_texture = arcade.load_texture('background_images/choice.png')
        self.manager = UIManager()
        self.manager.enable()
        
        self.anchor_layout = UIAnchorLayout()
        self.box_layout = UIBoxLayout(vertical=True, space_between=10)
        self.show_choice_flag = False
        
        self.setup_widgets()
        
        self.anchor_layout.add(self.box_layout)
        self.manager.add(self.anchor_layout)    

    def setup_widgets(self):
        arcade.play_sound(self.sound, volume=0.1)
        self.label = UILabel(
            x=1000,
            y=100,
            text="Press any key...", 
            font_size=50, 
            text_color=arcade.color.WHITE, 
            width=300
        )
        self.manager.add(self.label)

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.background, arcade.rect.XYWH(960, 540, SCREEN_WIDTH, SCREEN_HEIGHT))
        arcade.draw_texture_rect(self.logo, arcade.rect.XYWH(500, 1000, 700, 50))
        if self.show_choice_flag:
            arcade.draw_texture_rect(self.choice_texture, arcade.rect.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 1000, 500))
        self.manager.draw()
    
    def on_key_press(self, key, modifiers):
        if key:
            if self.label:
                self.manager.remove(self.label)
                self.label = None
                self.show_choice_flag = True
            return
        #ZZZZZ
        if key == arcade.key.F4 and (modifiers & arcade.key.MOD_ALT):
            arcade.close_window()
            return

def setup_game(width=800, height=600, title="Kriveria on Fire"):
    game = Enterance(width, height, title)
    return game

def main():
    game = setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, "Kriveria on Fire")
    arcade.run()

if __name__ == "__main__":
    main()