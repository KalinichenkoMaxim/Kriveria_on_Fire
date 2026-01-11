import arcade
from arcade.gui import UIManager, UIFlatButton, UITextureButton, UILabel, UIInputText, UITextArea, UISlider, UIDropdown, UIMessageBox
from arcade.gui.widgets.layout import UIAnchorLayout, UIBoxLayout
import random
import choose_side

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

class Enterance(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, fullscreen=True)
        self.m = random.randint(1, 19)
        self.background = arcade.load_texture(f"background_images/{self.m}.jpg")
        self.sound = arcade.load_sound(f"soundtrack/{random.randint(1, 9)}.mp3", )
        self.logo = arcade.load_texture(f"background_images/Kriveria on Fire.png")

        
        self.manager = UIManager()
        self.manager.enable()
        
        self.anchor_layout = UIAnchorLayout()
        self.box_layout = UIBoxLayout(vertical=True, space_between=10)
        
        self.setup_widgets()
        
        self.anchor_layout.add(self.box_layout)
        self.manager.add(self.anchor_layout)

    def setup_widgets(self):
        arcade.play_sound(self.sound, volume=0.1)
        label = UILabel(
                    x=1000,
                    y=100,
                    text="Press any key...", 
                    font_size=50, 
                    text_color=arcade.color.WHITE, 
                    width=300)
        self.manager.add(label) 

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.background, arcade.rect.XYWH(960, 540, SCREEN_WIDTH, SCREEN_HEIGHT))
        arcade.draw_texture_rect(self.logo, arcade.rect.XYWH(500, 1000, 700, 50))
        self.manager.draw()
    
    def on_key_press(self, key, modifiers):
        if key:
            exit()


def setup_game(width=800, height=600, title="Kriveria on Fire"):
    game = Enterance(width, height, title)
    return game

def main():
    game = setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, "Kriveria on Fire")
    arcade.run()

if __name__ == "__main__":
    main()